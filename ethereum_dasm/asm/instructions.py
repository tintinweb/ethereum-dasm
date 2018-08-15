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
import itertools
import random
import ethereum_dasm.utils as utils

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


class Instruction(object):
    """ Base Instruction class

        doubly linked
    """

    def __init__(self, opcode, name, length_of_operand=0, description=None, args=None, returns=None, gas=-1, category=None):
        # static
        self.opcode, self.name, self.length_of_operand = opcode, name, length_of_operand
        self.gas = gas
        self.description = description
        self.args = args or []  # number of arguments the instruction takes from stack
        self.returns = returns or []  # number of results returned (0 or 1)
        self.category = category  # instruction category

        # dynamic
        self.opcode_bytes = (self.opcode).to_bytes(1, byteorder="big")
        self.operand_bytes = b'\x00'*length_of_operand  # sane default
        self.operand = '\x00'*length_of_operand  # sane default
        self.annotations = []
        self.address = None
        self.next = None
        self.previous = None
        self.xrefs = set([])
        self.jumpto = None
        self.basicblock = None

    def clone(self):
        return Instruction(opcode=self.opcode,
                           name=self.name,
                           length_of_operand=self.length_of_operand,
                           description=self.description,
                           args=self.args, returns=self.returns,
                           gas=self.gas,
                           category=self.category)

    def __repr__(self):
        return "<%s name=%s address=%s size=%d %s>" % (self.__class__.__name__, self.name, hex(self.address), self.size(), "operand=%r" % self.operand if self.operand else "")

    def __str__(self):
        return "%s %s" % (self.name, "0x%s" % self.operand if self.operand else '')

    def size(self):
        return self.length_of_operand +1  # opcode + operand

    def consume(self, bytecode):
        # clone
        m = self.clone()
        # consume
        m.set_operand(bytes(_ for _ in itertools.islice(bytecode, m.length_of_operand)))
        return m

    def set_operand(self, b):
        self.operand_bytes = b
        self.operand = ''.join('%0.2x' % _ for _ in self.operand_bytes)
        return self

    def randomize_operand(self):
        self.set_operand(bytes(bytearray(random.getrandbits(8) for _ in range(self.length_of_operand))))
        return self

    def serialize(self):
        return ("%0.2x"%self.opcode)+utils.bytes_to_str(self.operand_bytes, prefix="")
        #return '%0.2x' % self.opcode + self.operand

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
            ascii = ' (%r)' % utils.hex_decode(self.operand_bytes) \
                if self.operand_bytes and utils.is_ascii_subsequence(self.operand_bytes) else ''
            str_operand = "0x%s%s" % (self.operand, ascii)
        else:
            ascii = ''
            str_operand = "0x%s%s" % (self.operand, ascii)

        extra = "@%s" % hex(self.jumpto) if self.jumpto else ''
        return "%s%s" % (str_operand, extra)

    def skip_to(self, names):
        res = self.next
        while res:
            if any(res.name==name for name in names):
                return res
            res = res.next
        return None