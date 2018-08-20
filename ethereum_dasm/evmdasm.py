#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
"""
Verbose EthereumVM Disassembler

OPCODES taken from:
    https://github.com/ethereum/go-ethereum/blob/master/core/vm/opcodes.go
    https://github.com/ethereum/yellowpaper/blob/master/Paper.tex
"""

import logging
import sys
import os
import time
from ethereum_dasm import utils
from ethereum_dasm.utils import colors
from ethereum_dasm.asm import BasicBlock
from ethereum_dasm.asm.registry import INSTRUCTION_MARKS_BASICBLOCK_END
from ethereum_dasm.asm.disassembler import EVMDisAssembler

try:
    import ethereum_dasm.symbolic.simplify as evmsimplify
    from ethereum_dasm.symbolic.simplify import get_z3_value
    supports_z3 = True
except ImportError as ie:
    supports_z3 = False

import textwrap
import tabulate
tabulate.PRESERVE_WHITESPACE = True


logger = logging.getLogger(__name__)

try:
    from ethereum_dasm.symbolic.mythril import symbolic_execute
    import z3
except ImportError as ie:
    symbolic_execute = None
    z3 = None
    logger.warning("Symbolic Execution not available: %s" % ie)

try:
    import pyetherchain.pyetherchain as pyetherchain
except ImportError as ie:
    pyetherchain = None
    logger.warning("pyetherchain not available: %s" % ie)


def format_comment_block(it, indent=0):
    s = [indent * " " + "/*******************************************************************"]
    for i in it:
        s.append((2+indent)*" "+ "%s" % i)
    s.append(indent*" "+ "*******************************************************************/")
    return "\n".join(s)


class Contract(object):
    """
    Main Input Class
    """

    def __init__(self, bytecode=None, address=None, static_analysis=True, dynamic_analysis=True):
        if not bytecode and not address:
            raise Exception("missing bytecode or contract address")

        if not bytecode:
            api = utils.EthJsonRpc("https://mainnet.infura.io/")
            bytecode = api.call(method="eth_getCode", params=[address, "latest"])["result"]

        self.bytecode = bytecode
        self.address = address
        self._evmcode = EvmCode(contract=self,
                                static_analysis=static_analysis, dynamic_analysis=dynamic_analysis)  # do not reference this directly, always use self.disassembly()

    @property
    def disassembly(self):
        if not self._evmcode.instructions:
            self._evmcode.disassemble(bytecode=self.bytecode)
        return self._evmcode

    @property
    def simplified(self):
        return evmsimplify(self.disassembly)

    @property
    def methods(self):
        return self.disassembly.functions

    def guess_abi(self, txs=30):
        """
        Guess the evmbytecodes ABI

        :return:
        """

        """
        1) get all sighashes from disassembly
        2) get all potential signatures 
        3) (optional) build the dict with sighashes we've already seen and verified on e.g. etherscan.io
        4) build abi.json
        """
        #todo: implement - this is just a quick hack

        if not self.address:
            raise Exception("address required.")


        etherchain = pyetherchain.EtherChain()
        account = etherchain.account(self.address)

        # try to get abi from etherchain
        try:
            abi = account.api.get_account_abi(account.address)
            if abi:
                return abi
        except Exception as e:
            # todo - JSONDecodeError or pyetherchainerror
            logger.warning("guess_abi: %r"%e)

        # guess abi from transactions
        # get all transaction inputs
        tx_inputs = set([])
        for t in account.transactions(
                start=0, length=txs, direction="in")["data"]:
            tx = pyetherchain.EtherChainTransaction(tx=t["parenthash"])
            if tx[0]["input"].strip():
                tx_inputs.add(tx[0]["input"])


        logger.debug("resolving %d unique inputs" % len(tx_inputs))

        online_sighash_to_pseudo_abi = {}

        for tx_input in tx_inputs:
            pseudo_abi = utils.signatures.ethereum_input_decoder.decoder.FourByteDirectory.get_pseudo_abi_for_input(utils.str_to_bytes(tx_input))
            lst_pa = list(pseudo_abi)
            # todo: hacky
            if lst_pa:
                online_sighash_to_pseudo_abi[lst_pa[0]["signature"]] = lst_pa

        # combine evm info with input decoder info
        abi_out = []
        for sighash, evmdismethod in self.disassembly.functions.items():
            # constant, inputs{name,type}, name, outputs{name,type}, payable, stateMutability, type, signature
            # "address":loc,
            #                                        "signature_ascii":ascii,
            #                                        "signatures": pot_funcsigs,
            #                                        "payable": True,#functions are payable by default
            #                                        "inputs": []}
            if not sighash.startswith("0x"):
                sighash = "0x%s"%sighash
            online_methods = online_sighash_to_pseudo_abi.get(sighash, [])
            online_input_method = {}
            for pa in online_methods:
                # list of online pseudo abis
                # check nr of parameters
                if len(pa["inputs"]) == len(evmdismethod.get("inputs")):
                    online_input_method = pa
                    break
            online_method = {}
            for pa in evmdismethod.get("signatures",[]):
                if len(pa["inputs"]) == len(evmdismethod.get("inputs")):
                    online_method = pa
                    break

            abi_method = {"signature": sighash,
                          "address": evmdismethod.get("address"),
                          "constant": None,  # we can probably check this this statically (no STORE) or dynamically
                          "name": online_input_method.get("name", online_method.get("name")),  # from 4byte.directory
                          "payable": evmdismethod.get("payable"),  # from static analysis
                          "stateMutability": None,  # no clue
                          "type": "function",
                          "inputs": online_input_method.get("inputs", evmdismethod.get("inputs", online_method.get("inputs"))),
                          "outputs":[],
                          }
            abi_out.append(abi_method)
        return abi_out


class EvmCode(object):
    """
    Main Disassembler Class

    designed like wdasm/idapro with instructions and annotations/tables with extra info per address
    """
    def __init__(self, contract, debug=False, static_analysis=True, dynamic_analysis=True):
        # args
        self.contract = contract
        self.debug = debug
        self.enable_static_analysis = static_analysis
        self.enable_dynamic_analysis = dynamic_analysis

        # init
        self.disassembler = EVMDisAssembler(debug=debug)

        self.first = None  # first instruction
        self.last = None  # last instruction

        self.instructions = []  # instructions as list to quickly jump to instruction at index
        self.instruction_at = {}  # address:instruction - quickly jump to instruction at address

        self.basicblocks = []  # basicblocks as list to quickly iter basicblocks sequentially
        self.basicblock_at = {}  # address:basicblock - quickly jump to basicblock at address
        # todo: basicblock with forking

        self.jumptable = {}  # address:JUMP(I) - quickly find jump instructions (instr.jumpto holds the destination)
        self.function_call_dispatcher_jumptable = {}  # address:JUMP(I) - of the dispatcher block 0
        self.xrefs_at = {}  # address:set(ref istruction,ref instruction) - address to instruction for JUMP xrefs

        self.functions = {}  # sighash: {"address","signature_ascii", "signatures", "payable", "inputs", "constant"}
        self.function_at = {}  # address (JUMPDEST): sighash

        self.name_for_location = {}  # address: function_name
        self.name_at = {}  # address:name # todo - to be implemented: replace the "operand" overwrite in instruction() with a global table for this
        self.comments_at = {}  # address:[comment,] todo implement in favor of instruction.annotation/basicblock.annotation
        self.annotations_at = {}  # address:[annot,] todo implement in favor of instruction.annotation/basicblock.annotation

        self.strings_at = {}  # collect potential strings in operands

        self.symbolic_state_at = {}  # address: [(node,state)] (1:n mapping) - the symbolic execution state at address (can be multiple as it is a graph)

        #self.gas_at = {}  # from symbolic execution: initial_gas - state.mstate.gas (gas up to instruction at address) # todo maybe implement

        self.duration = None

    def assemble(self, instructions=None):
        instructions = instructions or self.instructions
        return '0x' + ''.join(inst.serialize() for inst in instructions)

    def disassemble(self, bytecode=None):
        """
        Disassemble bytecode to [Instructions,]
        :param bytecode: evm bytecode
        :param analyze: perform analysis steps
        :return: iterator to instructions

        Example:

            for inst in self.disassembler.disassemble(bytecode):
                # return them as we process them
                yield inst
        """
        if not bytecode:
            return self.iterate()

        t_start = time.time()
        self.instructions = list(self.disassembler.disassemble(bytecode))

        self.instruction_at = dict((instr.address, instr) for instr in self.instructions)

        self.first = self.instructions[0]
        self.last = self.instructions[-1]

        self.basicblocks = list(EvmCode._get_basicblocks(self.instructions))
        self.basicblock_at = dict((bb.address, bb) for bb in self.basicblocks)

        self.jumptable = dict((instr.address, instr) for instr in self.instructions if instr.name in ("JUMP", "JUMPI"))

        # track strings >2 chars allascii
        self.strings_at = dict((instr.address, instr) for instr in self.instructions if instr.operand_bytes and len(instr.operand_bytes)>=2 and utils.is_all_ascii(instr.operand_bytes))

        # ---> run analysis <---
        self.analyze_static()
        self.analyze_dynamic()  # dynamic would be sufficient


        # timekeeping
        self.duration = time.time() - t_start

        # current = self.first
        return self.iterate()

    def iterate(self, first=None):
        """
        Iterate Blocks or Instructions (linked via .next)
        :param first: instruction
        :return: iterator
        """

        current = first or self.first
        yield current
        while current.next:
            current = current.next
            yield current

    def find(self, instruction, start=None):
        current = start or self.first
        while current:
            if instruction == current.name:
                yield current
            current = current.next

    def find_within_address_range(self, start=0, end=65535):
        current = start or self.first
        while current:
            if start <= current.address < end:
                yield current
            current = current.next

    def insert(self, instruction, index):
        self.instructions.insert(index, instruction)
        # fix jumptable in current code. adding length of current jump
        self.reload()

    def reload(self):
        self.disassemble(bytecode=self.assemble())  # reanalyze

    @staticmethod
    def _get_basicblocks(disasm):
        # listify it in order to resolve xrefs, jumps
        current_basicblock = BasicBlock(address=0, name="init")

        for i, nm in enumerate(disasm):
            if nm.name == "JUMPDEST":
                # jumpdest belongs to the new basicblock (marks the start)
                yield current_basicblock
                prevs_basicblock = current_basicblock
                current_basicblock = BasicBlock(address=nm.address,
                                                name="loc_%s" % hex(nm.address))

                # dbly linked for navigation <3
                prevs_basicblock.next = current_basicblock
                current_basicblock.previous = prevs_basicblock

            # add to current basicblock
            current_basicblock.instructions.append(nm)
            nm.basicblock = current_basicblock

        # yield the last basicblock
        yield current_basicblock

    def analyze_static(self):
        if not self.enable_static_analysis:
            return
        self._static_update_xrefs()  # update statically known XREFs
        self._reconstruct_function_signatures()  # find function signatures

    def _static_update_xrefs(self):
        """
        update instruction.jumpto and self.xrefs with JUMP based xref information
        limitation: can only resolve XREFS based on [PUSH,JUMP(I)]
        :return:
        """
        # find all JUMP, JUMPI's
        for loc, instruction in self.jumptable.items():
            if instruction.previous and instruction.previous.name.startswith("PUSH"):
                instruction.jumpto = int(instruction.previous.operand, 16)
                target_instruction = self.instruction_at.get(instruction.jumpto)
                if target_instruction and target_instruction.name == "JUMPDEST":
                    # valid address, valid target
                    self.xrefs_at.setdefault(instruction.jumpto, set([]))
                    self.xrefs_at[instruction.jumpto] = instruction
                    target_instruction.xrefs.add(instruction)
                else:
                    logger.error("invalid jump at %s" % instruction)

    def _reconstruct_function_signatures(self):

        # find CALLDATALOAD
        # find PUSH4 * JUMPI
        #   check next block for CALLDATALOAD to get number of args and length

        # get first instruction
        # check first 3 blocks:
        instr_calldataload = self.basicblock_at[0].skip_to(["CALLDATALOAD"])

        if not instr_calldataload or instr_calldataload.name != "CALLDATALOAD":
            return # todo remove
            raise Exception("missing CALLDATALOAD")

        loc_to_sighash = {}

        while instr_calldataload.name in ["CALLDATALOAD", "PUSH4", "EQ", "PUSH1", "PUSH2", "JUMPI"]:
            # abort on jumpdest
            ipushfuncsig = instr_calldataload.skip_to(
                ["CALLDATALOAD", "PUSH4", "EQ", "PUSH1", "PUSH2", "JUMPI", "JUMPDEST"])
            ieq = ipushfuncsig.skip_to(
                ["CALLDATALOAD", "PUSH4", "EQ", "PUSH1", "PUSH2", "JUMPI", "JUMPDEST"])
            ipushaddr = ieq.skip_to(
                ["CALLDATALOAD", "PUSH4", "EQ", "PUSH1", "PUSH2", "JUMPI", "JUMPDEST"])
            ijumpi = ipushaddr.skip_to(
                ["CALLDATALOAD", "PUSH4", "EQ", "PUSH1", "PUSH2", "JUMPI", "JUMPDEST"])

            if ipushfuncsig.name != "PUSH4" or ieq.name != "EQ" or not ipushaddr.name.startswith(
                    "PUSH") or ijumpi.name != "JUMPI":
                break

            loc_to_sighash[ijumpi.jumpto] = ipushfuncsig.operand
            # todo: save name_at[ipushfuncsig.address]

            # next instruction
            instr_calldataload = ijumpi

        # got all location to sighashes
        # resolve sighash
        for loc, sighash in loc_to_sighash.items():
            pot_funcsigs = utils.signatures.lookup_function_signature(sighash)
            if len(pot_funcsigs) == 0:
                ascii = "function 0x%s" % sighash
            elif len(pot_funcsigs) == 1:
                ascii = 'function %s' % pot_funcsigs[0]
            else:
                ascii = "function 0x%s"%sighash

            # todo: fixme
            self.functions[sighash] = {"address":loc,
                                       "signature_ascii": ascii,
                                       "signatures_ascii": pot_funcsigs,
                                       "signatures": [utils.signatures.ethereum_input_decoder.decoder.FourByteDirectory.parse_text_signature(s) for s in pot_funcsigs],
                                       "payable": True,#functions are payable by default
                                       "constant": None, # no write storage (replaced by view/pure)  todo
                                       "view": None, #no write storage  todo
                                       "pure": None, #no read/write storage  todo
                                       "inputs": []}

            # find next JUMP (marks end of funchead)
            args = []

            instr = self.instruction_at[loc]

            end_addr = instr.skip_to(["JUMP"]).address
            while instr.address < end_addr:
                instr = instr.skip_to(["CALLDATALOAD"])

                if not instr or not instr.previous or instr.address >= end_addr:
                    break

                p_instr = instr.previous
                while p_instr and p_instr.address>loc and not "JUMP" in p_instr.name and not "CALLDATALOAD" in p_instr.name:
                    if p_instr.name.startswith("PUSH"):
                        cdl_offset = int(p_instr.operand, 16)
                        args.append(cdl_offset)
                        break
                    p_instr = p_instr.previous
                instr = instr.next

            if args:
                num_args = len(args)
                sizes = []

                prevs = args[0]
                for nr,offset in enumerate(args):
                    if nr==0: continue
                    sizes.append("bytes%d"%(offset-prevs))
                    prevs = offset

                for _ in range(num_args-len(sizes)):
                    sizes.append("<bytes??>")

                self.functions[sighash]["inputs"] = sizes
            #
            #
            # check if payable
            #
            if self.basicblock_at[loc].find_sequence(["JUMPDEST", "CALLVALUE", "ISZERO", "PUSH", "JUMPI", "PUSH", "DUP", "REVERT"],
                                                     prn=lambda a, b: a.startswith(b)):  # we do not need an exact match
                self.functions[sighash]["payable"] = False


            # add annotations
            f = self.functions[sighash]
            self.instruction_at[loc].annotations.append(f["signature_ascii"])

            self.instruction_at[loc].annotations.append("payable: %r" % f["payable"])
            self.instruction_at[loc].annotations.append("inputs: (%d) %r" % (len(f["inputs"]), f["inputs"]))
            if f["signatures_ascii"]:
                self.instruction_at[loc].annotations.append("potential signatures: %r" % f["signatures_ascii"])

            self.function_at[loc] = f
            if f["signatures"]:
                self.name_for_location[loc] = "/*OR*/".join(_["name"] for _ in f["signatures"]) # in case multiple sigs returned
            else:
                # alt. use sighash as a label for location
                self.name_for_location[loc] = "0x%s" % sighash


    def analyze_dynamic(self):
        if not symbolic_execute or not self.enable_dynamic_analysis:
            return

        # run the symbolic execution
        logger.debug("running symbolic execution")
        symgraph = symbolic_execute(code=self.contract.bytecode, address=self.contract.address)
        logger.debug(repr(symgraph))

        # assign every address a block and states
        for node, state in symgraph.iterate_blocks_and_states():
            instr = state.get_current_instruction()
            self.symbolic_state_at.setdefault(instr['address'], [])
            self.symbolic_state_at[instr['address']].append((node, state))


        #print(set(self.symbolic_state_at.keys()).symmetric_difference(set(self.instruction_at.keys())))
        #print(self.symbolic_state_at.keys())
        #print(self.instruction_at.keys())
        #input("--")
        # -----------------------------
        #  analysis: jumps
        # -----------------------------
        # fix jump destinations
        # find all JUMP(I) s and get the location from stack
        for addr, instr in self.jumptable.items():  # all JUMP/I s
            # get symbolic stack
            for node, state in self.symbolic_state_at.get(addr,[]):  # todo investigate keyerror
                dst = z3.simplify(state.mstate.stack[-1]).as_long()
                if instr.jumpto and instr.jumpto != dst:  # todo: needs to be a set
                    logger.warning("Symbolic JUMP destination different: %s != %s" % (instr.jumpto, dst))
                instr.jumpto = dst

        # -----------------------------------------------
        #  analysis: calldataloads / function signatures
        # -----------------------------------------------


        # get calldataloads per block
        calldataloads = {}  # block: [instr,offset]

        for instr in self.find("CALLDATALOAD"):
            # get symbolic stack
            for node, state in self.symbolic_state_at.get(instr.address, []):
                cdl_offset = get_z3_value(state.mstate.stack[-1])  # get last item from stack (=offset)
                # calldata offset
                calldataloads.setdefault(node,[])
                calldataloads[node].append((instr, cdl_offset))
            # todo: implement like reconstruct method

        # -----------------------------------------------
        #  analysis: function modifiers reconstruction
        # -----------------------------------------------

        # todo implement the rest


class EVMDasmPrinter:
    """ utility class for different output formats
    """

    @staticmethod
    def listing(disasm, json=False):
        for i, nm in enumerate(disasm):
            if json:
                print(json.dumps({"name":nm.name, "operand":nm.operand}))
            else:
                print("%s %s" % (nm.name, nm.operand))

    @staticmethod
    def detailed(evmcode, resolve_funcsig=False):
        print("%-3s %-4s %-3s  %-15s %-36s %-30s %s" % (
            "Inst", "addr", " hex ", "mnemonic", "operand", "xrefs", "description"))
        print("-" * 150)
        # listify it in order to resolve xrefs, jumps
        for i, nm in enumerate(evmcode.instructions):
            if nm.name == "JUMPDEST":
                print(":loc_%s %s" % (hex(nm.address), "(%s)"%'  -->   '.join(nm.annotations)))
            try:
                operand = ','.join('%s@%s' % (x.name, hex(x.address)) for x in nm.xrefs) if nm.xrefs else ''
                print("%4d [%3d 0x%0.3x] %-15s %-36s %-30s # %s %s" % (i, nm.address, nm.address, nm.name,
                                                                    nm.describe_operand(resolve_funcsig=resolve_funcsig), # todo: get rid of this and use evmcode.name_at(nm.address)
                                                                    operand,
                                                                    nm.description,
                                                                    "returns: %r" % nm.returns if nm.returns else ""))
            except Exception as e:
                print(e)
            if nm.name in INSTRUCTION_MARKS_BASICBLOCK_END:
                print("")

    @staticmethod
    def basicblocks_detailed(evmcode, resolve_funcsig=False):

        # todo - remove annotations from objects and track them in evmcode
        print("%-4s   %-4s %-5s  %-3s | %-15s %-36s %-30s %s" % (
            "Inst", "addr", " hex ", "gas", "mnemonic", "operand", "xrefs", "description"))
        print("-" * 150)

        i = 0
        for bb in evmcode.basicblocks:
            # every basicblock
            print("%s %s" % (utils.colors.Color.location(":loc_%s" % hex(bb.address)),
                             "\n"+format_comment_block(bb.instructions[0].annotations, indent=2)+"\n" if bb.instructions[0].annotations else ""))
            for nm in bb.instructions:
                try:
                    operand = ','.join('%s@%s' % (x.name, hex(x.address)) for x in nm.xrefs) if nm.xrefs else ''
                    print("%4d [%-4s %-4s] %-3s | %-15s %-36s %-30s # %-60s %-30s %s" % (i,
                                                                                         utils.colors.Color.address(nm.address, fmt="%4d"),
                                                                                         utils.colors.Color.address(nm.address, fmt="0x%0.4x"),
                                                                                         utils.colors.Color.gas(nm.gas), utils.colors.Color.instruction(nm.name),
                                                                                         nm.describe_operand(
                                                                            resolve_funcsig=resolve_funcsig),  # todo: get rid of this and use evmcode.name_at(nm.address)
                                                                                         operand,
                                                                                         nm.description,
                                                                                         "returns: %s" % ', '.join(nm.returns) if nm.returns else "",
                                                                                         "args: %s" % ', '.join(nm.args) if nm.args else ""))

                except Exception as e:
                    print(e)

                i += 1
            if nm.name in INSTRUCTION_MARKS_BASICBLOCK_END:
                print("")

    @staticmethod
    def basicblocks_detailed_tabulate(evmcode, resolve_funcsig=False):
        headers = ["  %-4s   %-4s %-5s   %-3s | %-15s %-36s" % ("Inst", "addr", " hex ", "gas", "mnemonic", "operand"),
                   "xrefs", "description", "retval", "args"]

        lines = []
        # todo - remove annotations from objects and track them in evmcode

        i = 0
        for bb in evmcode.basicblocks:
            # every basicblock

            lines.append(["%s %s" % (utils.colors.Color.location(":loc_%s" % hex(bb.address)),
                             "\n" + format_comment_block(bb.instructions[0].annotations, indent=2) + "\n" if
                             bb.instructions[0].annotations else "")])

            for nm in bb.instructions:
                try:
                    operand = ','.join('%s@%s' % (x.name, utils.colors.Color.location(hex(x.address))) for x in nm.xrefs) if nm.xrefs else ''

                    lines.append(["  %4d [%-4s %-4s ] %-3s | %-15s %-36s" % (i,
                                                                          utils.colors.Color.address(nm.address, fmt="%4d"),
                                                                          utils.colors.Color.address(nm.address, fmt="0x%0.4x"),
                                                                          utils.colors.Color.gas(nm.gas),
                                                                          utils.colors.Color.instruction(nm.name),
                                                                          nm.describe_operand(resolve_funcsig=resolve_funcsig),),

                                 # todo: get rid of this and use evmcode.name_at(nm.address)
                                 operand,
                                 '\n  '.join(textwrap.wrap("%s %s" % (utils.colors.Color.description("#"), nm.description))),
                                 '\n'.join(textwrap.wrap(', '.join(nm.returns) if nm.returns else "", width=20)),
                                 '\n'.join(textwrap.wrap(', '.join(nm.args) if nm.args else "", width=20))])

                except Exception as e:
                    print(e)

                i += 1
            if nm.name in INSTRUCTION_MARKS_BASICBLOCK_END:
                lines.append([" "])
        print(tabulate.tabulate(lines, headers=headers, numalign="right"))




def main():
    logging.basicConfig(format="%(levelname)-7s - %(message)s", level=logging.WARNING)
    from optparse import OptionParser
    usage = """usage: %prog [options]

       example: %prog [-L -F -v] <file_or_bytecode>
                %prog [-L -F -v] # read from stdin
                %prog [-L -F -a <address>] # fetch contract code from infura.io
    """
    parser = OptionParser(usage=usage)
    loglevels = ['CRITICAL', 'FATAL', 'ERROR', 'WARNING', 'WARN', 'INFO', 'DEBUG', 'NOTSET']
    parser.add_option("-v", "--verbosity", default="critical",
                      help="available loglevels: %s [default: %%default]" % ','.join(l.lower() for l in loglevels))
    parser.add_option("-L", "--listing", action="store_true", dest="listing",
                      help="disables table mode, outputs assembly only")
    parser.add_option("-F", "--no-online-lookup", action="store_false", default=True, dest="function_signature_lookup",
                      help="disable online function signature lookup")
    parser.add_option("-a", "--address",
                      help="fetch contract bytecode from address")
    parser.add_option("-C", "--no-color", dest="no_color", default=False, action="store_true",
                      help="disable color mode (requires pip install colorama)")
    parser.add_option("-A", "--guess-abi", dest="guess_abi", default=False, action="store_true",
                      help="guess the ABI for that contract")
    parser.add_option("-D", "--no-dynamic-analysis", dest="dynamic_analysis", default=True, action="store_false",
                      help="disable dynamic analysis / symolic execution")
    parser.add_option("-S", "--no-static-analysis", dest="static_analysis", default=True, action="store_false",
                      help="disable static analysis")
    parser.add_option("-s", "--simplify", dest="simplify", default=False, action="store_true",
                      help="simplify disassembly to human readable code")

    # parse args
    (options, args) = parser.parse_args()

    if options.verbosity.upper() in loglevels:
        options.verbosity = getattr(logging, options.verbosity.upper())
        logger.setLevel(options.verbosity)
    else:
        parser.error("invalid verbosity selected. please check --help")

    if options.no_color:
        utils.colors.colorama = None  # override the import to disable colorama

    if not options.dynamic_analysis:
        symbolic_execute = None  # hack hack

    if options.function_signature_lookup and not utils.signatures.ethereum_input_decoder:
        logger.warning("ethereum_input_decoder package not installed. function signature lookup not available.(pip install ethereum-input-decoder)")

    # get bytecode from stdin, or arg:file or arg:bytcode

    if options.address:
        contract = Contract(address=options.address,
                            static_analysis=options.static_analysis, dynamic_analysis=options.dynamic_analysis)
    elif not args:
        contract = Contract(bytecode=sys.stdin.read(),
                            static_analysis=options.static_analysis, dynamic_analysis=options.dynamic_analysis)
    else:
        if os.path.isfile(args[0]):
            contract = Contract(bytecode=open(args[0], 'r').read(),
                                static_analysis=options.static_analysis, dynamic_analysis=options.dynamic_analysis)
        else:
            contract = Contract(bytecode=args[0],
                                static_analysis=options.static_analysis, dynamic_analysis=options.dynamic_analysis)

    #logger.debug(INSTRUCTIONS_BY_OPCODE)

    # print dissasembly
    if options.listing:
        EVMDasmPrinter.listing(contract.disassembly)
    else:
        #evm_dasm.disassemble(contract.bytecode)
        EVMDasmPrinter.basicblocks_detailed_tabulate(contract.disassembly,
                                                     resolve_funcsig=options.function_signature_lookup)
        #print(evm_dasm.functions)  ## print detected functions
        #EVMDasmPrinter.detailed(evm_dasm.disassemble(evmcode), resolve_funcsig=options.function_signature_lookup)

    logger.info("finished in %0.3f seconds." % contract.disassembly.duration)
    # post a notification that disassembly might be incorrect due to errors
    if contract.disassembly.disassembler.errors:
        logger.warning("disassembly finished with %d errors" % len(contract.disassembly.disassembler.errors))
        if options.verbosity >= 30:
            logger.warning("use -v INFO to see the errors")
        else:
            for e in contract.disassembly.disassembler.errors:
                logger.info(e)

    if options.guess_abi:
        print("=" * 30)
        print("reconstructed ABI:")
        print(contract.guess_abi())

    # ------ testing area

    if options.simplify:
        print("======================[simplified]")
        print("")
        for x in contract.simplified:
            print(x)

    # ------ testing area

    # quick check
    logger.debug("assemble(disassemble(evmcode))==",
                 contract.bytecode.strip() == ''.join(contract.disassembly.assemble(contract.disassembly.disassemble())))

    # -- exit --
    sys.exit(len(contract.disassembly.disassembler.errors))


if __name__ == "__main__":
    main()
