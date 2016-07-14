# ethereum-dasm 
ethereum vm (evm) bytecode disassembler based on the ethereum yellowpaper

[https://github.com/ethereum/] [https://www.ethereum.org/]

**disassembles evm bytecode** as shown on the [ethereum blockchain](https://etherscan.io/address/0x4432979c7c6bdd19f9ef20787c4ac9cc9710667b#code)

## usage

* provide the path to the ethereum vm bytecode or the bytecode as an argument to evmdasm. Tries to read from stdin by default.
* returns !=0 on errors
* use option `-L` to switch from table to listing mode
* invalid opcodes are prefixed with `UNKNOWN_`
* basic jump/xref analysis
* basicblocking

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
    #> echo "0x12345678" | python evmdasm.py -v critical
    #> python evmdasm.py -v critical "0x12345678"
    #> python evmdasm.py -v critical ether_contract.evm


## examples

* disasm with basic jumptable analysis (incomplete)
```python
#> python evmdasm.py -v critical 0x606060405260d28060106000396000f360606040526000357c010000000000000000000000000000000000000000000000000000000090048063eee97206146041578063f40a049d14606b57603f565b005b605560048080359060200190919050506095565b6040518082815260200191505060405180910390f35b607f600480803590602001909190505060ab565b6040518082815260200191505060405180910390f35b600060a082600260c1565b905060a6565b919050565b600060b682600360c1565b905060bc565b919050565b6000818302905060cc565b9291505056

 Instr.#    addrs.      mnemonic        operand                                                            xrefs                          description
------------------------------------------------------------------------------------------------------------------------------------------------------
[       0] [0x00000000] PUSH1           0x60 ('`')                                                                                        # Place 1 byte item on stack.
[       1] [0x00000002] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[       2] [0x00000004] MSTORE                                                                                                            # Save word to memory.
[       3] [0x00000005] PUSH1           0xd2                                                                                              # Place 1 byte item on stack.
[       4] [0x00000007] DUP1                                                                                                              # Duplicate 1st stack item.
[       5] [0x00000008] PUSH1           0x10                                                                                              # Place 1 byte item on stack.
[       6] [0x0000000a] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[       7] [0x0000000c] CODECOPY                                                                                                          # Copy code running in current environment to memory.
[       8] [0x0000000d] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[       9] [0x0000000f] RETURN                                                                                                            # Halt execution returning output data.

[      10] [0x00000010] PUSH1           0x60 ('`')                                                                                        # Place 1 byte item on stack.
[      11] [0x00000012] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[      12] [0x00000014] MSTORE                                                                                                            # Save word to memory.
[      13] [0x00000015] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[      14] [0x00000017] CALLDATALOAD                                                                                                      # Get input data of current environment.
[      15] [0x00000018] PUSH29          0x0100000000000000000000000000000000000000000000000000000000                                      # Place 29-byte item on stack.
[      16] [0x00000036] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      17] [0x00000037] DIV                                                                                                               # Integer division operation.
[      18] [0x00000038] DUP1                                                                                                              # Duplicate 1st stack item.
[      19] [0x00000039] PUSH4           0xeee97206                                                                                        # Place 4-byte item on stack.
[      20] [0x0000003e] EQ                                                                                                                # Equality  comparison
[      21] [0x0000003f] PUSH1           0x41 ('A')                                                                                        # Place 1 byte item on stack.
[      22] [0x00000041] JUMPI           @0x41                                                                                             # Conditionally alter the program counter.

[      23] [0x00000042] DUP1                                                                                                              # Duplicate 1st stack item.
[      24] [0x00000043] PUSH4           0xf40a049d                                                                                        # Place 4-byte item on stack.
[      25] [0x00000048] EQ                                                                                                                # Equality  comparison
[      26] [0x00000049] PUSH1           0x6b ('k')                                                                                        # Place 1 byte item on stack.
[      27] [0x0000004b] JUMPI           @0x6b                                                                                             # Conditionally alter the program counter.

[      28] [0x0000004c] PUSH1           0x3f ('?')                                                                                        # Place 1 byte item on stack.
[      29] [0x0000004e] JUMP            @0x3f                                                                                             # Alter the program counter.

:loc_0x4f
[      30] [0x0000004f] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[      31] [0x00000050] STOP                                                                                                              # Halts execution.

:loc_0x51
[      32] [0x00000051] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[      33] [0x00000052] PUSH1           0x55 ('U')                                                                                        # Place 1 byte item on stack.
[      34] [0x00000054] PUSH1           0x04                                                                                              # Place 1 byte item on stack.
[      35] [0x00000056] DUP1                                                                                                              # Duplicate 1st stack item.
[      36] [0x00000057] DUP1                                                                                                              # Duplicate 1st stack item.
[      37] [0x00000058] CALLDATALOAD                                                                                                      # Get input data of current environment.
[      38] [0x00000059] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      39] [0x0000005a] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[      40] [0x0000005c] ADD                                                                                                               # Addition operation.
[      41] [0x0000005d] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      42] [0x0000005e] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      43] [0x0000005f] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      44] [0x00000060] POP                                                                                                               # Remove item from stack.
[      45] [0x00000061] POP                                                                                                               # Remove item from stack.
[      46] [0x00000062] PUSH1           0x95                                                                                              # Place 1 byte item on stack.
[      47] [0x00000064] JUMP            @0x95                                                                                             # Alter the program counter.

:loc_0x65
[      48] [0x00000065] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[      49] [0x00000066] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[      50] [0x00000068] MLOAD                                                                                                             # Load word from memory.
[      51] [0x00000069] DUP1                                                                                                              # Duplicate 1st stack item.
[      52] [0x0000006a] DUP3                                                                                                              # Duplicate 3rd stack item.
[      53] [0x0000006b] DUP2                                                                                                              # Duplicate 2nd stack item.
[      54] [0x0000006c] MSTORE                                                                                                            # Save word to memory.
[      55] [0x0000006d] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[      56] [0x0000006f] ADD                                                                                                               # Addition operation.
[      57] [0x00000070] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      58] [0x00000071] POP                                                                                                               # Remove item from stack.
[      59] [0x00000072] POP                                                                                                               # Remove item from stack.
[      60] [0x00000073] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[      61] [0x00000075] MLOAD                                                                                                             # Load word from memory.
[      62] [0x00000076] DUP1                                                                                                              # Duplicate 1st stack item.
[      63] [0x00000077] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      64] [0x00000078] SUB                                                                                                               # Subtraction operation.
[      65] [0x00000079] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      66] [0x0000007a] RETURN                                                                                                            # Halt execution returning output data.

:loc_0x7b
[      67] [0x0000007b] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[      68] [0x0000007c] PUSH1           0x7f ('\x7f')                                                                                     # Place 1 byte item on stack.
[      69] [0x0000007e] PUSH1           0x04                                                                                              # Place 1 byte item on stack.
[      70] [0x00000080] DUP1                                                                                                              # Duplicate 1st stack item.
[      71] [0x00000081] DUP1                                                                                                              # Duplicate 1st stack item.
[      72] [0x00000082] CALLDATALOAD                                                                                                      # Get input data of current environment.
[      73] [0x00000083] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      74] [0x00000084] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[      75] [0x00000086] ADD                                                                                                               # Addition operation.
[      76] [0x00000087] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      77] [0x00000088] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      78] [0x00000089] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      79] [0x0000008a] POP                                                                                                               # Remove item from stack.
[      80] [0x0000008b] POP                                                                                                               # Remove item from stack.
[      81] [0x0000008c] PUSH1           0xab                                                                                              # Place 1 byte item on stack.
[      82] [0x0000008e] JUMP            @0xab                                                                                             # Alter the program counter.

:loc_0x8f
[      83] [0x0000008f] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[      84] [0x00000090] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[      85] [0x00000092] MLOAD                                                                                                             # Load word from memory.
[      86] [0x00000093] DUP1                                                                                                              # Duplicate 1st stack item.
[      87] [0x00000094] DUP3                                                                                                              # Duplicate 3rd stack item.
[      88] [0x00000095] DUP2                                                                                                              # Duplicate 2nd stack item.
[      89] [0x00000096] MSTORE                                                                                                            # Save word to memory.
[      90] [0x00000097] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[      91] [0x00000099] ADD                                                                                                               # Addition operation.
[      92] [0x0000009a] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      93] [0x0000009b] POP                                                                                                               # Remove item from stack.
[      94] [0x0000009c] POP                                                                                                               # Remove item from stack.
[      95] [0x0000009d] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[      96] [0x0000009f] MLOAD                                                                                                             # Load word from memory.
[      97] [0x000000a0] DUP1                                                                                                              # Duplicate 1st stack item.
[      98] [0x000000a1] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      99] [0x000000a2] SUB                                                                                                               # Subtraction operation.
[     100] [0x000000a3] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     101] [0x000000a4] RETURN                                                                                                            # Halt execution returning output data.

:loc_0xa5
[     102] [0x000000a5] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     103] [0x000000a6] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     104] [0x000000a8] PUSH1           0xa0                                                                                              # Place 1 byte item on stack.
[     105] [0x000000aa] DUP3                                                                                                              # Duplicate 3rd stack item.
[     106] [0x000000ab] PUSH1           0x02                                                                                              # Place 1 byte item on stack.
[     107] [0x000000ad] PUSH1           0xc1                                                                                              # Place 1 byte item on stack.
[     108] [0x000000af] JUMP            @0xc1                                                                                             # Alter the program counter.

:loc_0xb0
[     109] [0x000000b0] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     110] [0x000000b1] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     111] [0x000000b2] POP                                                                                                               # Remove item from stack.
[     112] [0x000000b3] PUSH1           0xa6                                                                                              # Place 1 byte item on stack.
[     113] [0x000000b5] JUMP            @0xa6                                                                                             # Alter the program counter.

:loc_0xb6
[     114] [0x000000b6] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     115] [0x000000b7] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     116] [0x000000b8] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     117] [0x000000b9] POP                                                                                                               # Remove item from stack.
[     118] [0x000000ba] JUMP                                                                                                              # Alter the program counter.

:loc_0xbb
[     119] [0x000000bb] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     120] [0x000000bc] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     121] [0x000000be] PUSH1           0xb6                                                                                              # Place 1 byte item on stack.
[     122] [0x000000c0] DUP3                                                                                                              # Duplicate 3rd stack item.
[     123] [0x000000c1] PUSH1           0x03                                                                                              # Place 1 byte item on stack.
[     124] [0x000000c3] PUSH1           0xc1                                                                                              # Place 1 byte item on stack.
[     125] [0x000000c5] JUMP            @0xc1                                                                                             # Alter the program counter.

:loc_0xc6
[     126] [0x000000c6] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     127] [0x000000c7] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     128] [0x000000c8] POP                                                                                                               # Remove item from stack.
[     129] [0x000000c9] PUSH1           0xbc                                                                                              # Place 1 byte item on stack.
[     130] [0x000000cb] JUMP            @0xbc                                                                                             # Alter the program counter.

:loc_0xcc
[     131] [0x000000cc] JUMPDEST                                                                           JUMP@0xdb                      # Mark a valid destination for jumps.
[     132] [0x000000cd] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     133] [0x000000ce] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     134] [0x000000cf] POP                                                                                                               # Remove item from stack.
[     135] [0x000000d0] JUMP                                                                                                              # Alter the program counter.

:loc_0xd1
[     136] [0x000000d1] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     137] [0x000000d2] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     138] [0x000000d4] DUP2                                                                                                              # Duplicate 2nd stack item.
[     139] [0x000000d5] DUP4                                                                                                              # Duplicate 4th stack item.
[     140] [0x000000d6] MUL                                                                                                               # Multiplication operation.
[     141] [0x000000d7] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     142] [0x000000d8] POP                                                                                                               # Remove item from stack.
[     143] [0x000000d9] PUSH1           0xcc                                                                                              # Place 1 byte item on stack.
[     144] [0x000000db] JUMP            @0xcc                                                                                             # Alter the program counter.

:loc_0xdc
[     145] [0x000000dc] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     146] [0x000000dd] SWAP3                                                                                                             # Exchange 1st and 4th stack items.
[     147] [0x000000de] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     148] [0x000000df] POP                                                                                                               # Remove item from stack.
[     149] [0x000000e0] POP                                                                                                               # Remove item from stack.
[     150] [0x000000e1] JUMP                                                                                                              # Alter the program counter.

assemble(disassemble(evmcode))== True

```
