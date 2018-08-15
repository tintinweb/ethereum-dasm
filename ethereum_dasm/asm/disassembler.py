#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>
import logging
from .registry import *
import ethereum_dasm.utils as utils

logger = logging.getLogger(__name__)


class EVMDisAssembler(object):

    def __init__(self, debug=False):
        self.errors = []
        self.debug = debug

    def disassemble(self, bytecode):
        """ Disassemble evm bytecode to a Instruction objects """

        """
        def iterbytes(bytecode):
            iter_bytecode = (b for b in bytecode if b in '1234567890abcdefABCDEFx')
            for b in zip(iter_bytecode, iter_bytecode):
                b = ''.join(b)
                try:
                    yield int(b, 16)
                except ValueError:
                    logger.warning("skipping invalid byte: %s" % repr(b))

        def iterbytes_(bytecode):
            for b in bytecode:
                yield b
        """

        pc = 0
        previous = None

        if bytecode.startswith("0x"):
            bytecode = bytecode[2:]

        # iter_bytecode = iterbytes(bytecode)
        iter_bytecode = iter(utils.str_to_bytes(bytecode))

        # disassemble
        seen_stop = False
        for opcode in iter_bytecode:
            logger.debug(opcode)
            try:
                instruction = INSTRUCTIONS_BY_OPCODE[opcode].consume(iter_bytecode)
                if not len(instruction.operand_bytes)==instruction.length_of_operand:
                    logger.error("invalid instruction: %s" % instruction.name)
                    instruction.name = "INVALID_%s" % hex(opcode)
                    instruction.description = "Invalid operand"
                    instruction.category = "unknown"

            except KeyError as ke:
                instruction = Instruction(opcode=opcode,
                                          name="UNKNOWN_%s" % hex(opcode),
                                          description="Invalid opcode",
                                          category="unknown")

                if not seen_stop:
                    msg = "error: byte at address %d (%s) is not a valid operator" % (pc, hex(opcode))
                    if self.debug:
                        logger.exception(msg)
                    self.errors.append("%s; %r" % (msg, ke))
            if instruction.name == 'STOP' and not seen_stop:
                seen_stop = True


            instruction.address = pc
            pc += instruction.size()
            # doubly link
            instruction.previous = previous
            if previous:
                previous.next = instruction

            # current is previous
            previous = instruction

            #print("%s: %s %s" % (hex(instruction.address), instruction.name, instruction.operand))
            yield instruction

    def assemble(self, instructions):
        """ Assemble a list of Instruction() objects to evm bytecode"""
        for instruction in instructions:
            yield instruction.serialize()
