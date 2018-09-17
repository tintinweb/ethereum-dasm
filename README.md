# ethereum-dasm 
ethereum evm bytecode disassembler with static- and dynamic-analysis and function signature lookup

[https://github.com/ethereum/] [https://www.ethereum.org/]

![windows](https://user-images.githubusercontent.com/2865694/42905736-28e71672-8ad9-11e8-9a2d-baa6f4260dbc.png)

**disassembles evm bytecode**

[![asciicast](https://asciinema.org/a/fbWad5tV9YmpCGB97wbI1al9w.png)](https://asciinema.org/a/fbWad5tV9YmpCGB97wbI1al9w)

## install

```
#> python3 -m pip install -r requirements*.txt
#> python3 -m pip install ethereum-dasm[mythril,abidecoder]
#> python3 -m ethereum-dasm  # verify installation
```

```
#> python3 -m ethereum_dasm -a 0x44919b8026f38d70437a8eb3be47b06ab1c3e4bf  # verify installation
```

## usage

```
#> evmdasm.py --help
Usage: evmdasm.py [options]

       example: evmdasm.py [-L -F -v] <file_or_bytecode>
                evmdasm.py [-L -F -v] # read from stdin
                evmdasm.py [-L -F -a <address>] # fetch contract code from infura.io


Options:
  -h, --help            show this help message and exit
  -v VERBOSITY, --verbosity=VERBOSITY
                        available loglevels:
                        critical,fatal,error,warning,warn,info,debug,notset
                        [default: critical]
  -L, --listing         disables table mode, outputs assembly only
  -F, --no-online-lookup
                        disable online function signature lookup
  -a ADDRESS, --address=ADDRESS
                        fetch contract bytecode from address
  -C, --no-color        disable color mode (requires pip install colorama)
  -A, --guess-abi       guess the ABI for that contract
  -D, --no-dynamic-analysis
                        disable dynamic analysis / symolic execution
  -S, --no-static-analysis
                        disable static analysis
```

    #> echo "0x12345678" | python evmdasm.py
    #> python evmdasm.py 0x12345678
    #> python evmdasm.py ether_contract.evm
    #> python evmdasm.py -a <contract address>
    #> python -m ethereum_dasm -a <contract address>  -A

## features

* provide the path to the ethereum vm bytecode or the bytecode as an argument to evmdasm. Tries to read from stdin by default.
* returns !=0 on errors
* various output modes (`-L` to switch from table to listing mode)
* color-mode
* invalid opcodes are prefixed with `UNKNOWN_`
* gas consumption for instruction
* return value and arguments for instruction
* basic jump/xref analysis
* basicblocking
* online function signature and method name lookup, operand annotations
* payable modifier detection
* dynamic analysis based on symbolic execution (depends on mythril)
* ABI.json download (from etherchain.org)
* ABI.json reconstruction from static analysis of the evm bytecode
* main interface `Contract()`.

## examples

**abi online lookup or reconstruction**
```#>python -m ethereum_dasm -a 0x44919b8026f38d70437a8eb3be47b06ab1c3e4bf  -A```
```python
# [....]
[{'stateMutability': 'nonpayable', 'constant': False, 'type': 'function', 'name': 'enter', 'signature': '0x124c32a1', 'outputs': [{'type': 'bool', 'name': ''}], 'inputs': [{'type': 'bytes32', 'name': '_passcode'
}, {'type': 'bytes8', 'name': '_gateKey'}], 'payable': False}, {'stateMutability': 'pure', 'constant': True, 'type': 'function', 'name': 'maxEntrants', 'signature': '0x60643652', 'outputs': [{'type': 'uint8', 'n
ame': ''}], 'inputs': [], 'payable': False}, {'stateMutability': 'view', 'constant': True, 'type': 'function', 'name': 'totalEntrants', 'signature': '0x694463a2', 'outputs': [{'type': 'uint8', 'name': ''}], 'inp
uts': [], 'payable': False}, {'stateMutability': 'nonpayable', 'constant': False, 'type': 'function', 'name': 'assignAll', 'signature': '0x90ae631d', 'outputs': [{'type': 'bool', 'name': ''}], 'inputs': [], 'pay
able': False}, {'inputs': [], 'stateMutability': 'nonpayable', 'payable': False, 'type': 'constructor'}]
```

**abi reconstruction from dasm if abi is not available**
`#> python -m ethereum_dasm -a 0x8f8bed23a644f3bbb4e227e28704c050e67c35be -A`
```
[{'signature': '0x95d89b41', 'outputs': [], 'stateMutability': None, 'name': 'symbol', 'constant': None, 'inputs': [], 'payable': True, 'type': 'function', 'address': 598}, {'signature': '0x095ea7b3', 'outputs':
 [], 'stateMutability': None, 'name': 'approve', 'constant': None, 'inputs': ['bytes32', '<bytes??>'], 'payable': True, 'type': 'function', 'address': 328}, {'signature': '0x313ce567', 'outputs': [], 'stateMutab
ility': None, 'name': 'decimals', 'constant': None, 'inputs': [], 'payable': True, 'type': 'function', 'address': 486}, {'signature': '0xdd62ed3e', 'outputs': [], 'stateMutability': None, 'name': 'allowance', 'c
onstant': None, 'inputs': ['bytes32', '<bytes??>'], 'payable': True, 'type': 'function', 'address': 691}, {'signature': '0x66188463', 'outputs': [], 'stateMutability': None, 'name': 'decreaseApproval', 'constant
': None, 'inputs': ['bytes32', '<bytes??>'], 'payable': True, 'type': 'function', 'address': 529}, {'signature': '0x23b872dd', 'outputs': [], 'stateMutability': None, 'name': 'transferFrom', 'constant': None, 'i
nputs': ['bytes32', 'bytes32', '<bytes??>'], 'payable': True, 'type': 'function', 'address': 423}, {'signature': '0x2ff2e9dc', 'outputs': [], 'stateMutability': None, 'name': 'INITIAL_SUPPLY', 'constant': None,
'inputs': [], 'payable': True, 'type': 'function', 'address': 465}, {'signature': '0x06fdde03', 'outputs': [], 'stateMutability': None, 'name': 'name', 'constant': None, 'inputs': [], 'payable': True, 'type': 'f
unction', 'address': 190}, {'signature': '0x18160ddd', 'outputs': [], 'stateMutability': None, 'name': 'totalSupply', 'constant': None, 'inputs': [], 'payable': True, 'type': 'function', 'address': 384}, {'signa
ture': '0x70a08231', 'outputs': [], 'stateMutability': None, 'name': 'balanceOf', 'constant': None, 'inputs': ['<bytes??>'], 'payable': True, 'type': 'function', 'address': 565}, {'signature': '0xa9059cbb', 'out
puts': [], 'stateMutability': None, 'name': 'transfer', 'constant': None, 'inputs': [{'type': 'address', 'name': 'arg0'}, {'type': 'uint256', 'name': 'arg1'}], 'payable': True, 'type': 'function', 'address': 619
}, {'signature': '0xd73dd623', 'outputs': [], 'stateMutability': None, 'name': 'increaseApproval', 'constant': None, 'inputs': ['bytes32', '<bytes??>'], 'payable': True, 'type': 'function', 'address': 655}]
```


**detailed listing**

```python -m ethereum_dasm -a 0x44919b8026f38d70437a8eb3be47b06ab1c3e4bf  -A --no-color ```
```python
  Inst   addr  hex    gas | mnemonic        operand                                               xrefs        description                                                           retval           args
------------------------------------------------------------------------------------------------  -----------  --------------------------------------------------------------------  ---------------  --------------------
:loc_0x0
     0 [   0 0x0000 ]   3 | PUSH1           0x60                                                               # Place 1 byte item on stack.                                         item
     1 [   2 0x0002 ]   3 | PUSH1           0x40                                                               # Place 1 byte item on stack.                                         item
     2 [   4 0x0004 ]   3 | MSTORE                                                                             # Save word to memory.                                                                 value, offset
     3 [   5 0x0005 ]   3 | PUSH1           0x04                                                               # Place 1 byte item on stack.                                         item
     4 [   7 0x0007 ]   2 | CALLDATASIZE                                                                       # Get size of input data in current environment.                      msg.data.length
     5 [   8 0x0008 ]   3 | LT                                                                                 # Lesser-than comparison                                              flag             a, b
     6 [   9 0x0009 ]   3 | PUSH2           0x0048                                                             # Place 2-byte item on stack.                                         item
     7 [  12 0x000c ]  10 | JUMPI           @0x48                                                              # Conditionally alter the program counter.                                             evm.pc, condition
     8 [  13 0x000d ]   3 | PUSH4           0xffffffff                                                         # Place 4-byte item on stack.                                         item
     9 [  18 0x0012 ]   3 | PUSH1           0xe0                                                               # Place 1 byte item on stack.                                         item
    10 [  20 0x0014 ]   3 | PUSH1           0x02                                                               # Place 1 byte item on stack.                                         item
    11 [  22 0x0016 ]  10 | EXP                                                                                # Exponential operation.                                              result           base, exponent
    12 [  23 0x0017 ]   3 | PUSH1           0x00                                                               # Place 1 byte item on stack.                                         item
    13 [  25 0x0019 ]   3 | CALLDATALOAD                                                                       # Get input data of current environment.                              msg.data         unknown
    14 [  26 0x001a ]   5 | DIV                                                                                # Integer division operation.                                         result           a, b
    15 [  27 0x001b ]   3 | AND                                                                                # Bitwise AND operation.                                              result           a, b
    16 [  28 0x001c ]   3 | PUSH4           0x124c32a1  --> 'function enter(bytes32,bytes8)'                   # Place 4-byte item on stack.                                         item
    17 [  33 0x0021 ]   3 | DUP2                                                                               # Duplicate 2nd stack item.
    18 [  34 0x0022 ]   3 | EQ                                                                                 # Equality  comparison                                                flag             a, b
    19 [  35 0x0023 ]   3 | PUSH2           0x004d                                                             # Place 2-byte item on stack.                                         item
    20 [  38 0x0026 ]  10 | JUMPI           @0x4d                                                              # Conditionally alter the program counter.                                             evm.pc, condition
    21 [  39 0x0027 ]   3 | DUP1                                                                               # Duplicate 1st stack item.
    22 [  40 0x0028 ]   3 | PUSH4           0x60643652  --> 'function maxEntrants()'                           # Place 4-byte item on stack.                                         item
    23 [  45 0x002d ]   3 | EQ                                                                                 # Equality  comparison                                                flag             a, b
    24 [  46 0x002e ]   3 | PUSH2           0x0095                                                             # Place 2-byte item on stack.                                         item
    25 [  49 0x0031 ]  10 | JUMPI           @0x95                                                              # Conditionally alter the program counter.                                             evm.pc, condition
    26 [  50 0x0032 ]   3 | DUP1                                                                               # Duplicate 1st stack item.
    27 [  51 0x0033 ]   3 | PUSH4           0x694463a2  --> 'function totalEntrants()'                         # Place 4-byte item on stack.                                         item
    28 [  56 0x0038 ]   3 | EQ                                                                                 # Equality  comparison                                                flag             a, b
    29 [  57 0x0039 ]   3 | PUSH2           0x00be                                                             # Place 2-byte item on stack.                                         item
    30 [  60 0x003c ]  10 | JUMPI           @0xbe                                                              # Conditionally alter the program counter.                                             evm.pc, condition
    31 [  61 0x003d ]   3 | DUP1                                                                               # Duplicate 1st stack item.
    32 [  62 0x003e ]   3 | PUSH4           0x90ae631d  --> 'function assignAll()'                             # Place 4-byte item on stack.                                         item
    33 [  67 0x0043 ]   3 | EQ                                                                                 # Equality  comparison                                                flag             a, b
    34 [  68 0x0044 ]   3 | PUSH2           0x00d1                                                             # Place 2-byte item on stack.                                         item
    35 [  71 0x0047 ]  10 | JUMPI           @0xd1                                                              # Conditionally alter the program counter.                                             evm.pc, condition

:loc_0x48
    36 [  72 0x0048 ]   1 | JUMPDEST                                                              JUMPI@0xc    # Mark a valid destination for jumps.
    37 [  73 0x0049 ]   3 | PUSH1           0x00                                                               # Place 1 byte item on stack.                                         item
    38 [  75 0x004b ]   3 | DUP1                                                                               # Duplicate 1st stack item.
    39 [  76 0x004c ]   0 | REVERT                                                                             # throw an error                                                                       offset, size
:loc_0x4d
  /*******************************************************************
    function enter(bytes32,bytes8)
    payable: False
    inputs: (2) ['bytes32', '<bytes??>']
    potential signatures: ['enter(bytes32,bytes8)']
  *******************************************************************/
    40 [  77 0x004d ]   1 | JUMPDEST                                                              JUMPI@0x26   # Mark a valid destination for jumps.
    41 [  78 0x004e ]   2 | CALLVALUE                                                                          # Get deposited value by the instruction/transaction responsible for  msg.value
                                                                                                                 this execution.
    42 [  79 0x004f ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
    43 [  80 0x0050 ]   3 | PUSH2           0x0058                                                             # Place 2-byte item on stack.                                         item
    44 [  83 0x0053 ]  10 | JUMPI           @0x58                                                              # Conditionally alter the program counter.                                             evm.pc, condition
    45 [  84 0x0054 ]   3 | PUSH1           0x00                                                               # Place 1 byte item on stack.                                         item
    46 [  86 0x0056 ]   3 | DUP1                                                                               # Duplicate 1st stack item.
    47 [  87 0x0057 ]   0 | REVERT                                                                             # throw an error                                                                       offset, size
:loc_0x58
    48 [  88 0x0058 ]   1 | JUMPDEST                                                              JUMPI@0x53   # Mark a valid destination for jumps.
    49 [  89 0x0059 ]   3 | PUSH2           0x0081                                                             # Place 2-byte item on stack.                                         item
    50 [  92 0x005c ]   3 | PUSH1           0x04                                                               # Place 1 byte item on stack.                                         item
    51 [  94 0x005e ]   3 | CALLDATALOAD                                                                       # Get input data of current environment.                              msg.data         unknown
    52 [  95 0x005f ]   3 | PUSH24          0xffffffffffffffffffffffffffffffffffffffffffffffff                 # Place 24-byte item on stack.                                        item
    53 [ 120 0x0078 ]   3 | NOT                                                                                # Bitwise NOT operation.                                              result           a, b
    54 [ 121 0x0079 ]   3 | PUSH1           0x24                                                               # Place 1 byte item on stack.                                         item
    55 [ 123 0x007b ]   3 | CALLDATALOAD                                                                       # Get input data of current environment.                              msg.data         unknown
    56 [ 124 0x007c ]   3 | AND                                                                                # Bitwise AND operation.                                              result           a, b
    57 [ 125 0x007d ]   3 | PUSH2           0x00e4                                                             # Place 2-byte item on stack.                                         item
    58 [ 128 0x0080 ]   8 | JUMP            @0xe4                                                              # Alter the program counter.                                                           evm.pc

:loc_0x81
    59 [ 129 0x0081 ]   1 | JUMPDEST                                                                           # Mark a valid destination for jumps.
    60 [ 130 0x0082 ]   3 | PUSH1           0x40                                                               # Place 1 byte item on stack.                                         item
    61 [ 132 0x0084 ]   3 | MLOAD                                                                              # Load word from memory.                                                               offset
    62 [ 133 0x0085 ]   3 | SWAP1                                                                              # Exchange 1st and 2nd stack items.
    63 [ 134 0x0086 ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
    64 [ 135 0x0087 ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
    65 [ 136 0x0088 ]   3 | DUP2                                                                               # Duplicate 2nd stack item.
    66 [ 137 0x0089 ]   3 | MSTORE                                                                             # Save word to memory.                                                                 value, offset
    67 [ 138 0x008a ]   3 | PUSH1           0x20                                                               # Place 1 byte item on stack.                                         item
    68 [ 140 0x008c ]   3 | ADD                                                                                # Addition operation.                                                 result           a, b
    69 [ 141 0x008d ]   3 | PUSH1           0x40                                                               # Place 1 byte item on stack.                                         item
    70 [ 143 0x008f ]   3 | MLOAD                                                                              # Load word from memory.                                                               offset
    71 [ 144 0x0090 ]   3 | DUP1                                                                               # Duplicate 1st stack item.
    72 [ 145 0x0091 ]   3 | SWAP2                                                                              # Exchange 1st and 3rd stack items.
    73 [ 146 0x0092 ]   3 | SUB                                                                                # Subtraction operation.                                              result           a, b
    74 [ 147 0x0093 ]   3 | SWAP1                                                                              # Exchange 1st and 2nd stack items.
    75 [ 148 0x0094 ]   0 | RETURN                                                                             # Halt execution returning output data.                                                offset, size

:loc_0x95
  /*******************************************************************
    function maxEntrants()
    payable: False
    inputs: (0) []
    potential signatures: ['maxEntrants()']
  *******************************************************************/
    76 [ 149 0x0095 ]   1 | JUMPDEST                                                              JUMPI@0x31   # Mark a valid destination for jumps.
    77 [ 150 0x0096 ]   2 | CALLVALUE                                                                          # Get deposited value by the instruction/transaction responsible for  msg.value
                                                                                                                 this execution.
    78 [ 151 0x0097 ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
    79 [ 152 0x0098 ]   3 | PUSH2           0x00a0                                                             # Place 2-byte item on stack.                                         item
    80 [ 155 0x009b ]  10 | JUMPI           @0xa0                                                              # Conditionally alter the program counter.                                             evm.pc, condition
    81 [ 156 0x009c ]   3 | PUSH1           0x00                                                               # Place 1 byte item on stack.                                         item
    82 [ 158 0x009e ]   3 | DUP1                                                                               # Duplicate 1st stack item.
    83 [ 159 0x009f ]   0 | REVERT                                                                             # throw an error                                                                       offset, size
:loc_0xa0
    84 [ 160 0x00a0 ]   1 | JUMPDEST                                                              JUMPI@0x9b   # Mark a valid destination for jumps.
    85 [ 161 0x00a1 ]   3 | PUSH2           0x00a8                                                             # Place 2-byte item on stack.                                         item
    86 [ 164 0x00a4 ]   3 | PUSH2           0x0314                                                             # Place 2-byte item on stack.                                         item
    87 [ 167 0x00a7 ]   8 | JUMP            @0x314                                                             # Alter the program counter.                                                           evm.pc

:loc_0xa8
    88 [ 168 0x00a8 ]   1 | JUMPDEST                                                                           # Mark a valid destination for jumps.
    89 [ 169 0x00a9 ]   3 | PUSH1           0x40                                                               # Place 1 byte item on stack.                                         item
    90 [ 171 0x00ab ]   3 | MLOAD                                                                              # Load word from memory.                                                               offset
    91 [ 172 0x00ac ]   3 | PUSH1           0xff                                                               # Place 1 byte item on stack.                                         item
    92 [ 174 0x00ae ]   3 | SWAP1                                                                              # Exchange 1st and 2nd stack items.
    93 [ 175 0x00af ]   3 | SWAP2                                                                              # Exchange 1st and 3rd stack items.
    94 [ 176 0x00b0 ]   3 | AND                                                                                # Bitwise AND operation.                                              result           a, b
    95 [ 177 0x00b1 ]   3 | DUP2                                                                               # Duplicate 2nd stack item.
    96 [ 178 0x00b2 ]   3 | MSTORE                                                                             # Save word to memory.                                                                 value, offset
    97 [ 179 0x00b3 ]   3 | PUSH1           0x20                                                               # Place 1 byte item on stack.                                         item
    98 [ 181 0x00b5 ]   3 | ADD                                                                                # Addition operation.                                                 result           a, b
    99 [ 182 0x00b6 ]   3 | PUSH1           0x40                                                               # Place 1 byte item on stack.                                         item
   100 [ 184 0x00b8 ]   3 | MLOAD                                                                              # Load word from memory.                                                               offset
   101 [ 185 0x00b9 ]   3 | DUP1                                                                               # Duplicate 1st stack item.
   102 [ 186 0x00ba ]   3 | SWAP2                                                                              # Exchange 1st and 3rd stack items.
   103 [ 187 0x00bb ]   3 | SUB                                                                                # Subtraction operation.                                              result           a, b
   104 [ 188 0x00bc ]   3 | SWAP1                                                                              # Exchange 1st and 2nd stack items.
   105 [ 189 0x00bd ]   0 | RETURN                                                                             # Halt execution returning output data.                                                offset, size

:loc_0xbe
  /*******************************************************************
    function totalEntrants()
    payable: False
    inputs: (0) []
    potential signatures: ['totalEntrants()']
  *******************************************************************/
   106 [ 190 0x00be ]   1 | JUMPDEST                                                              JUMPI@0x3c   # Mark a valid destination for jumps.
   107 [ 191 0x00bf ]   2 | CALLVALUE                                                                          # Get deposited value by the instruction/transaction responsible for  msg.value
                                                                                                                 this execution.
   108 [ 192 0x00c0 ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
   109 [ 193 0x00c1 ]   3 | PUSH2           0x00c9                                                             # Place 2-byte item on stack.                                         item
   110 [ 196 0x00c4 ]  10 | JUMPI           @0xc9                                                              # Conditionally alter the program counter.                                             evm.pc, condition
   111 [ 197 0x00c5 ]   3 | PUSH1           0x00                                                               # Place 1 byte item on stack.                                         item
   112 [ 199 0x00c7 ]   3 | DUP1                                                                               # Duplicate 1st stack item.
   113 [ 200 0x00c8 ]   0 | REVERT                                                                             # throw an error                                                                       offset, size
:loc_0xc9
   114 [ 201 0x00c9 ]   1 | JUMPDEST                                                              JUMPI@0xc4   # Mark a valid destination for jumps.
   115 [ 202 0x00ca ]   3 | PUSH2           0x00a8                                                             # Place 2-byte item on stack.                                         item
   116 [ 205 0x00cd ]   3 | PUSH2           0x031a                                                             # Place 2-byte item on stack.                                         item
   117 [ 208 0x00d0 ]   8 | JUMP            @0x31a                                                             # Alter the program counter.                                                           evm.pc

:loc_0xd1
  /*******************************************************************
    function assignAll()
    payable: False
    inputs: (0) []
    potential signatures: ['assignAll()']
  *******************************************************************/
   118 [ 209 0x00d1 ]   1 | JUMPDEST                                                              JUMPI@0x47   # Mark a valid destination for jumps.
   119 [ 210 0x00d2 ]   2 | CALLVALUE                                                                          # Get deposited value by the instruction/transaction responsible for  msg.value
                                                                                                                 this execution.
   120 [ 211 0x00d3 ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
   121 [ 212 0x00d4 ]   3 | PUSH2           0x00dc                                                             # Place 2-byte item on stack.                                         item
   122 [ 215 0x00d7 ]  10 | JUMPI           @0xdc                                                              # Conditionally alter the program counter.                                             evm.pc, condition
   123 [ 216 0x00d8 ]   3 | PUSH1           0x00                                                               # Place 1 byte item on stack.                                         item
   124 [ 218 0x00da ]   3 | DUP1                                                                               # Duplicate 1st stack item.
   125 [ 219 0x00db ]   0 | REVERT                                                                             # throw an error                                                                       offset, size
:loc_0xdc
   126 [ 220 0x00dc ]   1 | JUMPDEST                                                              JUMPI@0xd7   # Mark a valid destination for jumps.
   127 [ 221 0x00dd ]   3 | PUSH2           0x0081                                                             # Place 2-byte item on stack.                                         item
   128 [ 224 0x00e0 ]   3 | PUSH2           0x0320                                                             # Place 2-byte item on stack.                                         item
   129 [ 227 0x00e3 ]   8 | JUMP            @0x320                                                             # Alter the program counter.                                                           evm.pc

:loc_0xe4
   130 [ 228 0x00e4 ]   1 | JUMPDEST                                                              JUMP@0x80    # Mark a valid destination for jumps.
   131 [ 229 0x00e5 ]   3 | PUSH1           0x00                                                               # Place 1 byte item on stack.                                         item
   132 [ 231 0x00e7 ]   2 | ORIGIN                                                                             # Get execution origination address.                                  tx.origin
   133 [ 232 0x00e8 ]   3 | PUSH1           0x01                                                               # Place 1 byte item on stack.                                         item
   134 [ 234 0x00ea ]   3 | PUSH1           0xa0                                                               # Place 1 byte item on stack.                                         item
   135 [ 236 0x00ec ]   3 | PUSH1           0x02                                                               # Place 1 byte item on stack.                                         item
   136 [ 238 0x00ee ]  10 | EXP                                                                                # Exponential operation.                                              result           base, exponent
   137 [ 239 0x00ef ]   3 | SUB                                                                                # Subtraction operation.                                              result           a, b
   138 [ 240 0x00f0 ]   3 | AND                                                                                # Bitwise AND operation.                                              result           a, b
   139 [ 241 0x00f1 ]   2 | CALLER                                                                             # Get caller address.This is the address of the account that is       msg.sender
                                                                                                                 directly responsible for this execution.
   140 [ 242 0x00f2 ]   3 | PUSH1           0x01                                                               # Place 1 byte item on stack.                                         item
   141 [ 244 0x00f4 ]   3 | PUSH1           0xa0                                                               # Place 1 byte item on stack.                                         item
   142 [ 246 0x00f6 ]   3 | PUSH1           0x02                                                               # Place 1 byte item on stack.                                         item
   143 [ 248 0x00f8 ]  10 | EXP                                                                                # Exponential operation.                                              result           base, exponent
   144 [ 249 0x00f9 ]   3 | SUB                                                                                # Subtraction operation.                                              result           a, b
   145 [ 250 0x00fa ]   3 | AND                                                                                # Bitwise AND operation.                                              result           a, b
   146 [ 251 0x00fb ]   3 | EQ                                                                                 # Equality  comparison                                                flag             a, b
   147 [ 252 0x00fc ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
   148 [ 253 0x00fd ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
   149 [ 254 0x00fe ]   3 | ISZERO                                                                             # Simple not operator                                                 flag             a
   150 [ 255 0x00ff ]   3 | PUSH2           0x0107                                                             # Place 2-byte item on stack.                                         item
   151 [ 258 0x0102 ]  10 | JUMPI           @0x107                                                             # Conditionally alter the program counter.                                             evm.pc, condition
   152 [ 259 0x0103 ]   3 | PUSH1           0x00                                                               # Place 1 byte item on stack.                                         item
   153 [ 261 0x0105 ]   3 | DUP1                                                                               # Duplicate 1st stack item.
   154 [ 262 0x0106 ]   0 | REVERT                                                                             # throw an error                                                                       offset, size

[...]

:loc_0x5d5
   954 [1493 0x05d5 ]   1 | JUMPDEST                                                              JUMPI@0x5c9  # Mark a valid destination for jumps.
   955 [1494 0x05d6 ]   2 | POP                                                                                # Remove item from stack.                                                              #dummy
   956 [1495 0x05d7 ]   3 | SWAP1                                                                              # Exchange 1st and 2nd stack items.
   957 [1496 0x05d8 ]   8 | JUMP                                                                               # Alter the program counter.                                                           evm.pc
   958 [1497 0x05d9 ]   0 | STOP                                                                               # Halts execution.
   959 [1498 0x05da ] 750 | LOG1            0x65                                                               # Append log record with one topic.                                                    start, size, topic1
   960 [1500 0x05dc ]   3 | PUSH3           0x7a7a72                                                           # Place 3-byte item on stack.                                         item
   961 [1504 0x05e0 ]   2 | ADDRESS                                                                            # Get address of currently executing account.                         this.address
   962 [1505 0x05e1 ]   2 | PC                                                                                 # Get the value of the program counter prior to the increment.        evm.pc
   963 [1506 0x05e2 ]  30 | SHA3                                                                               # Compute Keccak-256 hash.                                            flag             offset, size
   964 [1507 0x05e3 ]  -1 | UNKNOWN_0xf                                                                        # Invalid opcode
   965 [1508 0x05e4 ]   3 | SWAP4                                                                              # Exchange 1st and 5th stack items.
   966 [1509 0x05e5 ]   3 | SWAP14                                                                             # Exchange 1st and 15th stack items.
   967 [1510 0x05e6 ]   2 | CALLDATASIZE                                                                       # Get size of input data in current environment.                      msg.data.length
   968 [1511 0x05e7 ]  -1 | UNKNOWN_0xe1                                                                       # Invalid opcode
   969 [1512 0x05e8 ]  -1 | UNKNOWN_0xcb                                                                       # Invalid opcode
   970 [1513 0x05e9 ]   3 | PUSH22          0xc68ec825da862dc7082ea12aea89eb3783b2e0423cd2                     # Place 22-byte item on stack.                                        item
   971 [1536 0x0600 ]  30 | SHA3                                                                               # Compute Keccak-256 hash.                                            flag             offset, size
   972 [1537 0x0601 ]  -1 | UNKNOWN_0x28                                                                       # Invalid opcode
   973 [1538 0x0602 ]   3 | PUSH16          0x0029                                                             # Place 16-byte item on stack.                                        item
==============================
reconstructed ABI:
[{'name': 'enter', 'stateMutability': 'nonpayable', 'signature': '0x124c32a1', 'payable': False, 'inputs': [{'name': '_passcode', 'type': 'bytes32'}, {'name': '_gateKey', 'type': 'bytes8'}], 'constant': False, 'type': 'function', 'outputs': [{'name': '', 'type': 'bool'}]}, {'name': 'maxEntrants', 'stateMutability': 'pure', 'signature': '0x60643652', 'payable': False, 'inputs': [], 'constant': True, 'type': 'function', 'outputs': [{'name': '', 'type': 'uint8'}]}, {'name': 'totalEntrants', 'stateMutability': 'view', 'signature': '0x694463a2', 'payable': False, 'inputs': [], 'constant': True, 'type': 'function', 'outputs': [{'name': '', 'type': 'uint8'}]}, {'name': 'assignAll', 'stateMutability': 'nonpayable', 'signature': '0x90ae631d', 'payable': False, 'inputs': [], 'constant': False, 'type': 'function', 'outputs': [{'name': '', 'type': 'bool'}]}, {'stateMutability': 'nonpayable', 'type': 'constructor', 'payable': False, 'inputs': []}]

```
