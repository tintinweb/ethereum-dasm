#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Author : <github.com/tintinweb>
'''
Verbose EthereumVM Disassembler

OPCODES taken from: 
    https://github.com/ethereum/go-ethereum/blob/master/core/vm/opcodes.go
    https://github.com/ethereum/yellowpaper/blob/master/Paper.tex
'''
import logging
import sys
import os
import itertools
import time

logger = logging.getLogger(__name__)

class Mnemonic(object):
    ''' Base mnemonic class
    '''
    def __init__(self, opcode, name, length_of_operand=0, description=None):
        self.opcode, self.name, self.length_of_operand = opcode, name, length_of_operand
        self.operand = ''
        self.description = description
        self.position = None
    def __repr__(self):
        return "<%s name=%s size=%d>"%(self.__class__.__name__, self.name, self.size())
    def __str__(self):
        return "%s %s"%(self.name, "0x%s"%self.operand if self.operand else '')
    def size(self):
        return 1 + len(self.operand)/2 # opcode + operand
    def consume(self, bytecode):
        # clone
        m = Mnemonic(opcode=self.opcode,
                     name=self.name,
                     length_of_operand=self.length_of_operand,
                     description=self.description)
        # consume
        m.operand = ''.join('%0.2x'%_ for _ in itertools.islice(bytecode, m.length_of_operand))
        return m
            
OPCODES = [ # Stop and Arithmetic Operations
            Mnemonic(opcode=0x00, name='STOP', description="Halts execution."), 
            Mnemonic(opcode=0x01, name='ADD', description="Addition operation."), 
            Mnemonic(opcode=0x02, name='MUL', description="Multiplication operation."), 
            Mnemonic(opcode=0x03, name='SUB', description="Subtraction operation."), 
            Mnemonic(opcode=0x04, name='DIV', description="Integer division operation."), 
            Mnemonic(opcode=0x05, name='SDIV', description="Signed integer"), 
            Mnemonic(opcode=0x06, name='MOD', description="Modulo"), 
            Mnemonic(opcode=0x07, name='SMOD', description="Signed modulo"), 
            Mnemonic(opcode=0x08, name='ADDMOD', description="Modulo"), 
            Mnemonic(opcode=0x09, name='MULMOD', description="Modulo"), 
            Mnemonic(opcode=0x0a, name='EXP', description="Exponential operation."), 
            Mnemonic(opcode=0x0b, name='SIGNEXTEND', description="Extend length of two’s complement signed integer."), 
            # Comparison & Bitwise Logic Operations
            Mnemonic(opcode=0x10, name='LT', description="Lesser-than comparison"), 
            Mnemonic(opcode=0x11, name='GT', description="Greater-than comparison"), 
            Mnemonic(opcode=0x12, name='SLT', description="Signed less-than comparison"), 
            Mnemonic(opcode=0x13, name='SGT', description="Signed greater-than comparison"), 
            Mnemonic(opcode=0x14, name='EQ', description="Equality  comparison"), 
            Mnemonic(opcode=0x15, name='ISZERO', description="Simple not operator"), 
            Mnemonic(opcode=0x16, name='AND', description="Bitwise AND operation."), 
            Mnemonic(opcode=0x17, name='OR', description="Bitwise OR operation."), 
            Mnemonic(opcode=0x18, name='XOR', description="Bitwise XOR operation."), 
            Mnemonic(opcode=0x19, name='NOT', description="Bitwise NOT operation."), 
            Mnemonic(opcode=0x1a, name='BYTE', description="Retrieve single byte from word"), 
            # SHA3
            Mnemonic(opcode=0x20, name='SHA3', description="Compute Keccak-256 hash."), 
            # Environmental Information
            Mnemonic(opcode=0x30, name='ADDRESS', description="Get address of currently executing account."), 
            Mnemonic(opcode=0x31, name='BALANCE', description="Get balance of the given account."), 
            Mnemonic(opcode=0x32, name='ORIGIN', description="Get execution origination address."), 
            Mnemonic(opcode=0x33, name='CALLER', description="Get caller address.This is the address of the account that is directly responsible for this execution."), 
            Mnemonic(opcode=0x34, name='CALLVALUE', description="Get deposited value by the instruction/transaction responsible for this execution."), 
            Mnemonic(opcode=0x35, name='CALLDATALOAD', description="Get input data of current environment."), 
            Mnemonic(opcode=0x36, name='CALLDATASIZE', description="Get size of input data in current environment."), 
            Mnemonic(opcode=0x37, name='CALLDATACOPY', description="Copy input data in current environment to memory. This pertains to the input data passed with the message call instruction or transaction."), 
            Mnemonic(opcode=0x38, name='CODESIZE', description="Get size of code running in current environment."), 
            Mnemonic(opcode=0x39, name='CODECOPY', description="Copy code running in current environment to memory."), 
            Mnemonic(opcode=0x3a, name='GASPRICE', description="Get price of gas in current environment."), 
            Mnemonic(opcode=0x3b, name='EXTCODESIZE', description="Get size of an account’s code."), 
            Mnemonic(opcode=0x3c, name='EXTCODECOPY', description="Copy an account’s code to memory."), 
            # Block Information
            Mnemonic(opcode=0x40, name='BLOCKHASH', description="Get the hash of one of the 256 most recent complete blocks."), 
            Mnemonic(opcode=0x41, name='COINBASE', description="Get the block’s beneficiary address."), 
            Mnemonic(opcode=0x42, name='TIMESTAMP', description="Get the block’s timestamp."), 
            Mnemonic(opcode=0x43, name='NUMBER', description="Get the block’s number."), 
            Mnemonic(opcode=0x44, name='DIFFICULTY', description="Get the block’s difficulty."), 
            Mnemonic(opcode=0x45, name='GASLIMIT', description="Get the block’s gas limit."), 
            # Stack, Memory, Storage and Flow Operations
            Mnemonic(opcode=0x50, name='POP', description="Remove item from stack."), 
            Mnemonic(opcode=0x51, name='MLOAD', description="Load word from memory."), 
            Mnemonic(opcode=0x52, name='MSTORE', description="Save word to memory."), 
            Mnemonic(opcode=0x53, name='MSTORE8', length_of_operand=0x8, description="Save byte to memory."), 
            Mnemonic(opcode=0x54, name='SLOAD', description="Load word from storage."), 
            Mnemonic(opcode=0x55, name='SSTORE', description="Save word to storage."), 
            Mnemonic(opcode=0x56, name='JUMP', description="Alter the program counter."), 
            Mnemonic(opcode=0x57, name='JUMPI', description="Conditionally alter the program counter."), 
            Mnemonic(opcode=0x58, name='PC', description="Get the value of the program counter prior to the increment."), 
            Mnemonic(opcode=0x59, name='MSIZE', description="Get the size of active memory in bytes."), 
            Mnemonic(opcode=0x5a, name='GAS', description="Get the amount of available gas, including the corresponding reduction"), 
            Mnemonic(opcode=0x5b, name='JUMPDEST', description="Mark a valid destination for jumps."), 
            # Stack Push Operations
            Mnemonic(opcode=0x60, name='PUSH1', length_of_operand=0x1, description="Place 1 byte item on stack."), 
            Mnemonic(opcode=0x61, name='PUSH2', length_of_operand=0x2, description="Place 2-byte item on stack."), 
            Mnemonic(opcode=0x62, name='PUSH3', length_of_operand=0x3, description="Place 3-byte item on stack."), 
            Mnemonic(opcode=0x63, name='PUSH4', length_of_operand=0x4, description="Place 4-byte item on stack."), 
            Mnemonic(opcode=0x64, name='PUSH5', length_of_operand=0x5, description="Place 5-byte item on stack."), 
            Mnemonic(opcode=0x65, name='PUSH6', length_of_operand=0x6, description="Place 6-byte item on stack."), 
            Mnemonic(opcode=0x66, name='PUSH7', length_of_operand=0x7, description="Place 7-byte item on stack."), 
            Mnemonic(opcode=0x67, name='PUSH8', length_of_operand=0x8, description="Place 8-byte item on stack."), 
            Mnemonic(opcode=0x68, name='PUSH9', length_of_operand=0x9, description="Place 9-byte item on stack."), 
            Mnemonic(opcode=0x69, name='PUSH10', length_of_operand=0xa, description="Place 10-byte item on stack."), 
            Mnemonic(opcode=0x6a, name='PUSH11', length_of_operand=0xb, description="Place 11-byte item on stack."), 
            Mnemonic(opcode=0x6b, name='PUSH12', length_of_operand=0xc, description="Place 12-byte item on stack."), 
            Mnemonic(opcode=0x6c, name='PUSH13', length_of_operand=0xd, description="Place 13-byte item on stack."), 
            Mnemonic(opcode=0x6d, name='PUSH14', length_of_operand=0xe, description="Place 14-byte item on stack."), 
            Mnemonic(opcode=0x6e, name='PUSH15', length_of_operand=0xf, description="Place 15-byte item on stack."), 
            Mnemonic(opcode=0x6f, name='PUSH16', length_of_operand=0x10, description="Place 16-byte item on stack."), 
            Mnemonic(opcode=0x70, name='PUSH17', length_of_operand=0x11, description="Place 17-byte item on stack."), 
            Mnemonic(opcode=0x71, name='PUSH18', length_of_operand=0x12, description="Place 18-byte item on stack."), 
            Mnemonic(opcode=0x72, name='PUSH19', length_of_operand=0x13, description="Place 19-byte item on stack."), 
            Mnemonic(opcode=0x73, name='PUSH20', length_of_operand=0x14, description="Place 20-byte item on stack."), 
            Mnemonic(opcode=0x74, name='PUSH21', length_of_operand=0x15, description="Place 21-byte item on stack."), 
            Mnemonic(opcode=0x75, name='PUSH22', length_of_operand=0x16, description="Place 22-byte item on stack."), 
            Mnemonic(opcode=0x76, name='PUSH23', length_of_operand=0x17, description="Place 23-byte item on stack."), 
            Mnemonic(opcode=0x77, name='PUSH24', length_of_operand=0x18, description="Place 24-byte item on stack."), 
            Mnemonic(opcode=0x78, name='PUSH25', length_of_operand=0x19, description="Place 25-byte item on stack."), 
            Mnemonic(opcode=0x79, name='PUSH26', length_of_operand=0x1a, description="Place 26-byte item on stack."), 
            Mnemonic(opcode=0x7a, name='PUSH27', length_of_operand=0x1b, description="Place 27-byte item on stack."), 
            Mnemonic(opcode=0x7b, name='PUSH28', length_of_operand=0x1c, description="Place 28-byte item on stack."), 
            Mnemonic(opcode=0x7c, name='PUSH29', length_of_operand=0x1d, description="Place 29-byte item on stack."), 
            Mnemonic(opcode=0x7d, name='PUSH30', length_of_operand=0x1e, description="Place 30-byte item on stack."), 
            Mnemonic(opcode=0x7e, name='PUSH31', length_of_operand=0x1f, description="Place 31-byte item on stack."), 
            Mnemonic(opcode=0x7f, name='PUSH32', length_of_operand=0x20, description="Place 32-byte (full word) item on stack."), 
            # Duplication Operations
            Mnemonic(opcode=0x80, name='DUP1', description="Duplicate 1st stack item."), 
            Mnemonic(opcode=0x81, name='DUP2', description="Duplicate 2nd stack item."), 
            Mnemonic(opcode=0x82, name='DUP3', description="Duplicate 3rd stack item."), 
            Mnemonic(opcode=0x83, name='DUP4', description="Duplicate 4th stack item."), 
            Mnemonic(opcode=0x84, name='DUP5', description="Duplicate 5th stack item."), 
            Mnemonic(opcode=0x85, name='DUP6', description="Duplicate 6th stack item."), 
            Mnemonic(opcode=0x86, name='DUP7', description="Duplicate 7th stack item."), 
            Mnemonic(opcode=0x87, name='DUP8', description="Duplicate 8th stack item."), 
            Mnemonic(opcode=0x88, name='DUP9', description="Duplicate 9th stack item."), 
            Mnemonic(opcode=0x89, name='DUP10', description="Duplicate 10th stack item."), 
            Mnemonic(opcode=0x8a, name='DUP11', description="Duplicate 11th stack item."), 
            Mnemonic(opcode=0x8b, name='DUP12', description="Duplicate 12th stack item."), 
            Mnemonic(opcode=0x8c, name='DUP13', description="Duplicate 13th stack item."), 
            Mnemonic(opcode=0x8d, name='DUP14', description="Duplicate 14th stack item."), 
            Mnemonic(opcode=0x8e, name='DUP15', description="Duplicate 15th stack item."), 
            Mnemonic(opcode=0x8f, name='DUP16', description="Duplicate 16th stack item."), 
            # Exchange Operations
            Mnemonic(opcode=0x90, name='SWAP1', description="Exchange 1st and 2nd stack items."), 
            Mnemonic(opcode=0x91, name='SWAP2', description="Exchange 1st and 3rd stack items."), 
            Mnemonic(opcode=0x92, name='SWAP3', description="Exchange 1st and 4th stack items."), 
            Mnemonic(opcode=0x93, name='SWAP4', description="Exchange 1st and 5th stack items."), 
            Mnemonic(opcode=0x94, name='SWAP5', description="Exchange 1st and 6th stack items."), 
            Mnemonic(opcode=0x95, name='SWAP6', description="Exchange 1st and 7th stack items."), 
            Mnemonic(opcode=0x96, name='SWAP7', description="Exchange 1st and 8th stack items."), 
            Mnemonic(opcode=0x97, name='SWAP8', description="Exchange 1st and 9th stack items."), 
            Mnemonic(opcode=0x98, name='SWAP9', description="Exchange 1st and 10th stack items."), 
            Mnemonic(opcode=0x99, name='SWAP10', description="Exchange 1st and 11th stack items."), 
            Mnemonic(opcode=0x9a, name='SWAP11', description="Exchange 1st and 12th stack items."), 
            Mnemonic(opcode=0x9b, name='SWAP12', description="Exchange 1st and 13th stack items."), 
            Mnemonic(opcode=0x9c, name='SWAP13', description="Exchange 1st and 14th stack items."), 
            Mnemonic(opcode=0x9d, name='SWAP14', description="Exchange 1st and 15th stack items."), 
            Mnemonic(opcode=0x9e, name='SWAP15', description="Exchange 1st and 16th stack items."), 
            Mnemonic(opcode=0x9f, name='SWAP16', description="Exchange 1st and 17th stack items."), 
            # Logging Operations
            Mnemonic(opcode=0xa0, name='LOG0', length_of_operand=0x0, description="Append log record with no topics."), 
            Mnemonic(opcode=0xa1, name='LOG1', length_of_operand=0x1, description="Append log record with one topic."), 
            Mnemonic(opcode=0xa2, name='LOG2', length_of_operand=0x2, description="Append log record with two topics."), 
            Mnemonic(opcode=0xa3, name='LOG3', length_of_operand=0x3, description="Append log record with three topics."), 
            Mnemonic(opcode=0xa4, name='LOG4', length_of_operand=0x4, description="Append log record with four topics."), 
            # System Operations
            Mnemonic(opcode=0xf0, name='CREATE', description="Create a new account with associated code."), 
            Mnemonic(opcode=0xf1, name='CALL', description="Message-call into an account."), 
            Mnemonic(opcode=0xf2, name='CALLCODE', description="Message-call into this account with alternative account’s code."), 
            Mnemonic(opcode=0xf3, name='RETURN', description="Halt execution returning output data."), 
            # Halt Execution, Mark for deletion
            Mnemonic(opcode=0xff, name='SUICIDE', description="Halt execution and register account for later deletion."), ]

class EVMAnalyzer(object):
    OPCODE_TABLE = dict((obj.opcode, obj) for obj in OPCODES)
    
    def __init__(self):
        self.errors = []
    
    def disassemble(self, bytecode):
        def iterbytes(bytecode):
            
            iter_bytecode = (b for b in bytecode if b in '1234567890abcdefABCDEFx') #0x will bail below.
            for b in itertools.izip(iter_bytecode,iter_bytecode):
                b = ''.join(b)
                try:
                    yield int(b,16)
                except ValueError, ve:
                    logger.warning("skipping invalid byte: %s"%repr(b))
                    
        pos = 0
        iter_bytecode = iterbytes(bytecode)
        # disassemble
        for opcode in iter_bytecode:
            logger.debug(opcode)
            try:
                mnemonic = self.OPCODE_TABLE[opcode].consume(iter_bytecode)
            except KeyError,ke:
                msg = "error: byte at position %d (%s) is not a valid operator"%(pos,hex(opcode))
                logger.exception(msg)
                mnemonic = Mnemonic(opcode=opcode, 
                                    name="UNKNOWN_%s"%hex(opcode), 
                                    description="%s; %r"%(msg,ke))
                self.errors.append("%s; %r"%(msg,ke))
            mnemonic.position = pos
            pos += mnemonic.size() 
            yield mnemonic

def main():
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s")
    from optparse import OptionParser
    usage = """usage: %prog [options]
    
       example: %prog [-L -v] <file_or_bytecode>
                %prog [-L -v] # read from stdin
    """
    parser = OptionParser(usage=usage)
    loglevels = ['CRITICAL', 'FATAL', 'ERROR', 'WARNING', 'WARN', 'INFO', 'DEBUG', 'NOTSET']
    parser.add_option("-v", "--verbosity", default="notset", 
                      help="available loglevels: %s [default: %%default]"%','.join(l.lower() for l in loglevels))
    parser.add_option("-L", "--listing", action="store_true", dest="listing", 
                      help="disables table mode, outputs assembly only")
    # parse args
    (options, args) = parser.parse_args()
    
    if options.verbosity.upper() in loglevels:
        logger.setLevel(getattr(logging,options.verbosity.upper()))
    else:
        parser.error("invalid verbosity selected. please check --help")
        
    # get bytecode from stdin, or arg:file or arg:bytcode
    if not args:
        evmcode = sys.stdin.read()
    else:
        if os.path.isfile(args[0]):
            evmcode = open(args[0],'r').read()
        else:
            evmcode = args[0]
    
    # init analyzer
    evm_dasm = EVMAnalyzer()
    logger.debug(EVMAnalyzer.OPCODE_TABLE)
    
    t_start = time.time()
    # print dissasembly
    if options.listing:
        for i,nm in enumerate(evm_dasm.disassemble(evmcode)):
            print "%s %s"%(nm.name, nm.operand)
    else:
        print " %6s %6s %-15s %-66s %s"%("Instr.#", "pos.", "mnemonic", "operand", "description")
        print "-"*120
        for i,nm in enumerate(evm_dasm.disassemble(evmcode)):
            print "[%6d] %6d %-15s %-66s # %s"%(i, nm.position,
                                                nm.name, 
                                                "0x%s"%nm.operand if nm.operand else '',
                                                nm.description)
            
    logger.info("finished in %0.3f seconds."%(time.time()-t_start))
    # post a notification that disassembly might be incorrect due to errors
    if evm_dasm.errors:
        logger.warning("disassembly finished with %d errors"%len(evm_dasm.errors))
        
    
    sys.exit(len(evm_dasm.errors))
    
if __name__=="__main__":
    main()