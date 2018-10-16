#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
"""
console output writer
"""


from ethereum_dasm import utils
from ethereum_dasm.utils import colors
import ethereum_dasm.asm.registry as registry
import textwrap
import tabulate
tabulate.PRESERVE_WHITESPACE = True


def format_comment_block(it, indent=0):
    s = [indent * " " + "/*******************************************************************"]
    for i in it:
        s.append((2+indent)*" "+ "%s" % i)
    s.append(indent*" "+ "*******************************************************************/")
    return "\n".join(s)


class EVMDasmPrinter:
    """ utility class for different output formats
    """

    @staticmethod
    def listing(evmcode, json=False):
        for i, nm in enumerate(evmcode.instructions):
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
            if nm.name in registry.INSTRUCTION_MARKS_BASICBLOCK_END:
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
                                                                                         "returns: %s" % ', '.join(map(str,nm.returns)) if nm.returns else "",
                                                                                         "args: %s" % ', '.join(map(str,nm.args)) if nm.args else ""))

                except Exception as e:
                    print(e)

                i += 1
            if nm.name in registry.INSTRUCTION_MARKS_BASICBLOCK_END:
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
                                 '\n'.join(textwrap.wrap(', '.join(map(str,nm.returns)) if nm.returns else "", width=20)),
                                 '\n'.join(textwrap.wrap(', '.join(map(str,nm.args)) if nm.args else "", width=20))])

                except Exception as e:
                    print(e)

                i += 1
            if nm.name in registry.INSTRUCTION_MARKS_BASICBLOCK_END:
                lines.append([" "])
        print(tabulate.tabulate(lines, headers=headers, numalign="right"))