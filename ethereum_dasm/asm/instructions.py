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
import random
import ethereum_dasm.utils as utils
import evmdasm.instructions

logger = logging.getLogger(__name__)


class BasicBlock(object):

    def __init__(self, address=None, name=None, instructions=None):
        self.instructions = instructions or []
        self.address = address
        self.name = name
        self.annotations = []

        self.next = None
        self.previous = None

    def __repr__(self):
        return "<BasicBlock 0x%x instructions:%d>" % (self.address, len(self.instructions))

    def skip_to(self, names):
        for instr in self.instructions:
            if any(instr.name==name for name in names):
                return instr
        return None

    def find_sequence(self, seq, prn=lambda a,b:a==b):
        i_instr = iter(self.instructions)

        try:
            i = 0
            seqlen = len(seq)
            while True:
                instr = next(i_instr)
                if prn(instr.name,seq[i]):
                    i += 1
                elif i > 0:
                    # abort no match
                    break
                if i+1==seqlen:
                    return True
        except StopIteration:
            print("STOPITER")
            pass
        return False


class Instruction(evmdasm.instructions.Instruction):

    def __init__(self, opcode, name, length_of_operand=0, description=None, args=None, returns=None, gas=-1,
                 category=None, pops=None, pushes=None, fork=None):
        super().__init__(opcode=opcode, name=name,
                         length_of_operand=length_of_operand,
                         description=description,
                         args=args, returns=returns,
                         gas=gas, category=category,
                         pops=pops, pushes=pushes, fork=fork)

        # additional attribs
        self.annotations = []
        self.xrefs = set([])
        self.jumpto = None
        self.basicblock = None

    @staticmethod
    def from_evmdasm_instruction(evmdasm_instruction):
        return Instruction()

    def randomize_operand(self):
        self.operand_bytes = bytes(bytearray(random.getrandbits(8) for _ in range(self.length_of_operand)))
        return self

    def describe_operand(self, resolve_funcsig=False):
        if not self.operand:
            str_operand = ''
        elif resolve_funcsig and len(self.operand) == 8 and self.address < 0x100:
            # speed improvment: its very unlikely that there will be funcsigs after addr 400
            # 4bytes, could be a func-sig
            logger.info("online sighash lookup for: %s"%self.operand)
            pot_funcsigs = utils.signatures.lookup_function_signature(self.operand)
            if len(pot_funcsigs) == 0:
                ascii = ''
            elif len(pot_funcsigs) == 1:
                ascii = '  --> \'function %s\'' % pot_funcsigs[0]
            else:
                ascii = '  --> *ambiguous* \'function %s\'' % pot_funcsigs[0]

            str_operand = "0x%s%s" % (self.operand, ascii)
        elif len(self.operand_bytes) >= 4:
            try:
                ascii = ' (%r)' % self.operand_bytes.decode("utf-8") \
                    if self.operand_bytes and utils.is_ascii_subsequence(self.operand_bytes) else ''
            except UnicodeDecodeError:
                ascii = ''
            str_operand = "0x%s%s" % (self.operand, ascii)
        else:
            ascii = ''
            str_operand = "0x%s%s" % (self.operand, ascii)

        extra = "@%s" % hex(self.jumpto) if self.jumpto else ''
        return "%s%s" % (str_operand, extra)
