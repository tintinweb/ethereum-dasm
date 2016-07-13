# ethereum-dasm 
ethereum vm (evm) bytecode disassembler based on the ethereum yellowpaper

[https://github.com/ethereum/] [https://www.ethereum.org/]

**disassembles evm bytecode** as shown on the [ethereum blockchain](https://etherscan.io/address/0x4432979c7c6bdd19f9ef20787c4ac9cc9710667b#code)

## usage

* provide the path to the ethereum vm bytecode or the bytecode as an argument to evmdasm. Tries to read from stdin by default.
* returns !=0 on errors
* use option `-L` to switch from table to listing mode

```
#> evmdasm.py --help
Usage: evmdasm.py [options]
    
       example: evmdasm.py [-L -v] <file_or_bytecode>
                evmdasm.py [-L -v] # read from stdin
    

Options:
  -h, --help            show this help message and exit
  -v VERBOSITY, --verbosity=VERBOSITY
                        available loglevels:
                        critical,fatal,error,warning,warn,info,debug,notset
                        [default: notset]
  -L, --listing         disables table mode, outputs assembly only

```


## examples

* via stdin
```python
#> echo "0x12345678" | python ethereum_dasm
 Instr.#   pos. mnemonic        operand                   description
------------------------------------------------------------------------------------------------------------------------
2016-07-14 00:32:34,059 - WARNING - skipping invalid byte: '0x'
[     0]      0 SLT                                         # Signed less-than comparison
[     1]      1 CALLVALUE                                   # Get deposited value by the instruction/transaction responsible for this execution.
[     2]      2 JUMP                                        # Alter the program counter.
[     3]      3 PUSH25                                      # Place 25-byte item on stack.
```

* https://etherchain.org/account/0x012a5642306b0deb8d65f281d289998223dfb7c7#code
```python
#> python ethereum_dasm 0x60606040526000357c01000000000000000000000000000000000000000000000000000000009004806390b98a1114610044578063bbd39ac01461007157610042565b005b61005b6004803590602001803590602001506100b3565b6040518082815260200191505060405180910390f35b610082600480359060200150610098565b6040518082815260200191505060405180910390f35b60006000506020528060005260406000206000915090505481565b600081600060005060003373ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000505410156100f557600090506101e9565b81600060005060003373ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008282825054039250508190555081600060005060008573ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828282505401925050819055507f16cdf1707799c6655baac6e210f52b94b7cec08adcaf9ede7dfe8649da926146338484604051808473ffffffffffffffffffffffffffffffffffffffff1681526020018373ffffffffffffffffffffffffffffffffffffffff168152602001828152602001935050505060405180910390a1600190506101e9565b9291505056
 Instr.#   pos. mnemonic        operand                                                            description
------------------------------------------------------------------------------------------------------------------------
2016-07-14 00:23:54,075 - WARNING - skipping invalid byte: '0x'
[     0]      0 PUSH1           0x60                                                               # Place 1 byte item on stack.
[     1]      2 PUSH1           0x40                                                               # Place 1 byte item on stack.
[     2]      4 MSTORE                                                                             # Save word to memory.
[     3]      5 PUSH1           0x00                                                               # Place 1 byte item on stack.
[     4]      7 CALLDATALOAD                                                                       # Get input data of current environment.
[     5]      8 PUSH29          0x0100000000000000000000000000000000000000000000000000000000       # Place 29-byte item on stack.
[     6]     38 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[     7]     39 DIV                                                                                # Integer division operation.
[     8]     40 DUP1                                                                               # Duplicate 1st stack item.
[     9]     41 PUSH4           0x90b98a11                                                         # Place 4-byte item on stack.
[    10]     46 EQ                                                                                 # Equality  comparison
[    11]     47 PUSH2           0x0044                                                             # Place 2-byte item on stack.
[    12]     50 JUMPI                                                                              # Conditionally alter the program counter.
[    13]     51 DUP1                                                                               # Duplicate 1st stack item.
[    14]     52 PUSH4           0xbbd39ac0                                                         # Place 4-byte item on stack.
[    15]     57 EQ                                                                                 # Equality  comparison
[    16]     58 PUSH2           0x0071                                                             # Place 2-byte item on stack.
[    17]     61 JUMPI                                                                              # Conditionally alter the program counter.
[    18]     62 PUSH2           0x0042                                                             # Place 2-byte item on stack.
[    19]     65 JUMP                                                                               # Alter the program counter.
[    20]     66 JUMPDEST                                                                           # Mark a valid destination for jumps.
[    21]     67 STOP                                                                               # Halts execution.
[    22]     68 JUMPDEST                                                                           # Mark a valid destination for jumps.
[    23]     69 PUSH2           0x005b                                                             # Place 2-byte item on stack.
[    24]     72 PUSH1           0x04                                                               # Place 1 byte item on stack.
[    25]     74 DUP1                                                                               # Duplicate 1st stack item.
[    26]     75 CALLDATALOAD                                                                       # Get input data of current environment.
[    27]     76 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[    28]     77 PUSH1           0x20                                                               # Place 1 byte item on stack.
[    29]     79 ADD                                                                                # Addition operation.
[    30]     80 DUP1                                                                               # Duplicate 1st stack item.
[    31]     81 CALLDATALOAD                                                                       # Get input data of current environment.
[    32]     82 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[    33]     83 PUSH1           0x20                                                               # Place 1 byte item on stack.
[    34]     85 ADD                                                                                # Addition operation.
[    35]     86 POP                                                                                # Remove item from stack.
[    36]     87 PUSH2           0x00b3                                                             # Place 2-byte item on stack.
[    37]     90 JUMP                                                                               # Alter the program counter.
[    38]     91 JUMPDEST                                                                           # Mark a valid destination for jumps.
[    39]     92 PUSH1           0x40                                                               # Place 1 byte item on stack.
[    40]     94 MLOAD                                                                              # Load word from memory.
[    41]     95 DUP1                                                                               # Duplicate 1st stack item.
[    42]     96 DUP3                                                                               # Duplicate 3rd stack item.
[    43]     97 DUP2                                                                               # Duplicate 2nd stack item.
[    44]     98 MSTORE                                                                             # Save word to memory.
[    45]     99 PUSH1           0x20                                                               # Place 1 byte item on stack.
[    46]    101 ADD                                                                                # Addition operation.
[    47]    102 SWAP2                                                                              # Exchange 1st and 3rd stack items.
[    48]    103 POP                                                                                # Remove item from stack.
[    49]    104 POP                                                                                # Remove item from stack.
[    50]    105 PUSH1           0x40                                                               # Place 1 byte item on stack.
[    51]    107 MLOAD                                                                              # Load word from memory.
[    52]    108 DUP1                                                                               # Duplicate 1st stack item.
[    53]    109 SWAP2                                                                              # Exchange 1st and 3rd stack items.
[    54]    110 SUB                                                                                # Subtraction operation.
[    55]    111 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[    56]    112 RETURN                                                                             # Halt execution returning output data.
[    57]    113 JUMPDEST                                                                           # Mark a valid destination for jumps.
[    58]    114 PUSH2           0x0082                                                             # Place 2-byte item on stack.
[    59]    117 PUSH1           0x04                                                               # Place 1 byte item on stack.
[    60]    119 DUP1                                                                               # Duplicate 1st stack item.
[    61]    120 CALLDATALOAD                                                                       # Get input data of current environment.
[    62]    121 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[    63]    122 PUSH1           0x20                                                               # Place 1 byte item on stack.
[    64]    124 ADD                                                                                # Addition operation.
[    65]    125 POP                                                                                # Remove item from stack.
[    66]    126 PUSH2           0x0098                                                             # Place 2-byte item on stack.
[    67]    129 JUMP                                                                               # Alter the program counter.
[    68]    130 JUMPDEST                                                                           # Mark a valid destination for jumps.
[    69]    131 PUSH1           0x40                                                               # Place 1 byte item on stack.
[    70]    133 MLOAD                                                                              # Load word from memory.
[    71]    134 DUP1                                                                               # Duplicate 1st stack item.
[    72]    135 DUP3                                                                               # Duplicate 3rd stack item.
[    73]    136 DUP2                                                                               # Duplicate 2nd stack item.
[    74]    137 MSTORE                                                                             # Save word to memory.
[    75]    138 PUSH1           0x20                                                               # Place 1 byte item on stack.
[    76]    140 ADD                                                                                # Addition operation.
[    77]    141 SWAP2                                                                              # Exchange 1st and 3rd stack items.
[    78]    142 POP                                                                                # Remove item from stack.
[    79]    143 POP                                                                                # Remove item from stack.
[    80]    144 PUSH1           0x40                                                               # Place 1 byte item on stack.
[    81]    146 MLOAD                                                                              # Load word from memory.
[    82]    147 DUP1                                                                               # Duplicate 1st stack item.
[    83]    148 SWAP2                                                                              # Exchange 1st and 3rd stack items.
[    84]    149 SUB                                                                                # Subtraction operation.
[    85]    150 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[    86]    151 RETURN                                                                             # Halt execution returning output data.
[    87]    152 JUMPDEST                                                                           # Mark a valid destination for jumps.
[    88]    153 PUSH1           0x00                                                               # Place 1 byte item on stack.
[    89]    155 PUSH1           0x00                                                               # Place 1 byte item on stack.
[    90]    157 POP                                                                                # Remove item from stack.
[    91]    158 PUSH1           0x20                                                               # Place 1 byte item on stack.
[    92]    160 MSTORE                                                                             # Save word to memory.
[    93]    161 DUP1                                                                               # Duplicate 1st stack item.
[    94]    162 PUSH1           0x00                                                               # Place 1 byte item on stack.
[    95]    164 MSTORE                                                                             # Save word to memory.
[    96]    165 PUSH1           0x40                                                               # Place 1 byte item on stack.
[    97]    167 PUSH1           0x00                                                               # Place 1 byte item on stack.
[    98]    169 SHA3                                                                               # Compute Keccak-256 hash.
[    99]    170 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   100]    172 SWAP2                                                                              # Exchange 1st and 3rd stack items.
[   101]    173 POP                                                                                # Remove item from stack.
[   102]    174 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   103]    175 POP                                                                                # Remove item from stack.
[   104]    176 SLOAD                                                                              # Load word from storage.
[   105]    177 DUP2                                                                               # Duplicate 2nd stack item.
[   106]    178 JUMP                                                                               # Alter the program counter.
[   107]    179 JUMPDEST                                                                           # Mark a valid destination for jumps.
[   108]    180 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   109]    182 DUP2                                                                               # Duplicate 2nd stack item.
[   110]    183 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   111]    185 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   112]    187 POP                                                                                # Remove item from stack.
[   113]    188 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   114]    190 CALLER                                                                             # Get caller address.This is the address of the account that is directly responsible for this execution.
[   115]    191 PUSH20          0xffffffffffffffffffffffffffffffffffffffff                         # Place 20-byte item on stack.
[   116]    212 AND                                                                                # Bitwise AND operation.
[   117]    213 DUP2                                                                               # Duplicate 2nd stack item.
[   118]    214 MSTORE                                                                             # Save word to memory.
[   119]    215 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   120]    217 ADD                                                                                # Addition operation.
[   121]    218 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   122]    219 DUP2                                                                               # Duplicate 2nd stack item.
[   123]    220 MSTORE                                                                             # Save word to memory.
[   124]    221 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   125]    223 ADD                                                                                # Addition operation.
[   126]    224 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   127]    226 SHA3                                                                               # Compute Keccak-256 hash.
[   128]    227 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   129]    229 POP                                                                                # Remove item from stack.
[   130]    230 SLOAD                                                                              # Load word from storage.
[   131]    231 LT                                                                                 # Lesser-than comparison
[   132]    232 ISZERO                                                                             # Simple not operator
[   133]    233 PUSH2           0x00f5                                                             # Place 2-byte item on stack.
[   134]    236 JUMPI                                                                              # Conditionally alter the program counter.
[   135]    237 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   136]    239 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   137]    240 POP                                                                                # Remove item from stack.
[   138]    241 PUSH2           0x01e9                                                             # Place 2-byte item on stack.
[   139]    244 JUMP                                                                               # Alter the program counter.
[   140]    245 JUMPDEST                                                                           # Mark a valid destination for jumps.
[   141]    246 DUP2                                                                               # Duplicate 2nd stack item.
[   142]    247 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   143]    249 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   144]    251 POP                                                                                # Remove item from stack.
[   145]    252 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   146]    254 CALLER                                                                             # Get caller address.This is the address of the account that is directly responsible for this execution.
[   147]    255 PUSH20          0xffffffffffffffffffffffffffffffffffffffff                         # Place 20-byte item on stack.
[   148]    276 AND                                                                                # Bitwise AND operation.
[   149]    277 DUP2                                                                               # Duplicate 2nd stack item.
[   150]    278 MSTORE                                                                             # Save word to memory.
[   151]    279 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   152]    281 ADD                                                                                # Addition operation.
[   153]    282 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   154]    283 DUP2                                                                               # Duplicate 2nd stack item.
[   155]    284 MSTORE                                                                             # Save word to memory.
[   156]    285 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   157]    287 ADD                                                                                # Addition operation.
[   158]    288 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   159]    290 SHA3                                                                               # Compute Keccak-256 hash.
[   160]    291 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   161]    293 DUP3                                                                               # Duplicate 3rd stack item.
[   162]    294 DUP3                                                                               # Duplicate 3rd stack item.
[   163]    295 DUP3                                                                               # Duplicate 3rd stack item.
[   164]    296 POP                                                                                # Remove item from stack.
[   165]    297 SLOAD                                                                              # Load word from storage.
[   166]    298 SUB                                                                                # Subtraction operation.
[   167]    299 SWAP3                                                                              # Exchange 1st and 4th stack items.
[   168]    300 POP                                                                                # Remove item from stack.
[   169]    301 POP                                                                                # Remove item from stack.
[   170]    302 DUP2                                                                               # Duplicate 2nd stack item.
[   171]    303 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   172]    304 SSTORE                                                                             # Save word to storage.
[   173]    305 POP                                                                                # Remove item from stack.
[   174]    306 DUP2                                                                               # Duplicate 2nd stack item.
[   175]    307 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   176]    309 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   177]    311 POP                                                                                # Remove item from stack.
[   178]    312 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   179]    314 DUP6                                                                               # Duplicate 6th stack item.
[   180]    315 PUSH20          0xffffffffffffffffffffffffffffffffffffffff                         # Place 20-byte item on stack.
[   181]    336 AND                                                                                # Bitwise AND operation.
[   182]    337 DUP2                                                                               # Duplicate 2nd stack item.
[   183]    338 MSTORE                                                                             # Save word to memory.
[   184]    339 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   185]    341 ADD                                                                                # Addition operation.
[   186]    342 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   187]    343 DUP2                                                                               # Duplicate 2nd stack item.
[   188]    344 MSTORE                                                                             # Save word to memory.
[   189]    345 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   190]    347 ADD                                                                                # Addition operation.
[   191]    348 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   192]    350 SHA3                                                                               # Compute Keccak-256 hash.
[   193]    351 PUSH1           0x00                                                               # Place 1 byte item on stack.
[   194]    353 DUP3                                                                               # Duplicate 3rd stack item.
[   195]    354 DUP3                                                                               # Duplicate 3rd stack item.
[   196]    355 DUP3                                                                               # Duplicate 3rd stack item.
[   197]    356 POP                                                                                # Remove item from stack.
[   198]    357 SLOAD                                                                              # Load word from storage.
[   199]    358 ADD                                                                                # Addition operation.
[   200]    359 SWAP3                                                                              # Exchange 1st and 4th stack items.
[   201]    360 POP                                                                                # Remove item from stack.
[   202]    361 POP                                                                                # Remove item from stack.
[   203]    362 DUP2                                                                               # Duplicate 2nd stack item.
[   204]    363 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   205]    364 SSTORE                                                                             # Save word to storage.
[   206]    365 POP                                                                                # Remove item from stack.
[   207]    366 PUSH32          0x16cdf1707799c6655baac6e210f52b94b7cec08adcaf9ede7dfe8649da926146 # Place 32-byte (full word) item on stack.
[   208]    399 CALLER                                                                             # Get caller address.This is the address of the account that is directly responsible for this execution.
[   209]    400 DUP5                                                                               # Duplicate 5th stack item.
[   210]    401 DUP5                                                                               # Duplicate 5th stack item.
[   211]    402 PUSH1           0x40                                                               # Place 1 byte item on stack.
[   212]    404 MLOAD                                                                              # Load word from memory.
[   213]    405 DUP1                                                                               # Duplicate 1st stack item.
[   214]    406 DUP5                                                                               # Duplicate 5th stack item.
[   215]    407 PUSH20          0xffffffffffffffffffffffffffffffffffffffff                         # Place 20-byte item on stack.
[   216]    428 AND                                                                                # Bitwise AND operation.
[   217]    429 DUP2                                                                               # Duplicate 2nd stack item.
[   218]    430 MSTORE                                                                             # Save word to memory.
[   219]    431 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   220]    433 ADD                                                                                # Addition operation.
[   221]    434 DUP4                                                                               # Duplicate 4th stack item.
[   222]    435 PUSH20          0xffffffffffffffffffffffffffffffffffffffff                         # Place 20-byte item on stack.
[   223]    456 AND                                                                                # Bitwise AND operation.
[   224]    457 DUP2                                                                               # Duplicate 2nd stack item.
[   225]    458 MSTORE                                                                             # Save word to memory.
[   226]    459 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   227]    461 ADD                                                                                # Addition operation.
[   228]    462 DUP3                                                                               # Duplicate 3rd stack item.
[   229]    463 DUP2                                                                               # Duplicate 2nd stack item.
[   230]    464 MSTORE                                                                             # Save word to memory.
[   231]    465 PUSH1           0x20                                                               # Place 1 byte item on stack.
[   232]    467 ADD                                                                                # Addition operation.
[   233]    468 SWAP4                                                                              # Exchange 1st and 5th stack items.
[   234]    469 POP                                                                                # Remove item from stack.
[   235]    470 POP                                                                                # Remove item from stack.
[   236]    471 POP                                                                                # Remove item from stack.
[   237]    472 POP                                                                                # Remove item from stack.
[   238]    473 PUSH1           0x40                                                               # Place 1 byte item on stack.
[   239]    475 MLOAD                                                                              # Load word from memory.
[   240]    476 DUP1                                                                               # Duplicate 1st stack item.
[   241]    477 SWAP2                                                                              # Exchange 1st and 3rd stack items.
[   242]    478 SUB                                                                                # Subtraction operation.
[   243]    479 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   244]    480 LOG1            0x60                                                               # Append log record with one topic.
[   245]    482 ADD                                                                                # Addition operation.
[   246]    483 SWAP1                                                                              # Exchange 1st and 2nd stack items.
[   247]    484 POP                                                                                # Remove item from stack.
[   248]    485 PUSH2           0x01e9                                                             # Place 2-byte item on stack.
[   249]    488 JUMP                                                                               # Alter the program counter.
[   250]    489 JUMPDEST                                                                           # Mark a valid destination for jumps.
[   251]    490 SWAP3                                                                              # Exchange 1st and 4th stack items.
[   252]    491 SWAP2                                                                              # Exchange 1st and 3rd stack items.
[   253]    492 POP                                                                                # Remove item from stack.
[   254]    493 POP                                                                                # Remove item from stack.
[   255]    494 JUMP                                                                               # Alter the program counter.
2016-07-14 00:23:54,091 - WARNING - finished in 0.016 seconds.

```

* evmcode with invalid opcodes like https://etherscan.io/address/0x4432979c7c6bdd19f9ef20787c4ac9cc9710667b#code
```python
#> python ethereum_dasm contract_0x4432979c7c6bdd19f9ef20787c4ac9cc9710667b.evm
...
[  1350]   1996 MULMOD                         # Modulo
[  1351]   1997 CALLCODE                       # Message-call into this account with alternative accounts code.
[  1352]   1998 DUP15                          # Duplicate 15th stack item.
[  1353]   1999 DUP7                           # Duplicate 7th stack item.
[  1354]   2000 STOP                           # Halts execution.
2016-07-14 00:34:22,263 - ERROR - error: byte at position 2001 (0xb4) is not a valid operator
Traceback (most recent call last):
  File "ethereum_dasm\evmdasm.py", line 208, in disassemble
    mnemonic = self.OPCODE_TABLE[opcode].consume(iter_bytecode)
KeyError: 180
[  1355]   2001 UNKNOWN_0xb4                   # error: byte at position 2001 (0xb4) is not a valid operator; KeyError(180,)
2016-07-14 00:34:22,263 - ERROR - error: byte at position 2002 (0xaa) is not a valid operator
Traceback (most recent call last):
  File "ethereum_dasm\evmdasm.py", line 208, in disassemble
    mnemonic = self.OPCODE_TABLE[opcode].consume(iter_bytecode)
KeyError: 170
[  1356]   2002 UNKNOWN_0xaa                   # error: byte at position 2002 (0xaa) is not a valid operator; KeyError(170,)
[  1357]   2003 DUP13                          # Duplicate 13th stack item.
[  1358]   2004 PUSH6           0xc6b64bfe7fe3 # Place 6-byte item on stack.
[  1359]   2011 PUSH12          0xd19b         # Place 12-byte item on stack.
2016-07-14 00:34:22,279 - WARNING - disassembly finished with 12 errors
```
