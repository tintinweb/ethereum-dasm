#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

from .instructions import Instruction

INSTRUCTIONS = [
    # Stop and Arithmetic Operations
    Instruction(opcode=0x00, name='STOP', category="terminate", gas=0, description="Halts execution."),
    Instruction(opcode=0x01, name='ADD', category="arithmetic", gas=3, description="Addition operation.", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x02, name='MUL', category="arithmetic", gas=5, description="Multiplication operation.", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x03, name='SUB', category="arithmetic", gas=3, description="Subtraction operation.", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x04, name='DIV', category="arithmetic", gas=5, description="Integer division operation.", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x05, name='SDIV', category="arithmetic", gas=5, description="Signed integer", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x06, name='MOD', category="arithmetic", gas=5, description="Modulo", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x07, name='SMOD', category="arithmetic", gas=5, description="Signed modulo", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x08, name='ADDMOD', category="arithmetic", gas=8, description="Modulo addition operation", args=['a', 'b', 'mod'], returns=['result']),
    Instruction(opcode=0x09, name='MULMOD', category="arithmetic", gas=8, description="Modulo multiplication operation", args=['a', 'b', 'mod'], returns=['result']),
    Instruction(opcode=0x0a, name='EXP', category="arithmetic", gas=10, description="Exponential operation.", args=['base', 'exponent'], returns=['result']),
    Instruction(opcode=0x0b, name='SIGNEXTEND', category="arithmetic", gas=5, description="Extend length of two's complement signed integer.", args=['bits', 'num'], returns=['result']),

    # Comparison & Bitwise Logic Operations
    Instruction(opcode=0x10, name='LT', category="comparison", gas=3, description="Lesser-than comparison", args=['a', 'b'], returns=['flag']),
    Instruction(opcode=0x11, name='GT', category="comparison", gas=3, description="Greater-than comparison", args=['a', 'b'], returns=['flag']),
    Instruction(opcode=0x12, name='SLT', category="comparison", gas=3, description="Signed less-than comparison", args=['a', 'b'], returns=['flag']),
    Instruction(opcode=0x13, name='SGT', category="comparison", gas=3, description="Signed greater-than comparison", args=['a', 'b'], returns=['flag']),
    Instruction(opcode=0x14, name='EQ', category="comparison", gas=3, description="Equality  comparison", args=['a', 'b'], returns=['flag']),
    Instruction(opcode=0x15, name='ISZERO', category="comparison",  gas=3, description="Simple not operator", args=['a'], returns=['flag']),
    Instruction(opcode=0x16, name='AND', category="bitwise-logic",  gas=3, description="Bitwise AND operation.", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x17, name='OR', category="bitwise-logic",gas=3, description="Bitwise OR operation.", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x18, name='XOR', category="bitwise-logic",gas=3, description="Bitwise XOR operation.", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x19, name='NOT', category="bitwise-logic",gas=3, description="Bitwise NOT operation.", args=['a', 'b'], returns=['result']),
    Instruction(opcode=0x1a, name='BYTE', category="bitwise-logic",gas=3, description="Retrieve single byte from word", args=['th', 'val'], returns=['result']),
    Instruction(opcode=0x1b, name='SHL', category="bitwise-logic", gas=3, description="<TBD> Shift left", args=['shift', 'value'], returns=['result']),
    Instruction(opcode=0x1c, name='SHR', category="bitwise-logic", gas=3, description="<TBD> Shift Right", args=['shift', 'value'], returns=['result']),
    Instruction(opcode=0x1d, name='SAR', category="bitwise-logic", gas=3, description="<TBD> Shift arithmetic right", args=['shift', 'value'], returns=['flag']),

    # SHA3
    Instruction(opcode=0x20, name='SHA3', category="cryptographic", gas=30, description="Compute Keccak-256 hash.", args=['offset', 'size'], returns=['sha3']),

    # Environmental Information
    Instruction(opcode=0x30, name='ADDRESS', category="envinfo", gas=2, description="Get address of currently executing account.", returns=['this.address']),
    Instruction(opcode=0x31, name='BALANCE', category="envinfo", gas=20, description="Get balance of the given account.", args=["slot"], returns=["this.balance"]),
    Instruction(opcode=0x32, name='ORIGIN', category="envinfo", gas=2, description="Get execution origination address.", returns=["tx.origin"]),
    Instruction(opcode=0x33, name='CALLER', category="envinfo", gas=2, description="Get caller address.This is the address of the account that is directly responsible for this execution.", returns=["msg.sender"]),
    Instruction(opcode=0x34, name='CALLVALUE', category="envinfo", gas=2, description="Get deposited value by the instruction/transaction responsible for this execution.", returns=["msg.value"]),
    Instruction(opcode=0x35, name='CALLDATALOAD', category="envinfo", gas=3, description="Get input data of current environment.", args=['dataOffset'], returns=["msg.data"]),
    Instruction(opcode=0x36, name='CALLDATASIZE', category="envinfo", gas=2, description="Get size of input data in current environment.", returns=["msg.data.length"]),
    Instruction(opcode=0x37, name='CALLDATACOPY', category="envinfo", gas=3, description="Copy input data in current environment to memory. This pertains to the input data passed with the message call instruction or transaction.", args=["memOffset", "dataOffset", "length"]),
    Instruction(opcode=0x38, name='CODESIZE', category="envinfo", gas=2, description="Get size of code running in current environment.", returns=["codesize"]),
    Instruction(opcode=0x39, name='CODECOPY', category="envinfo", gas=3, description="Copy code running in current environment to memory.", args=["memOffset", "codeOffset", "length"]),
    Instruction(opcode=0x3a, name='GASPRICE', category="envinfo", gas=2, description="Get price of gas in current environment.", returns=["tx.gasprice"]),
    Instruction(opcode=0x3b, name='EXTCODESIZE', category="envinfo", gas=20, description="Get size of an account's code.", args=['slot'], returns=["extcodesize"]),
    Instruction(opcode=0x3c, name='EXTCODECOPY', category="envinfo", gas=20, description="Copy an account's code to memory.", args=["address", "memOffset", "codeOffset", "length"]),
    Instruction(opcode=0x3d, name='RETURNDATASIZE', category="envinfo", gas=2, description="Push the size of the return data buffer onto the stack.", returns=["returndatasize"]),
    Instruction(opcode=0x3e, name='RETURNDATACOPY', category="envinfo", gas=3, description="Copy data from the return data buffer.", args=["memOffset", "dataOffset", "length"]),
    Instruction(opcode=0x3f, name='EXTCODEHASH', category="envinfo", gas=400, description="<TBD> - Constantinople", args=["slot"]),


    # Block Information
    Instruction(opcode=0x40, name='BLOCKHASH', category="blockinfo", gas=20, description="Get the hash of one of the 256 most recent complete blocks.", args=["num"], returns=["block.blockhash"]),
    Instruction(opcode=0x41, name='COINBASE', category="blockinfo", gas=2, description="Get the block's beneficiary address.", returns=["block.coinbase"]),
    Instruction(opcode=0x42, name='TIMESTAMP', category="blockinfo", gas=2, description="Get the block's timestamp.", returns=["block.timestamp"]),
    Instruction(opcode=0x43, name='NUMBER', category="blockinfo", gas=2, description="Get the block's number.", returns=["block.number"]),
    Instruction(opcode=0x44, name='DIFFICULTY', category="blockinfo", gas=2, description="Get the block's difficulty.", returns=["block.difficulty"]),
    Instruction(opcode=0x45, name='GASLIMIT', category="blockinfo", gas=2, description="Get the block's gas limit.", returns=["block.gaslimit"]),

    # Stack, Memory, Storage and Flow Operations
    Instruction(opcode=0x50, name='POP', category="stack", gas=2, description="Remove item from stack.", args=["#dummy"], ),
    # dummy is only there to indicate that there is a pop()
    Instruction(opcode=0x51, name='MLOAD', category="memory", gas=3, description="Load word from memory.", args=["offset"]),
    Instruction(opcode=0x52, name='MSTORE', category="memory", gas=3, description="Save word to memory.", args=["offset","value"]),
    Instruction(opcode=0x53, name='MSTORE8', category="memory", gas=3, length_of_operand=0x8, description="Save byte to memory.", args=["offset","value"]),
    Instruction(opcode=0x54, name='SLOAD', category="storage", gas=50, description="Load word from storage.", args=["loc"], returns=["result"]),
    Instruction(opcode=0x55, name='SSTORE', category="storage", gas=0, description="Save word to storage.", args=["loc", "value"]),
    Instruction(opcode=0x56, name='JUMP', category="controlflow", gas=8, description="Alter the program counter.", args=["evm.pc"]),
    Instruction(opcode=0x57, name='JUMPI', category="controlflow", gas=10, description="Conditionally alter the program counter.", args=["evm.pc", "condition"]),
    Instruction(opcode=0x58, name='PC', category="info", gas=2, description="Get the value of the program counter prior to the increment.", returns=["evm.pc"]),
    Instruction(opcode=0x59, name='MSIZE', category="memory", gas=2, description="Get the size of active memory in bytes.", returns=["memory.length"]),
    Instruction(opcode=0x5a, name='GAS', category="info", gas=2, description="Get the amount of available gas, including the corresponding reduction", returns=["gasleft"]),
    Instruction(opcode=0x5b, name='JUMPDEST', category="label", gas=1, description="Mark a valid destination for jumps."),

    # Stack Push Operations
    Instruction(opcode=0x60, name='PUSH1', category="stack", gas=3, length_of_operand=0x1, description="Place 1 byte item on stack.", returns=["item"]),
    Instruction(opcode=0x61, name='PUSH2', category="stack", gas=3, length_of_operand=0x2, description="Place 2-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x62, name='PUSH3', category="stack",  gas=3, length_of_operand=0x3, description="Place 3-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x63, name='PUSH4', category="stack", gas=3, length_of_operand=0x4, description="Place 4-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x64, name='PUSH5', category="stack", gas=3, length_of_operand=0x5, description="Place 5-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x65, name='PUSH6', category="stack", gas=3, length_of_operand=0x6, description="Place 6-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x66, name='PUSH7', category="stack", gas=3, length_of_operand=0x7, description="Place 7-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x67, name='PUSH8', category="stack", gas=3, length_of_operand=0x8, description="Place 8-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x68, name='PUSH9', category="stack", gas=3, length_of_operand=0x9, description="Place 9-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x69, name='PUSH10', category="stack", gas=3, length_of_operand=0xa, description="Place 10-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x6a, name='PUSH11', category="stack", gas=3, length_of_operand=0xb, description="Place 11-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x6b, name='PUSH12', category="stack", gas=3, length_of_operand=0xc, description="Place 12-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x6c, name='PUSH13', category="stack", gas=3, length_of_operand=0xd, description="Place 13-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x6d, name='PUSH14', category="stack", gas=3, length_of_operand=0xe, description="Place 14-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x6e, name='PUSH15', category="stack", gas=3, length_of_operand=0xf, description="Place 15-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x6f, name='PUSH16', category="stack", gas=3, length_of_operand=0x10, description="Place 16-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x70, name='PUSH17', category="stack", gas=3, length_of_operand=0x11, description="Place 17-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x71, name='PUSH18', category="stack", gas=3, length_of_operand=0x12, description="Place 18-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x72, name='PUSH19', category="stack", gas=3, length_of_operand=0x13, description="Place 19-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x73, name='PUSH20', category="stack", gas=3, length_of_operand=0x14, description="Place 20-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x74, name='PUSH21', category="stack", gas=3, length_of_operand=0x15, description="Place 21-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x75, name='PUSH22', category="stack", gas=3, length_of_operand=0x16, description="Place 22-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x76, name='PUSH23', category="stack", gas=3, length_of_operand=0x17, description="Place 23-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x77, name='PUSH24', category="stack", gas=3, length_of_operand=0x18, description="Place 24-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x78, name='PUSH25', category="stack", gas=3, length_of_operand=0x19, description="Place 25-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x79, name='PUSH26', category="stack", gas=3, length_of_operand=0x1a, description="Place 26-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x7a, name='PUSH27', category="stack", gas=3, length_of_operand=0x1b, description="Place 27-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x7b, name='PUSH28', category="stack", gas=3, length_of_operand=0x1c, description="Place 28-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x7c, name='PUSH29', category="stack", gas=3, length_of_operand=0x1d, description="Place 29-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x7d, name='PUSH30', category="stack", gas=3, length_of_operand=0x1e, description="Place 30-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x7e, name='PUSH31', category="stack", gas=3, length_of_operand=0x1f, description="Place 31-byte item on stack.", returns=["item"]),
    Instruction(opcode=0x7f, name='PUSH32', category="stack", gas=3, length_of_operand=0x20, description="Place 32-byte (full word) item on stack."),

    # Duplication Operations
    Instruction(opcode=0x80, name='DUP1', category="stack", gas=3, description="Duplicate 1st stack item."),
    Instruction(opcode=0x81, name='DUP2', category="stack", gas=3, description="Duplicate 2nd stack item."),
    Instruction(opcode=0x82, name='DUP3', category="stack", gas=3, description="Duplicate 3rd stack item."),
    Instruction(opcode=0x83, name='DUP4', category="stack", gas=3, description="Duplicate 4th stack item."),
    Instruction(opcode=0x84, name='DUP5', category="stack", gas=3, description="Duplicate 5th stack item."),
    Instruction(opcode=0x85, name='DUP6', category="stack", gas=3, description="Duplicate 6th stack item."),
    Instruction(opcode=0x86, name='DUP7', category="stack", gas=3, description="Duplicate 7th stack item."),
    Instruction(opcode=0x87, name='DUP8', category="stack", gas=3, description="Duplicate 8th stack item."),
    Instruction(opcode=0x88, name='DUP9', category="stack", gas=3, description="Duplicate 9th stack item."),
    Instruction(opcode=0x89, name='DUP10', category="stack", gas=3, description="Duplicate 10th stack item."),
    Instruction(opcode=0x8a, name='DUP11', category="stack", gas=3, description="Duplicate 11th stack item."),
    Instruction(opcode=0x8b, name='DUP12', category="stack", gas=3, description="Duplicate 12th stack item."),
    Instruction(opcode=0x8c, name='DUP13', category="stack", gas=3, description="Duplicate 13th stack item."),
    Instruction(opcode=0x8d, name='DUP14', category="stack", gas=3, description="Duplicate 14th stack item."),
    Instruction(opcode=0x8e, name='DUP15', category="stack", gas=3, description="Duplicate 15th stack item."),
    Instruction(opcode=0x8f, name='DUP16', category="stack", gas=3, description="Duplicate 16th stack item."),

    # Exchange Operations
    Instruction(opcode=0x90, name='SWAP1', category="stack", gas=3, description="Exchange 1st and 2nd stack items."),
    Instruction(opcode=0x91, name='SWAP2', category="stack", gas=3, description="Exchange 1st and 3rd stack items."),
    Instruction(opcode=0x92, name='SWAP3', category="stack", gas=3, description="Exchange 1st and 4th stack items."),
    Instruction(opcode=0x93, name='SWAP4', category="stack", gas=3, description="Exchange 1st and 5th stack items."),
    Instruction(opcode=0x94, name='SWAP5', category="stack", gas=3, description="Exchange 1st and 6th stack items."),
    Instruction(opcode=0x95, name='SWAP6', category="stack", gas=3, description="Exchange 1st and 7th stack items."),
    Instruction(opcode=0x96, name='SWAP7', category="stack", gas=3, description="Exchange 1st and 8th stack items."),
    Instruction(opcode=0x97, name='SWAP8', category="stack", gas=3, description="Exchange 1st and 9th stack items."),
    Instruction(opcode=0x98, name='SWAP9', category="stack", gas=3, description="Exchange 1st and 10th stack items."),
    Instruction(opcode=0x99, name='SWAP10', category="stack", gas=3, description="Exchange 1st and 11th stack items."),
    Instruction(opcode=0x9a, name='SWAP11', category="stack", gas=3, description="Exchange 1st and 12th stack items."),
    Instruction(opcode=0x9b, name='SWAP12', category="stack", gas=3, description="Exchange 1st and 13th stack items."),
    Instruction(opcode=0x9c, name='SWAP13', category="stack", gas=3, description="Exchange 1st and 14th stack items."),
    Instruction(opcode=0x9d, name='SWAP14', category="stack", gas=3, description="Exchange 1st and 15th stack items."),
    Instruction(opcode=0x9e, name='SWAP15', category="stack", gas=3, description="Exchange 1st and 16th stack items."),
    Instruction(opcode=0x9f, name='SWAP16', category="stack", gas=3, description="Exchange 1st and 17th stack items."),

    # Logging Operations
    Instruction(opcode=0xa0, name='LOG0', category="event", gas=375, length_of_operand=0x0, description="Append log record with no topics.", args=["start", "size"]),
    Instruction(opcode=0xa1, name='LOG1', category="event", gas=750, length_of_operand=0x1, description="Append log record with one topic.", args=["start", "size", "topic1"]),
    Instruction(opcode=0xa2, name='LOG2', category="event", gas=1125, length_of_operand=0x2, description="Append log record with two topics.", args=["start", "size", "topic1", "topic2"]),
    Instruction(opcode=0xa3, name='LOG3', category="event", gas=1500, length_of_operand=0x3, description="Append log record with three topics.", args=["start", "size", "topic1", "topic2", "topic3"]),
    Instruction(opcode=0xa4, name='LOG4', category="event", gas=1875, length_of_operand=0x4, description="Append log record with four topics.", args=["start", "size", "topic1", "topic2", "topic3", "topic4"]),

    # unofficial opcodes used for parsing.
    Instruction(opcode=0xb0, name='UNOFFICIAL_PUSH', category="unofficial", description="unofficial opcodes used for parsing."),
    Instruction(opcode=0xb1, name='UNOFFICIAL_DUP', category="unofficial", description="unofficial opcodes used for parsing."),
    Instruction(opcode=0xb2, name='UNOFFICIAL_SWAP', category="unofficial", description="unofficial opcodes used for parsing."),

    # System Operations
    Instruction(opcode=0xf0, name='CREATE', category="system", gas=32000, description="Create a new account with associated code.", args=["value", "offset", "size"]),
    Instruction(opcode=0xf1, name='CALL', category="system", gas=40, description="Message-call into an account.", args=["gas", "address", "value", "inOffset", "inSize", "retOffset", "retSize"]),
    Instruction(opcode=0xf2, name='CALLCODE', category="system", gas=40, description="Message-call into this account with alternative account's code.", args=["gas", "address", "value", "inOffset", "inSize", "retOffset", "retSize"]),
    Instruction(opcode=0xf3, name='RETURN', category="terminate", gas=0, description="Halt execution returning output data.", args=["offset", "size"]),
    Instruction(opcode=0xf4, name='DELEGATECALL', category="system", gas=40, description="<TBD - fixme todo>", args=["gas", "address", "inOffset", "inSize", "retOffset", "retSize"]),
    Instruction(opcode=0xf5, name='CREATE2', category="system", gas=32000, description="<TBD> - Constantinople", args=["endowment", "offset", "size", "salt"]),

    # Newer opcode
    Instruction(opcode=0xfa, name='STATICCALL', category="system", gas=40, description='<TBD - fixme todo>', args=["gas", "address", "inOffset", "inSize", "retOffset", "retSize"]),
    Instruction(opcode=0xfd, name='REVERT', category="terminate", gas=0, description='throw an error', args=["offset", "size"]),

    # Halt Execution, Mark for deletion
    Instruction(opcode=0xff, name='SELFDESTRUCT', category="terminate", gas=0, description="Halt execution and register account for later deletion.", args=["address"]), ]

INSTRUCTIONS_BY_OPCODE = {obj.opcode: obj for obj in INSTRUCTIONS}
INSTRUCTIONS_BY_NAME = {obj.name: obj for obj in INSTRUCTIONS}
INSTRUCTIONS_BY_CATEGORY = {}
for instr in INSTRUCTIONS:
    INSTRUCTIONS_BY_CATEGORY.setdefault(instr.category, [])
    INSTRUCTIONS_BY_CATEGORY[instr.category].append(instr)

INSTRUCTION_MARKS_BASICBLOCK_END = ['JUMP', 'JUMPI', 'STOP', 'RETURN']


def create_instruction(name=None, opcode=None):
    assert(name is not None or opcode is not None)
    assert(not(name is None and opcode is None))

    if name is not None:
        instr = INSTRUCTIONS_BY_NAME.get(name)
    elif opcode is not None:
        instr = INSTRUCTIONS_BY_OPCODE.get(opcode)
        if not instr:
            instr = Instruction(opcode=opcode,
                                name="UNKNOWN_%s" % hex(opcode),
                                description="Invalid opcode",
                                category="unknown")
    else:
        raise Exception("name or opcode required")

    return instr.clone()
