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

* disasm with basic jumptable analysis (incomplete)
```python
#> python evmdasm.py -v critical 0x6060604052610209806100126000396000f3606060405260e060020a60003504634ed3885e81146100265780636d4ce63c146100cc575b005b60206004803580820135601f810184900490930260809081016040526060848152610024946024939192918401918190838280828437509496505050505050508060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106101a057805160ff19168380011785555b5061019b9291505b808211156101d0578381556001016100b9565b61012d60006060818152815460a06020601f60026000196101006001871615020190941693909304928301819004028101604052608082815292939190828280156101ff5780601f106101d4576101008083540402835291602001916101ff565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f16801561018d5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b505050565b828001600101855582156100b1579182015b828111156100b15782518260005055916020019190600101906101b2565b5090565b820191906000526020600020905b8154815290600101906020018083116101e257829003601f168201915b505050505090509056

 Instr.#    addrs.      mnemonic        operand                                                            xrefs                          description
------------------------------------------------------------------------------------------------------------------------------------------------------
[       0] [0x00000000] PUSH1           0x60 ('`')                                                                                        # Place 1 byte item on stack.
[       1] [0x00000002] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[       2] [0x00000004] MSTORE                                                                                                            # Save word to memory.
[       3] [0x00000005] PUSH2           0x0209                                                                                            # Place 2-byte item on stack.
[       4] [0x00000008] DUP1                                                                                                              # Duplicate 1st stack item.
[       5] [0x00000009] PUSH2           0x0012                                                                                            # Place 2-byte item on stack.
[       6] [0x0000000c] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[       7] [0x0000000e] CODECOPY                                                                                                          # Copy code running in current environment to memory.
[       8] [0x0000000f] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[       9] [0x00000011] RETURN                                                                                                            # Halt execution returning output data.
[      10] [0x00000012] PUSH1           0x60 ('`')                                                                                        # Place 1 byte item on stack.
[      11] [0x00000014] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[      12] [0x00000016] MSTORE                                                                                                            # Save word to memory.
[      13] [0x00000017] PUSH1           0xe0                                                                                              # Place 1 byte item on stack.
[      14] [0x00000019] PUSH1           0x02                                                                                              # Place 1 byte item on stack.
[      15] [0x0000001b] EXP                                                                                                               # Exponential operation.
[      16] [0x0000001c] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[      17] [0x0000001e] CALLDATALOAD                                                                                                      # Get input data of current environment.
[      18] [0x0000001f] DIV                                                                                                               # Integer division operation.
[      19] [0x00000020] PUSH4           0x4ed3885e                                                                                        # Place 4-byte item on stack.
[      20] [0x00000025] DUP2                                                                                                              # Duplicate 2nd stack item.
[      21] [0x00000026] EQ                                                                                 JUMPI@0x2a                     # Equality  comparison
[      22] [0x00000027] PUSH2           0x0026                                                                                            # Place 2-byte item on stack.
[      23] [0x0000002a] JUMPI           @0x26                                                                                             # Conditionally alter the program counter.
[      24] [0x0000002b] DUP1                                                                                                              # Duplicate 1st stack item.
[      25] [0x0000002c] PUSH4           0x6d4ce63c ('mL\xe6<')                                                                            # Place 4-byte item on stack.
[      26] [0x00000031] EQ                                                                                                                # Equality  comparison
[      27] [0x00000032] PUSH2           0x00cc                                                                                            # Place 2-byte item on stack.
[      28] [0x00000035] JUMPI           @0xcc                                                                                             # Conditionally alter the program counter.
[      29] [0x00000036] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[      30] [0x00000037] STOP                                                                                                              # Halts execution.
[      31] [0x00000038] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[      32] [0x00000039] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[      33] [0x0000003b] PUSH1           0x04                                                                                              # Place 1 byte item on stack.
[      34] [0x0000003d] DUP1                                                                                                              # Duplicate 1st stack item.
[      35] [0x0000003e] CALLDATALOAD                                                                                                      # Get input data of current environment.
[      36] [0x0000003f] DUP1                                                                                                              # Duplicate 1st stack item.
[      37] [0x00000040] DUP3                                                                                                              # Duplicate 3rd stack item.
[      38] [0x00000041] ADD                                                                                                               # Addition operation.
[      39] [0x00000042] CALLDATALOAD                                                                                                      # Get input data of current environment.
[      40] [0x00000043] PUSH1           0x1f                                                                                              # Place 1 byte item on stack.
[      41] [0x00000045] DUP2                                                                                                              # Duplicate 2nd stack item.
[      42] [0x00000046] ADD                                                                                                               # Addition operation.
[      43] [0x00000047] DUP5                                                                                                              # Duplicate 5th stack item.
[      44] [0x00000048] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      45] [0x00000049] DIV                                                                                                               # Integer division operation.
[      46] [0x0000004a] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      47] [0x0000004b] SWAP4                                                                                                             # Exchange 1st and 5th stack items.
[      48] [0x0000004c] MUL                                                                                                               # Multiplication operation.
[      49] [0x0000004d] PUSH1           0x80                                                                                              # Place 1 byte item on stack.
[      50] [0x0000004f] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      51] [0x00000050] DUP2                                                                                                              # Duplicate 2nd stack item.
[      52] [0x00000051] ADD                                                                                                               # Addition operation.
[      53] [0x00000052] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[      54] [0x00000054] MSTORE                                                                                                            # Save word to memory.
[      55] [0x00000055] PUSH1           0x60 ('`')                                                                                        # Place 1 byte item on stack.
[      56] [0x00000057] DUP5                                                                                                              # Duplicate 5th stack item.
[      57] [0x00000058] DUP2                                                                                                              # Duplicate 2nd stack item.
[      58] [0x00000059] MSTORE                                                                                                            # Save word to memory.
[      59] [0x0000005a] PUSH2           0x0024                                                                                            # Place 2-byte item on stack.
[      60] [0x0000005d] SWAP5                                                                                                             # Exchange 1st and 6th stack items.
[      61] [0x0000005e] PUSH1           0x24 ('$')                                                                                        # Place 1 byte item on stack.
[      62] [0x00000060] SWAP4                                                                                                             # Exchange 1st and 5th stack items.
[      63] [0x00000061] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      64] [0x00000062] SWAP3                                                                                                             # Exchange 1st and 4th stack items.
[      65] [0x00000063] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      66] [0x00000064] DUP5                                                                                                              # Duplicate 5th stack item.
[      67] [0x00000065] ADD                                                                                                               # Addition operation.
[      68] [0x00000066] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[      69] [0x00000067] DUP2                                                                                                              # Duplicate 2nd stack item.
[      70] [0x00000068] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      71] [0x00000069] DUP4                                                                                                              # Duplicate 4th stack item.
[      72] [0x0000006a] DUP3                                                                                                              # Duplicate 3rd stack item.
[      73] [0x0000006b] DUP1                                                                                                              # Duplicate 1st stack item.
[      74] [0x0000006c] DUP3                                                                                                              # Duplicate 3rd stack item.
[      75] [0x0000006d] DUP5                                                                                                              # Duplicate 5th stack item.
[      76] [0x0000006e] CALLDATACOPY                                                                                                      # Copy input data in current environment to memory. This pertains to the input data passed with the message call instruction or transaction.
[      77] [0x0000006f] POP                                                                                                               # Remove item from stack.
[      78] [0x00000070] SWAP5                                                                                                             # Exchange 1st and 6th stack items.
[      79] [0x00000071] SWAP7                                                                                                             # Exchange 1st and 8th stack items.
[      80] [0x00000072] POP                                                                                                               # Remove item from stack.
[      81] [0x00000073] POP                                                                                                               # Remove item from stack.
[      82] [0x00000074] POP                                                                                                               # Remove item from stack.
[      83] [0x00000075] POP                                                                                                               # Remove item from stack.
[      84] [0x00000076] POP                                                                                                               # Remove item from stack.
[      85] [0x00000077] POP                                                                                                               # Remove item from stack.
[      86] [0x00000078] POP                                                                                                               # Remove item from stack.
[      87] [0x00000079] DUP1                                                                                                              # Duplicate 1st stack item.
[      88] [0x0000007a] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[      89] [0x0000007c] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[      90] [0x0000007e] POP                                                                                                               # Remove item from stack.
[      91] [0x0000007f] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      92] [0x00000080] DUP1                                                                                                              # Duplicate 1st stack item.
[      93] [0x00000081] MLOAD                                                                                                             # Load word from memory.
[      94] [0x00000082] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      95] [0x00000083] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[      96] [0x00000085] ADD                                                                                                               # Addition operation.
[      97] [0x00000086] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[      98] [0x00000087] DUP3                                                                                                              # Duplicate 3rd stack item.
[      99] [0x00000088] DUP1                                                                                                              # Duplicate 1st stack item.
[     100] [0x00000089] SLOAD                                                                                                             # Load word from storage.
[     101] [0x0000008a] PUSH1           0x01                                                                                              # Place 1 byte item on stack.
[     102] [0x0000008c] DUP2                                                                                                              # Duplicate 2nd stack item.
[     103] [0x0000008d] PUSH1           0x01                                                                                              # Place 1 byte item on stack.
[     104] [0x0000008f] AND                                                                                                               # Bitwise AND operation.
[     105] [0x00000090] ISZERO                                                                                                            # Simple not operator
[     106] [0x00000091] PUSH2           0x0100                                                                                            # Place 2-byte item on stack.
[     107] [0x00000094] MUL                                                                                                               # Multiplication operation.
[     108] [0x00000095] SUB                                                                                                               # Subtraction operation.
[     109] [0x00000096] AND                                                                                                               # Bitwise AND operation.
[     110] [0x00000097] PUSH1           0x02                                                                                              # Place 1 byte item on stack.
[     111] [0x00000099] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     112] [0x0000009a] DIV                                                                                                               # Integer division operation.
[     113] [0x0000009b] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     114] [0x0000009c] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     115] [0x0000009e] MSTORE                                                                                                            # Save word to memory.
[     116] [0x0000009f] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     117] [0x000000a1] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     118] [0x000000a3] SHA3                                                                                                              # Compute Keccak-256 hash.
[     119] [0x000000a4] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     120] [0x000000a5] PUSH1           0x1f                                                                                              # Place 1 byte item on stack.
[     121] [0x000000a7] ADD                                                                                                               # Addition operation.
[     122] [0x000000a8] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     123] [0x000000aa] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     124] [0x000000ab] DIV                                                                                                               # Integer division operation.
[     125] [0x000000ac] DUP2                                                                                                              # Duplicate 2nd stack item.
[     126] [0x000000ad] ADD                                                                                                               # Addition operation.
[     127] [0x000000ae] SWAP3                                                                                                             # Exchange 1st and 4th stack items.
[     128] [0x000000af] DUP3                                                                                                              # Duplicate 3rd stack item.
[     129] [0x000000b0] PUSH1           0x1f                                                                                              # Place 1 byte item on stack.
[     130] [0x000000b2] LT                                                                                                                # Lesser-than comparison
[     131] [0x000000b3] PUSH2           0x01a0                                                                                            # Place 2-byte item on stack.
[     132] [0x000000b6] JUMPI           @0x1a0                                                                                            # Conditionally alter the program counter.
[     133] [0x000000b7] DUP1                                                                                                              # Duplicate 1st stack item.
[     134] [0x000000b8] MLOAD                                                                                                             # Load word from memory.
[     135] [0x000000b9] PUSH1           0xff                                                               JUMP@0xdd                      # Place 1 byte item on stack.
[     136] [0x000000bb] NOT                                                                                                               # Bitwise NOT operation.
[     137] [0x000000bc] AND                                                                                                               # Bitwise AND operation.
[     138] [0x000000bd] DUP4                                                                                                              # Duplicate 4th stack item.
[     139] [0x000000be] DUP1                                                                                                              # Duplicate 1st stack item.
[     140] [0x000000bf] ADD                                                                                                               # Addition operation.
[     141] [0x000000c0] OR                                                                                                                # Bitwise OR operation.
[     142] [0x000000c1] DUP6                                                                                                              # Duplicate 6th stack item.
[     143] [0x000000c2] SSTORE                                                                                                            # Save word to storage.
[     144] [0x000000c3] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     145] [0x000000c4] POP                                                                                                               # Remove item from stack.
[     146] [0x000000c5] PUSH2           0x019b                                                                                            # Place 2-byte item on stack.
[     147] [0x000000c8] SWAP3                                                                                                             # Exchange 1st and 4th stack items.
[     148] [0x000000c9] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     149] [0x000000ca] POP                                                                                                               # Remove item from stack.
[     150] [0x000000cb] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     151] [0x000000cc] DUP1                                                                               JUMPI@0x35                     # Duplicate 1st stack item.
[     152] [0x000000cd] DUP3                                                                                                              # Duplicate 3rd stack item.
[     153] [0x000000ce] GT                                                                                                                # Greater-than comparison
[     154] [0x000000cf] ISZERO                                                                                                            # Simple not operator
[     155] [0x000000d0] PUSH2           0x01d0                                                                                            # Place 2-byte item on stack.
[     156] [0x000000d3] JUMPI           @0x1d0                                                                                            # Conditionally alter the program counter.
[     157] [0x000000d4] DUP4                                                                                                              # Duplicate 4th stack item.
[     158] [0x000000d5] DUP2                                                                                                              # Duplicate 2nd stack item.
[     159] [0x000000d6] SSTORE                                                                                                            # Save word to storage.
[     160] [0x000000d7] PUSH1           0x01                                                                                              # Place 1 byte item on stack.
[     161] [0x000000d9] ADD                                                                                                               # Addition operation.
[     162] [0x000000da] PUSH2           0x00b9                                                                                            # Place 2-byte item on stack.
[     163] [0x000000dd] JUMP            @0xb9                                                                                             # Alter the program counter.
[     164] [0x000000de] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     165] [0x000000df] PUSH2           0x012d                                                                                            # Place 2-byte item on stack.
[     166] [0x000000e2] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     167] [0x000000e4] PUSH1           0x60 ('`')                                                                                        # Place 1 byte item on stack.
[     168] [0x000000e6] DUP2                                                                                                              # Duplicate 2nd stack item.
[     169] [0x000000e7] DUP2                                                                                                              # Duplicate 2nd stack item.
[     170] [0x000000e8] MSTORE                                                                                                            # Save word to memory.
[     171] [0x000000e9] DUP2                                                                                                              # Duplicate 2nd stack item.
[     172] [0x000000ea] SLOAD                                                                                                             # Load word from storage.
[     173] [0x000000eb] PUSH1           0xa0                                                                                              # Place 1 byte item on stack.
[     174] [0x000000ed] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     175] [0x000000ef] PUSH1           0x1f                                                                                              # Place 1 byte item on stack.
[     176] [0x000000f1] PUSH1           0x02                                                                                              # Place 1 byte item on stack.
[     177] [0x000000f3] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     178] [0x000000f5] NOT                                                                                                               # Bitwise NOT operation.
[     179] [0x000000f6] PUSH2           0x0100                                                                                            # Place 2-byte item on stack.
[     180] [0x000000f9] PUSH1           0x01                                                                                              # Place 1 byte item on stack.
[     181] [0x000000fb] DUP8                                                                                                              # Duplicate 8th stack item.
[     182] [0x000000fc] AND                                                                                                               # Bitwise AND operation.
[     183] [0x000000fd] ISZERO                                                                                                            # Simple not operator
[     184] [0x000000fe] MUL                                                                                                               # Multiplication operation.
[     185] [0x000000ff] ADD                                                                                                               # Addition operation.
[     186] [0x00000100] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     187] [0x00000101] SWAP5                                                                                                             # Exchange 1st and 6th stack items.
[     188] [0x00000102] AND                                                                                                               # Bitwise AND operation.
[     189] [0x00000103] SWAP4                                                                                                             # Exchange 1st and 5th stack items.
[     190] [0x00000104] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     191] [0x00000105] SWAP4                                                                                                             # Exchange 1st and 5th stack items.
[     192] [0x00000106] DIV                                                                                                               # Integer division operation.
[     193] [0x00000107] SWAP3                                                                                                             # Exchange 1st and 4th stack items.
[     194] [0x00000108] DUP4                                                                                                              # Duplicate 4th stack item.
[     195] [0x00000109] ADD                                                                                                               # Addition operation.
[     196] [0x0000010a] DUP2                                                                                                              # Duplicate 2nd stack item.
[     197] [0x0000010b] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     198] [0x0000010c] DIV                                                                                                               # Integer division operation.
[     199] [0x0000010d] MUL                                                                                                               # Multiplication operation.
[     200] [0x0000010e] DUP2                                                                                                              # Duplicate 2nd stack item.
[     201] [0x0000010f] ADD                                                                                                               # Addition operation.
[     202] [0x00000110] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[     203] [0x00000112] MSTORE                                                                                                            # Save word to memory.
[     204] [0x00000113] PUSH1           0x80                                                                                              # Place 1 byte item on stack.
[     205] [0x00000115] DUP3                                                                                                              # Duplicate 3rd stack item.
[     206] [0x00000116] DUP2                                                                                                              # Duplicate 2nd stack item.
[     207] [0x00000117] MSTORE                                                                                                            # Save word to memory.
[     208] [0x00000118] SWAP3                                                                                                             # Exchange 1st and 4th stack items.
[     209] [0x00000119] SWAP4                                                                                                             # Exchange 1st and 5th stack items.
[     210] [0x0000011a] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     211] [0x0000011b] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     212] [0x0000011c] DUP3                                                                                                              # Duplicate 3rd stack item.
[     213] [0x0000011d] DUP3                                                                                                              # Duplicate 3rd stack item.
[     214] [0x0000011e] DUP1                                                                                                              # Duplicate 1st stack item.
[     215] [0x0000011f] ISZERO                                                                                                            # Simple not operator
[     216] [0x00000120] PUSH2           0x01ff                                                                                            # Place 2-byte item on stack.
[     217] [0x00000123] JUMPI           @0x1ff                                                                                            # Conditionally alter the program counter.
[     218] [0x00000124] DUP1                                                                                                              # Duplicate 1st stack item.
[     219] [0x00000125] PUSH1           0x1f                                                                                              # Place 1 byte item on stack.
[     220] [0x00000127] LT                                                                                                                # Lesser-than comparison
[     221] [0x00000128] PUSH2           0x01d4                                                                                            # Place 2-byte item on stack.
[     222] [0x0000012b] JUMPI           @0x1d4                                                                                            # Conditionally alter the program counter.
[     223] [0x0000012c] PUSH2           0x0100                                                                                            # Place 2-byte item on stack.
[     224] [0x0000012f] DUP1                                                                                                              # Duplicate 1st stack item.
[     225] [0x00000130] DUP4                                                                                                              # Duplicate 4th stack item.
[     226] [0x00000131] SLOAD                                                                                                             # Load word from storage.
[     227] [0x00000132] DIV                                                                                                               # Integer division operation.
[     228] [0x00000133] MUL                                                                                                               # Multiplication operation.
[     229] [0x00000134] DUP4                                                                                                              # Duplicate 4th stack item.
[     230] [0x00000135] MSTORE                                                                                                            # Save word to memory.
[     231] [0x00000136] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     232] [0x00000137] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     233] [0x00000139] ADD                                                                                                               # Addition operation.
[     234] [0x0000013a] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     235] [0x0000013b] PUSH2           0x01ff                                                                                            # Place 2-byte item on stack.
[     236] [0x0000013e] JUMP            @0x1ff                                                                                            # Alter the program counter.
[     237] [0x0000013f] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     238] [0x00000140] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[     239] [0x00000142] MLOAD                                                                                                             # Load word from memory.
[     240] [0x00000143] DUP1                                                                                                              # Duplicate 1st stack item.
[     241] [0x00000144] DUP1                                                                                                              # Duplicate 1st stack item.
[     242] [0x00000145] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     243] [0x00000147] ADD                                                                                                               # Addition operation.
[     244] [0x00000148] DUP3                                                                                                              # Duplicate 3rd stack item.
[     245] [0x00000149] DUP2                                                                                                              # Duplicate 2nd stack item.
[     246] [0x0000014a] SUB                                                                                                               # Subtraction operation.
[     247] [0x0000014b] DUP3                                                                                                              # Duplicate 3rd stack item.
[     248] [0x0000014c] MSTORE                                                                                                            # Save word to memory.
[     249] [0x0000014d] DUP4                                                                                                              # Duplicate 4th stack item.
[     250] [0x0000014e] DUP2                                                                                                              # Duplicate 2nd stack item.
[     251] [0x0000014f] DUP2                                                                                                              # Duplicate 2nd stack item.
[     252] [0x00000150] MLOAD                                                                                                             # Load word from memory.
[     253] [0x00000151] DUP2                                                                                                              # Duplicate 2nd stack item.
[     254] [0x00000152] MSTORE                                                                                                            # Save word to memory.
[     255] [0x00000153] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     256] [0x00000155] ADD                                                                                                               # Addition operation.
[     257] [0x00000156] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     258] [0x00000157] POP                                                                                                               # Remove item from stack.
[     259] [0x00000158] DUP1                                                                                                              # Duplicate 1st stack item.
[     260] [0x00000159] MLOAD                                                                                                             # Load word from memory.
[     261] [0x0000015a] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     262] [0x0000015b] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     263] [0x0000015d] ADD                                                                                                               # Addition operation.
[     264] [0x0000015e] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     265] [0x0000015f] DUP1                                                                                                              # Duplicate 1st stack item.
[     266] [0x00000160] DUP4                                                                                                              # Duplicate 4th stack item.
[     267] [0x00000161] DUP4                                                                                                              # Duplicate 4th stack item.
[     268] [0x00000162] DUP3                                                                                                              # Duplicate 3rd stack item.
[     269] [0x00000163] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     270] [0x00000164] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     271] [0x00000166] PUSH1           0x04                                                                                              # Place 1 byte item on stack.
[     272] [0x00000168] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     273] [0x0000016a] DUP5                                                                                                              # Duplicate 5th stack item.
[     274] [0x0000016b] PUSH1           0x1f                                                                                              # Place 1 byte item on stack.
[     275] [0x0000016d] ADD                                                                                                               # Addition operation.
[     276] [0x0000016e] DIV                                                                                                               # Integer division operation.
[     277] [0x0000016f] PUSH1           0x0f                                                                                              # Place 1 byte item on stack.
[     278] [0x00000171] MUL                                                                                                               # Multiplication operation.
[     279] [0x00000172] PUSH1           0x03                                                                                              # Place 1 byte item on stack.
[     280] [0x00000174] ADD                                                                                                               # Addition operation.
[     281] [0x00000175] CALL                                                                                                              # Message-call into an account.
[     282] [0x00000176] POP                                                                                                               # Remove item from stack.
[     283] [0x00000177] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     284] [0x00000178] POP                                                                                                               # Remove item from stack.
[     285] [0x00000179] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     286] [0x0000017a] DUP2                                                                                                              # Duplicate 2nd stack item.
[     287] [0x0000017b] ADD                                                                                                               # Addition operation.
[     288] [0x0000017c] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     289] [0x0000017d] PUSH1           0x1f                                                                                              # Place 1 byte item on stack.
[     290] [0x0000017f] AND                                                                                                               # Bitwise AND operation.
[     291] [0x00000180] DUP1                                                                                                              # Duplicate 1st stack item.
[     292] [0x00000181] ISZERO                                                                                                            # Simple not operator
[     293] [0x00000182] PUSH2           0x018d                                                                                            # Place 2-byte item on stack.
[     294] [0x00000185] JUMPI           @0x18d                                                                                            # Conditionally alter the program counter.
[     295] [0x00000186] DUP1                                                                                                              # Duplicate 1st stack item.
[     296] [0x00000187] DUP3                                                                                                              # Duplicate 3rd stack item.
[     297] [0x00000188] SUB                                                                                                               # Subtraction operation.
[     298] [0x00000189] DUP1                                                                                                              # Duplicate 1st stack item.
[     299] [0x0000018a] MLOAD                                                                                                             # Load word from memory.
[     300] [0x0000018b] PUSH1           0x01                                                                                              # Place 1 byte item on stack.
[     301] [0x0000018d] DUP4                                                                               JUMPI@0x185                    # Duplicate 4th stack item.
[     302] [0x0000018e] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     303] [0x00000190] SUB                                                                                                               # Subtraction operation.
[     304] [0x00000191] PUSH2           0x0100                                                                                            # Place 2-byte item on stack.
[     305] [0x00000194] EXP                                                                                                               # Exponential operation.
[     306] [0x00000195] SUB                                                                                                               # Subtraction operation.
[     307] [0x00000196] NOT                                                                                                               # Bitwise NOT operation.
[     308] [0x00000197] AND                                                                                                               # Bitwise AND operation.
[     309] [0x00000198] DUP2                                                                                                              # Duplicate 2nd stack item.
[     310] [0x00000199] MSTORE                                                                                                            # Save word to memory.
[     311] [0x0000019a] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     312] [0x0000019c] ADD                                                                                                               # Addition operation.
[     313] [0x0000019d] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     314] [0x0000019e] POP                                                                                                               # Remove item from stack.
[     315] [0x0000019f] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     316] [0x000001a0] POP                                                                                JUMPI@0xb6                     # Remove item from stack.
[     317] [0x000001a1] SWAP3                                                                                                             # Exchange 1st and 4th stack items.
[     318] [0x000001a2] POP                                                                                                               # Remove item from stack.
[     319] [0x000001a3] POP                                                                                                               # Remove item from stack.
[     320] [0x000001a4] POP                                                                                                               # Remove item from stack.
[     321] [0x000001a5] PUSH1           0x40 ('@')                                                                                        # Place 1 byte item on stack.
[     322] [0x000001a7] MLOAD                                                                                                             # Load word from memory.
[     323] [0x000001a8] DUP1                                                                                                              # Duplicate 1st stack item.
[     324] [0x000001a9] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     325] [0x000001aa] SUB                                                                                                               # Subtraction operation.
[     326] [0x000001ab] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     327] [0x000001ac] RETURN                                                                                                            # Halt execution returning output data.
[     328] [0x000001ad] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     329] [0x000001ae] POP                                                                                                               # Remove item from stack.
[     330] [0x000001af] POP                                                                                                               # Remove item from stack.
[     331] [0x000001b0] POP                                                                                                               # Remove item from stack.
[     332] [0x000001b1] JUMP                                                                                                              # Alter the program counter.
[     333] [0x000001b2] JUMPDEST                                                                           JUMP@0x1e1                     # Mark a valid destination for jumps.
[     334] [0x000001b3] DUP3                                                                                                              # Duplicate 3rd stack item.
[     335] [0x000001b4] DUP1                                                                                                              # Duplicate 1st stack item.
[     336] [0x000001b5] ADD                                                                                                               # Addition operation.
[     337] [0x000001b6] PUSH1           0x01                                                                                              # Place 1 byte item on stack.
[     338] [0x000001b8] ADD                                                                                                               # Addition operation.
[     339] [0x000001b9] DUP6                                                                                                              # Duplicate 6th stack item.
[     340] [0x000001ba] SSTORE                                                                                                            # Save word to storage.
[     341] [0x000001bb] DUP3                                                                                                              # Duplicate 3rd stack item.
[     342] [0x000001bc] ISZERO                                                                                                            # Simple not operator
[     343] [0x000001bd] PUSH2           0x00b1                                                                                            # Place 2-byte item on stack.
[     344] [0x000001c0] JUMPI           @0xb1                                                                                             # Conditionally alter the program counter.
[     345] [0x000001c1] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     346] [0x000001c2] DUP3                                                                                                              # Duplicate 3rd stack item.
[     347] [0x000001c3] ADD                                                                                                               # Addition operation.
[     348] [0x000001c4] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     349] [0x000001c5] DUP3                                                                                                              # Duplicate 3rd stack item.
[     350] [0x000001c6] DUP2                                                                                                              # Duplicate 2nd stack item.
[     351] [0x000001c7] GT                                                                                                                # Greater-than comparison
[     352] [0x000001c8] ISZERO                                                                                                            # Simple not operator
[     353] [0x000001c9] PUSH2           0x00b1                                                                                            # Place 2-byte item on stack.
[     354] [0x000001cc] JUMPI           @0xb1                                                                                             # Conditionally alter the program counter.
[     355] [0x000001cd] DUP3                                                                                                              # Duplicate 3rd stack item.
[     356] [0x000001ce] MLOAD                                                                                                             # Load word from memory.
[     357] [0x000001cf] DUP3                                                                                                              # Duplicate 3rd stack item.
[     358] [0x000001d0] PUSH1           0x00                                                               JUMPI@0xd3                     # Place 1 byte item on stack.
[     359] [0x000001d2] POP                                                                                                               # Remove item from stack.
[     360] [0x000001d3] SSTORE                                                                                                            # Save word to storage.
[     361] [0x000001d4] SWAP2                                                                              JUMPI@0x12b                    # Exchange 1st and 3rd stack items.
[     362] [0x000001d5] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     363] [0x000001d7] ADD                                                                                                               # Addition operation.
[     364] [0x000001d8] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     365] [0x000001d9] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     366] [0x000001da] PUSH1           0x01                                                                                              # Place 1 byte item on stack.
[     367] [0x000001dc] ADD                                                                                                               # Addition operation.
[     368] [0x000001dd] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     369] [0x000001de] PUSH2           0x01b2                                                                                            # Place 2-byte item on stack.
[     370] [0x000001e1] JUMP            @0x1b2                                                                                            # Alter the program counter.
[     371] [0x000001e2] JUMPDEST                                                                           JUMPI@0x207                    # Mark a valid destination for jumps.
[     372] [0x000001e3] POP                                                                                                               # Remove item from stack.
[     373] [0x000001e4] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     374] [0x000001e5] JUMP                                                                                                              # Alter the program counter.
[     375] [0x000001e6] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     376] [0x000001e7] DUP3                                                                                                              # Duplicate 3rd stack item.
[     377] [0x000001e8] ADD                                                                                                               # Addition operation.
[     378] [0x000001e9] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     379] [0x000001ea] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     380] [0x000001eb] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     381] [0x000001ed] MSTORE                                                                                                            # Save word to memory.
[     382] [0x000001ee] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     383] [0x000001f0] PUSH1           0x00                                                                                              # Place 1 byte item on stack.
[     384] [0x000001f2] SHA3                                                                                                              # Compute Keccak-256 hash.
[     385] [0x000001f3] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     386] [0x000001f4] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     387] [0x000001f5] DUP2                                                                                                              # Duplicate 2nd stack item.
[     388] [0x000001f6] SLOAD                                                                                                             # Load word from storage.
[     389] [0x000001f7] DUP2                                                                                                              # Duplicate 2nd stack item.
[     390] [0x000001f8] MSTORE                                                                                                            # Save word to memory.
[     391] [0x000001f9] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     392] [0x000001fa] PUSH1           0x01                                                                                              # Place 1 byte item on stack.
[     393] [0x000001fc] ADD                                                                                                               # Addition operation.
[     394] [0x000001fd] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     395] [0x000001fe] PUSH1           0x20                                                                                              # Place 1 byte item on stack.
[     396] [0x00000200] ADD                                                                                                               # Addition operation.
[     397] [0x00000201] DUP1                                                                                                              # Duplicate 1st stack item.
[     398] [0x00000202] DUP4                                                                                                              # Duplicate 4th stack item.
[     399] [0x00000203] GT                                                                                                                # Greater-than comparison
[     400] [0x00000204] PUSH2           0x01e2                                                                                            # Place 2-byte item on stack.
[     401] [0x00000207] JUMPI           @0x1e2                                                                                            # Conditionally alter the program counter.
[     402] [0x00000208] DUP3                                                                                                              # Duplicate 3rd stack item.
[     403] [0x00000209] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     404] [0x0000020a] SUB                                                                                                               # Subtraction operation.
[     405] [0x0000020b] PUSH1           0x1f                                                                                              # Place 1 byte item on stack.
[     406] [0x0000020d] AND                                                                                                               # Bitwise AND operation.
[     407] [0x0000020e] DUP3                                                                                                              # Duplicate 3rd stack item.
[     408] [0x0000020f] ADD                                                                                                               # Addition operation.
[     409] [0x00000210] SWAP2                                                                                                             # Exchange 1st and 3rd stack items.
[     410] [0x00000211] JUMPDEST                                                                                                          # Mark a valid destination for jumps.
[     411] [0x00000212] POP                                                                                                               # Remove item from stack.
[     412] [0x00000213] POP                                                                                                               # Remove item from stack.
[     413] [0x00000214] POP                                                                                                               # Remove item from stack.
[     414] [0x00000215] POP                                                                                                               # Remove item from stack.
[     415] [0x00000216] POP                                                                                                               # Remove item from stack.
[     416] [0x00000217] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     417] [0x00000218] POP                                                                                                               # Remove item from stack.
[     418] [0x00000219] SWAP1                                                                                                             # Exchange 1st and 2nd stack items.
[     419] [0x0000021a] JUMP                                                                                                              # Alter the program counter.
assemble(disassemble(evmcode))== True

```

* via stdin
```python
#> echo "0x12345678" | python ethereum_dasm
 Instr.#   pos. mnemonic        operand                   description
------------------------------------------------------------------------------------------------------------------------
WARNING - skipping invalid byte: '0x'
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
WARNING - skipping invalid byte: '0x'
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
WARNING - finished in 0.016 seconds.

```

* evmcode with invalid opcodes like https://etherscan.io/address/0x4432979c7c6bdd19f9ef20787c4ac9cc9710667b#code
```python
#> python ethereum_dasm contract_0x4432979c7c6bdd19f9ef20787c4ac9cc9710667b.evm
...
[  1345]   1943 PUSH22          0xcd3aa3bb5acec2575a0e9e593c00f959f8c92f12db28                     # Place 22-byte item on stack.
[  1346]   1966 PUSH10          0xc3395a3b0502d05e2516                                             # Place 10-byte item on stack.
[  1347]   1977 DIFFICULTY                                                                         # Get the blockΓÇÖs difficulty.
[  1348]   1978 PUSH16          0x71f85b8a35acfbc15ff81a39ae7d344f                                 # Place 16-byte item on stack.
[  1349]   1995 UNKNOWN_0xd7                                                                       # error: byte at position 1995 (0xd7) is not a valid operator; KeyError(215,)
[  1350]   1996 MULMOD                                                                             # Modulo
[  1351]   1997 CALLCODE                                                                           # Message-call into this account with alternative accountΓÇÖs code.
[  1352]   1998 DUP15                                                                              # Duplicate 15th stack item.
[  1353]   1999 DUP7                                                                               # Duplicate 7th stack item.
[  1354]   2000 STOP                                                                               # Halts execution.
[  1355]   2001 UNKNOWN_0xb4                                                                       # error: byte at position 2001 (0xb4) is not a valid operator; KeyError(180,)
[  1356]   2002 UNKNOWN_0xaa                                                                       # error: byte at position 2002 (0xaa) is not a valid operator; KeyError(170,)
[  1357]   2003 DUP13                                                                              # Duplicate 13th stack item.
[  1358]   2004 PUSH6           0xc6b64bfe7fe3                                                     # Place 6-byte item on stack.
[  1359]   2011 PUSH12          0xd19b                                                             # Place 12-byte item on stack.
WARNING - disassembly finished with 12 errors
```
