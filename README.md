# ethereum-dasm 
ethereum evm bytecode disassembler

[https://github.com/ethereum/] [https://www.ethereum.org/]

**disassembles evm bytecode**

## install

```#> python -m pip install ethereum-dasm
#>python -m ethereum_dasm -a 0x44919b8026f38d70437a8eb3be47b06ab1c3e4bf```

## usage

* provide the path to the ethereum vm bytecode or the bytecode as an argument to evmdasm. Tries to read from stdin by default.
* returns !=0 on errors
* use option `-L` to switch from table to listing mode
* invalid opcodes are prefixed with `UNKNOWN_`
* basic jump/xref analysis
* basicblocking
* online function signature lookup and operand annotations

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

```
    #> echo "0x12345678" | python evmdasm.py
    #> python evmdasm.py -v critical "0x12345678"
    #> python evmdasm.py -v critical ether_contract.evm
    #> python evmdasm.py -a <contract address>


## examples

* disasm with basic jumptable analysis (incomplete)
```python
#> python evmdasm.py -f 0x6080604052600436106100ba576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806316243356146100bf57806338af3eed146100ea5780636e15266a14610141578063834ee4171461016c57806386d1a69f146101975780638da5cb5b146101ae5780639b7faaf0146102055780639e1a4d1914610234578063a4e2d6341461025f578063f2fde38b1461028e578063f83d08ba146102d1578063fa2a899714610300575b600080fd5b3480156100cb57600080fd5b506100d461032f565b6040518082815260200191505060405180910390f35b3480156100f657600080fd5b506100ff610335565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561014d57600080fd5b5061015661035b565b6040518082815260200191505060405180910390f35b34801561017857600080fd5b50610181610361565b6040518082815260200191505060405180910390f35b3480156101a357600080fd5b506101ac610367565b005b3480156101ba57600080fd5b506101c36105e6565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561021157600080fd5b5061021a61060b565b604051808215151515815260200191505060405180910390f35b34801561024057600080fd5b5061024961061c565b6040518082815260200191505060405180910390f35b34801561026b57600080fd5b5061027461071b565b604051808215151515815260200191505060405180910390f35b34801561029a57600080fd5b506102cf600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061072e565b005b3480156102dd57600080fd5b506102e6610883565b604051808215151515815260200191505060405180910390f35b34801561030c57600080fd5b50610315610954565b604051808215151515815260200191505060405180910390f35b60045481565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60055481565b60035481565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156103c457600080fd5b600260149054906101000a900460ff1615156103df57600080fd5b600260159054906101000a900460ff161515156103fb57600080fd5b61040361060b565b151561040e57600080fd5b61041661061c565b9050600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16836040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050602060405180830381600087803b1580156104ff57600080fd5b505af1158015610513573d6000803e3d6000fd5b505050506040513d602081101561052957600080fd5b8101908080519060200190929190505050507f9cf9e3ab58b33f06d81842ea0ad850b6640c6430d6396973312e1715792e7a91600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1682604051808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018281526020019250505060405180910390a16001600260156101000a81548160ff02191690831515021790555050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600080429050600454811191505090565b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166370a08231306040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001915050602060405180830381600087803b1580156106db57600080fd5b505af11580156106ef573d6000803e3d6000fd5b505050506040513d602081101561070557600080fd5b8101908080519060200190929190505050905090565b600260149054906101000a900460ff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561078957600080fd5b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141515156107c557600080fd5b8073ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a3806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156108e057600080fd5b600260149054906101000a900460ff161515156108fc57600080fd5b600061090661061c565b11151561091257600080fd5b4260038190555061093060055460035461096790919063ffffffff16565b6004819055506001600260146101000a81548160ff02191690831515021790555090565b600260159054906101000a900460ff1681565b600080828401905083811015151561097b57fe5b80915050929150505600a165627a7a7230582069642cdfbf8b49cb944b12328add2c81c3557600ed88f94b907c0d547a6251db0029

Inst addr  hex   mnemonic        operand                              xrefs                          description
------------------------------------------------------------------------------------------------------------------------------------------------------
   0 [  0 0x000] PUSH1           0x80                                                                # Place 1 byte item on stack.
   1 [  2 0x002] PUSH1           0x40                                                                # Place 1 byte item on stack.
   2 [  4 0x004] MSTORE                                                                              # Save word to memory.
   3 [  5 0x005] PUSH1           0x04                                                                # Place 1 byte item on stack.
   4 [  7 0x007] CALLDATASIZE                                                                        # Get size of input data in current environment.
   5 [  8 0x008] LT                                                                                  # Lesser-than comparison
   6 [  9 0x009] PUSH2           0x00ba                                                              # Place 2-byte item on stack.
   7 [ 12 0x00c] JUMPI           @0xba                                                               # Conditionally alter the program counter.

   8 [ 13 0x00d] PUSH1           0x00                                                                # Place 1 byte item on stack.
   9 [ 15 0x00f] CALLDATALOAD                                                                        # Get input data of current environment.
  10 [ 16 0x010] PUSH29          0x0100000000000000000000000000000000000000000000000000000000                                # Place 29-byte item on stack.
  11 [ 46 0x02e] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  12 [ 47 0x02f] DIV                                                                                 # Integer division operation.
  13 [ 48 0x030] PUSH4           0xffffffff                                                          # Place 4-byte item on stack.
  14 [ 53 0x035] AND                                                                                 # Bitwise AND operation.
  15 [ 54 0x036] DUP1                                                                                # Duplicate 1st stack item.
  16 [ 55 0x037] PUSH4           0x16243356                                                          # Place 4-byte item on stack.
  17 [ 60 0x03c] EQ                                                                                  # Equality  comparison
  18 [ 61 0x03d] PUSH2           0x00bf                                                              # Place 2-byte item on stack.
  19 [ 64 0x040] JUMPI           @0xbf                                                               # Conditionally alter the program counter.

  20 [ 65 0x041] DUP1                                                                                # Duplicate 1st stack item.
  21 [ 66 0x042] PUSH4           0x38af3eed  ('function beneficiary()')                                # Place 4-byte item on stack.
  22 [ 71 0x047] EQ                                                                                  # Equality  comparison
  23 [ 72 0x048] PUSH2           0x00ea                                                              # Place 2-byte item on stack.
  24 [ 75 0x04b] JUMPI           @0xea                                                               # Conditionally alter the program counter.

  25 [ 76 0x04c] DUP1                                                                                # Duplicate 1st stack item.
  26 [ 77 0x04d] PUSH4           0x6e15266a                                                          # Place 4-byte item on stack.
  27 [ 82 0x052] EQ                                                                                  # Equality  comparison
  28 [ 83 0x053] PUSH2           0x0141                                                              # Place 2-byte item on stack.
  29 [ 86 0x056] JUMPI           @0x141                                                              # Conditionally alter the program counter.

  30 [ 87 0x057] DUP1                                                                                # Duplicate 1st stack item.
  31 [ 88 0x058] PUSH4           0x834ee417                                                          # Place 4-byte item on stack.
  32 [ 93 0x05d] EQ                                                                                  # Equality  comparison
  33 [ 94 0x05e] PUSH2           0x016c                                                              # Place 2-byte item on stack.
  34 [ 97 0x061] JUMPI           @0x16c                                                              # Conditionally alter the program counter.

  35 [ 98 0x062] DUP1                                                                                # Duplicate 1st stack item.
  36 [ 99 0x063] PUSH4           0x86d1a69f  ('function release()')                                  # Place 4-byte item on stack.
  37 [104 0x068] EQ                                                                                  # Equality  comparison
  38 [105 0x069] PUSH2           0x0197                                                              # Place 2-byte item on stack.
  39 [108 0x06c] JUMPI           @0x197                                                              # Conditionally alter the program counter.

  40 [109 0x06d] DUP1                                                                                # Duplicate 1st stack item.
  41 [110 0x06e] PUSH4           0x8da5cb5b  (*ambiguous* 'function ideal_warn_timed(uint256,uint128)')                                # Place 4-byte item on stack.
  42 [115 0x073] EQ                                                                                  # Equality  comparison
  43 [116 0x074] PUSH2           0x01ae                                                              # Place 2-byte item on stack.
  44 [119 0x077] JUMPI           @0x1ae                                                              # Conditionally alter the program counter.

  45 [120 0x078] DUP1                                                                                # Duplicate 1st stack item.
  46 [121 0x079] PUSH4           0x9b7faaf0  ('function lockOver()')                                 # Place 4-byte item on stack.
  47 [126 0x07e] EQ                                                                                  # Equality  comparison
  48 [127 0x07f] PUSH2           0x0205                                                              # Place 2-byte item on stack.
  49 [130 0x082] JUMPI           @0x205                                                              # Conditionally alter the program counter.

  50 [131 0x083] DUP1                                                                                # Duplicate 1st stack item.
  51 [132 0x084] PUSH4           0x9e1a4d19  ('function tokenBalance()')                                # Place 4-byte item on stack.
  52 [137 0x089] EQ                                                                                  # Equality  comparison
  53 [138 0x08a] PUSH2           0x0234                                                              # Place 2-byte item on stack.
  54 [141 0x08d] JUMPI           @0x234                                                              # Conditionally alter the program counter.

  55 [142 0x08e] DUP1                                                                                # Duplicate 1st stack item.
  56 [143 0x08f] PUSH4           0xa4e2d634  ('function isLocked()')                                 # Place 4-byte item on stack.
  57 [148 0x094] EQ                                                                                  # Equality  comparison
  58 [149 0x095] PUSH2           0x025f                                                              # Place 2-byte item on stack.
  59 [152 0x098] JUMPI           @0x25f                                                              # Conditionally alter the program counter.

  60 [153 0x099] DUP1                                                                                # Duplicate 1st stack item.
  61 [154 0x09a] PUSH4           0xf2fde38b  ('function transferOwnership(address)')                                # Place 4-byte item on stack.
  62 [159 0x09f] EQ                                                                                  # Equality  comparison
  63 [160 0x0a0] PUSH2           0x028e                                                              # Place 2-byte item on stack.
  64 [163 0x0a3] JUMPI           @0x28e                                                              # Conditionally alter the program counter.

  65 [164 0x0a4] DUP1                                                                                # Duplicate 1st stack item.
  66 [165 0x0a5] PUSH4           0xf83d08ba  ('function lock()')                                     # Place 4-byte item on stack.
  67 [170 0x0aa] EQ                                                                                  # Equality  comparison
  68 [171 0x0ab] PUSH2           0x02d1                                                              # Place 2-byte item on stack.
  69 [174 0x0ae] JUMPI           @0x2d1                                                              # Conditionally alter the program counter.

  70 [175 0x0af] DUP1                                                                                # Duplicate 1st stack item.
  71 [176 0x0b0] PUSH4           0xfa2a8997                                                          # Place 4-byte item on stack.
  72 [181 0x0b5] EQ                                                                                  # Equality  comparison
  73 [182 0x0b6] PUSH2           0x0300                                                              # Place 2-byte item on stack.
  74 [185 0x0b9] JUMPI           @0x300                                                              # Conditionally alter the program counter.

:loc_0xba
  75 [186 0x0ba] JUMPDEST                                             JUMPI@0xc                      # Mark a valid destination for jumps.
  76 [187 0x0bb] PUSH1           0x00                                                                # Place 1 byte item on stack.
  77 [189 0x0bd] DUP1                                                                                # Duplicate 1st stack item.
  78 [190 0x0be] REVERT                                                                              # throw an error
:loc_0xbf
  79 [191 0x0bf] JUMPDEST                                             JUMPI@0x40                     # Mark a valid destination for jumps.
  80 [192 0x0c0] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
  81 [193 0x0c1] DUP1                                                                                # Duplicate 1st stack item.
  82 [194 0x0c2] ISZERO                                                                              # Simple not operator
  83 [195 0x0c3] PUSH2           0x00cb                                                              # Place 2-byte item on stack.
  84 [198 0x0c6] JUMPI           @0xcb                                                               # Conditionally alter the program counter.

  85 [199 0x0c7] PUSH1           0x00                                                                # Place 1 byte item on stack.
  86 [201 0x0c9] DUP1                                                                                # Duplicate 1st stack item.
  87 [202 0x0ca] REVERT                                                                              # throw an error
:loc_0xcb
  88 [203 0x0cb] JUMPDEST                                             JUMPI@0xc6                     # Mark a valid destination for jumps.
  89 [204 0x0cc] POP                                                                                 # Remove item from stack.
  90 [205 0x0cd] PUSH2           0x00d4                                                              # Place 2-byte item on stack.
  91 [208 0x0d0] PUSH2           0x032f                                                              # Place 2-byte item on stack.
  92 [211 0x0d3] JUMP            @0x32f                                                              # Alter the program counter.

:loc_0xd4
  93 [212 0x0d4] JUMPDEST                                                                            # Mark a valid destination for jumps.
  94 [213 0x0d5] PUSH1           0x40                                                                # Place 1 byte item on stack.
  95 [215 0x0d7] MLOAD                                                                               # Load word from memory.
  96 [216 0x0d8] DUP1                                                                                # Duplicate 1st stack item.
  97 [217 0x0d9] DUP3                                                                                # Duplicate 3rd stack item.
  98 [218 0x0da] DUP2                                                                                # Duplicate 2nd stack item.
  99 [219 0x0db] MSTORE                                                                              # Save word to memory.
 100 [220 0x0dc] PUSH1           0x20                                                                # Place 1 byte item on stack.
 101 [222 0x0de] ADD                                                                                 # Addition operation.
 102 [223 0x0df] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 103 [224 0x0e0] POP                                                                                 # Remove item from stack.
 104 [225 0x0e1] POP                                                                                 # Remove item from stack.
 105 [226 0x0e2] PUSH1           0x40                                                                # Place 1 byte item on stack.
 106 [228 0x0e4] MLOAD                                                                               # Load word from memory.
 107 [229 0x0e5] DUP1                                                                                # Duplicate 1st stack item.
 108 [230 0x0e6] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 109 [231 0x0e7] SUB                                                                                 # Subtraction operation.
 110 [232 0x0e8] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 111 [233 0x0e9] RETURN                                                                              # Halt execution returning output data.

:loc_0xea
 112 [234 0x0ea] JUMPDEST                                             JUMPI@0x4b                     # Mark a valid destination for jumps.
 113 [235 0x0eb] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 114 [236 0x0ec] DUP1                                                                                # Duplicate 1st stack item.
 115 [237 0x0ed] ISZERO                                                                              # Simple not operator
 116 [238 0x0ee] PUSH2           0x00f6                                                              # Place 2-byte item on stack.
 117 [241 0x0f1] JUMPI           @0xf6                                                               # Conditionally alter the program counter.

 118 [242 0x0f2] PUSH1           0x00                                                                # Place 1 byte item on stack.
 119 [244 0x0f4] DUP1                                                                                # Duplicate 1st stack item.
 120 [245 0x0f5] REVERT                                                                              # throw an error
:loc_0xf6
 121 [246 0x0f6] JUMPDEST                                             JUMPI@0xf1                     # Mark a valid destination for jumps.
 122 [247 0x0f7] POP                                                                                 # Remove item from stack.
 123 [248 0x0f8] PUSH2           0x00ff                                                              # Place 2-byte item on stack.
 124 [251 0x0fb] PUSH2           0x0335                                                              # Place 2-byte item on stack.
 125 [254 0x0fe] JUMP            @0x335                                                              # Alter the program counter.

:loc_0xff
 126 [255 0x0ff] JUMPDEST                                                                            # Mark a valid destination for jumps.
 127 [256 0x100] PUSH1           0x40                                                                # Place 1 byte item on stack.
 128 [258 0x102] MLOAD                                                                               # Load word from memory.
 129 [259 0x103] DUP1                                                                                # Duplicate 1st stack item.
 130 [260 0x104] DUP3                                                                                # Duplicate 3rd stack item.
 131 [261 0x105] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 132 [282 0x11a] AND                                                                                 # Bitwise AND operation.
 133 [283 0x11b] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 134 [304 0x130] AND                                                                                 # Bitwise AND operation.
 135 [305 0x131] DUP2                                                                                # Duplicate 2nd stack item.
 136 [306 0x132] MSTORE                                                                              # Save word to memory.
 137 [307 0x133] PUSH1           0x20                                                                # Place 1 byte item on stack.
 138 [309 0x135] ADD                                                                                 # Addition operation.
 139 [310 0x136] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 140 [311 0x137] POP                                                                                 # Remove item from stack.
 141 [312 0x138] POP                                                                                 # Remove item from stack.
 142 [313 0x139] PUSH1           0x40                                                                # Place 1 byte item on stack.
 143 [315 0x13b] MLOAD                                                                               # Load word from memory.
 144 [316 0x13c] DUP1                                                                                # Duplicate 1st stack item.
 145 [317 0x13d] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 146 [318 0x13e] SUB                                                                                 # Subtraction operation.
 147 [319 0x13f] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 148 [320 0x140] RETURN                                                                              # Halt execution returning output data.

:loc_0x141
 149 [321 0x141] JUMPDEST                                             JUMPI@0x56                     # Mark a valid destination for jumps.
 150 [322 0x142] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 151 [323 0x143] DUP1                                                                                # Duplicate 1st stack item.
 152 [324 0x144] ISZERO                                                                              # Simple not operator
 153 [325 0x145] PUSH2           0x014d                                                              # Place 2-byte item on stack.
 154 [328 0x148] JUMPI           @0x14d                                                              # Conditionally alter the program counter.

 155 [329 0x149] PUSH1           0x00                                                                # Place 1 byte item on stack.
 156 [331 0x14b] DUP1                                                                                # Duplicate 1st stack item.
 157 [332 0x14c] REVERT                                                                              # throw an error
:loc_0x14d
 158 [333 0x14d] JUMPDEST                                             JUMPI@0x148                    # Mark a valid destination for jumps.
 159 [334 0x14e] POP                                                                                 # Remove item from stack.
 160 [335 0x14f] PUSH2           0x0156                                                              # Place 2-byte item on stack.
 161 [338 0x152] PUSH2           0x035b                                                              # Place 2-byte item on stack.
 162 [341 0x155] JUMP            @0x35b                                                              # Alter the program counter.

:loc_0x156
 163 [342 0x156] JUMPDEST                                                                            # Mark a valid destination for jumps.
 164 [343 0x157] PUSH1           0x40                                                                # Place 1 byte item on stack.
 165 [345 0x159] MLOAD                                                                               # Load word from memory.
 166 [346 0x15a] DUP1                                                                                # Duplicate 1st stack item.
 167 [347 0x15b] DUP3                                                                                # Duplicate 3rd stack item.
 168 [348 0x15c] DUP2                                                                                # Duplicate 2nd stack item.
 169 [349 0x15d] MSTORE                                                                              # Save word to memory.
 170 [350 0x15e] PUSH1           0x20                                                                # Place 1 byte item on stack.
 171 [352 0x160] ADD                                                                                 # Addition operation.
 172 [353 0x161] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 173 [354 0x162] POP                                                                                 # Remove item from stack.
 174 [355 0x163] POP                                                                                 # Remove item from stack.
 175 [356 0x164] PUSH1           0x40                                                                # Place 1 byte item on stack.
 176 [358 0x166] MLOAD                                                                               # Load word from memory.
 177 [359 0x167] DUP1                                                                                # Duplicate 1st stack item.
 178 [360 0x168] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 179 [361 0x169] SUB                                                                                 # Subtraction operation.
 180 [362 0x16a] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 181 [363 0x16b] RETURN                                                                              # Halt execution returning output data.

:loc_0x16c
 182 [364 0x16c] JUMPDEST                                             JUMPI@0x61                     # Mark a valid destination for jumps.
 183 [365 0x16d] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 184 [366 0x16e] DUP1                                                                                # Duplicate 1st stack item.
 185 [367 0x16f] ISZERO                                                                              # Simple not operator
 186 [368 0x170] PUSH2           0x0178                                                              # Place 2-byte item on stack.
 187 [371 0x173] JUMPI           @0x178                                                              # Conditionally alter the program counter.

 188 [372 0x174] PUSH1           0x00                                                                # Place 1 byte item on stack.
 189 [374 0x176] DUP1                                                                                # Duplicate 1st stack item.
 190 [375 0x177] REVERT                                                                              # throw an error
:loc_0x178
 191 [376 0x178] JUMPDEST                                             JUMPI@0x173                    # Mark a valid destination for jumps.
 192 [377 0x179] POP                                                                                 # Remove item from stack.
 193 [378 0x17a] PUSH2           0x0181                                                              # Place 2-byte item on stack.
 194 [381 0x17d] PUSH2           0x0361                                                              # Place 2-byte item on stack.
 195 [384 0x180] JUMP            @0x361                                                              # Alter the program counter.

:loc_0x181
 196 [385 0x181] JUMPDEST                                                                            # Mark a valid destination for jumps.
 197 [386 0x182] PUSH1           0x40                                                                # Place 1 byte item on stack.
 198 [388 0x184] MLOAD                                                                               # Load word from memory.
 199 [389 0x185] DUP1                                                                                # Duplicate 1st stack item.
 200 [390 0x186] DUP3                                                                                # Duplicate 3rd stack item.
 201 [391 0x187] DUP2                                                                                # Duplicate 2nd stack item.
 202 [392 0x188] MSTORE                                                                              # Save word to memory.
 203 [393 0x189] PUSH1           0x20                                                                # Place 1 byte item on stack.
 204 [395 0x18b] ADD                                                                                 # Addition operation.
 205 [396 0x18c] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 206 [397 0x18d] POP                                                                                 # Remove item from stack.
 207 [398 0x18e] POP                                                                                 # Remove item from stack.
 208 [399 0x18f] PUSH1           0x40                                                                # Place 1 byte item on stack.
 209 [401 0x191] MLOAD                                                                               # Load word from memory.
 210 [402 0x192] DUP1                                                                                # Duplicate 1st stack item.
 211 [403 0x193] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 212 [404 0x194] SUB                                                                                 # Subtraction operation.
 213 [405 0x195] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 214 [406 0x196] RETURN                                                                              # Halt execution returning output data.

:loc_0x197
 215 [407 0x197] JUMPDEST                                             JUMPI@0x6c                     # Mark a valid destination for jumps.
 216 [408 0x198] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 217 [409 0x199] DUP1                                                                                # Duplicate 1st stack item.
 218 [410 0x19a] ISZERO                                                                              # Simple not operator
 219 [411 0x19b] PUSH2           0x01a3                                                              # Place 2-byte item on stack.
 220 [414 0x19e] JUMPI           @0x1a3                                                              # Conditionally alter the program counter.

 221 [415 0x19f] PUSH1           0x00                                                                # Place 1 byte item on stack.
 222 [417 0x1a1] DUP1                                                                                # Duplicate 1st stack item.
 223 [418 0x1a2] REVERT                                                                              # throw an error
:loc_0x1a3
 224 [419 0x1a3] JUMPDEST                                             JUMPI@0x19e                    # Mark a valid destination for jumps.
 225 [420 0x1a4] POP                                                                                 # Remove item from stack.
 226 [421 0x1a5] PUSH2           0x01ac                                                              # Place 2-byte item on stack.
 227 [424 0x1a8] PUSH2           0x0367                                                              # Place 2-byte item on stack.
 228 [427 0x1ab] JUMP            @0x367                                                              # Alter the program counter.

:loc_0x1ac
 229 [428 0x1ac] JUMPDEST                                                                            # Mark a valid destination for jumps.
 230 [429 0x1ad] STOP                                                                                # Halts execution.

:loc_0x1ae
 231 [430 0x1ae] JUMPDEST                                             JUMPI@0x77                     # Mark a valid destination for jumps.
 232 [431 0x1af] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 233 [432 0x1b0] DUP1                                                                                # Duplicate 1st stack item.
 234 [433 0x1b1] ISZERO                                                                              # Simple not operator
 235 [434 0x1b2] PUSH2           0x01ba                                                              # Place 2-byte item on stack.
 236 [437 0x1b5] JUMPI           @0x1ba                                                              # Conditionally alter the program counter.

 237 [438 0x1b6] PUSH1           0x00                                                                # Place 1 byte item on stack.
 238 [440 0x1b8] DUP1                                                                                # Duplicate 1st stack item.
 239 [441 0x1b9] REVERT                                                                              # throw an error
:loc_0x1ba
 240 [442 0x1ba] JUMPDEST                                             JUMPI@0x1b5                    # Mark a valid destination for jumps.
 241 [443 0x1bb] POP                                                                                 # Remove item from stack.
 242 [444 0x1bc] PUSH2           0x01c3                                                              # Place 2-byte item on stack.
 243 [447 0x1bf] PUSH2           0x05e6                                                              # Place 2-byte item on stack.
 244 [450 0x1c2] JUMP            @0x5e6                                                              # Alter the program counter.

:loc_0x1c3
 245 [451 0x1c3] JUMPDEST                                                                            # Mark a valid destination for jumps.
 246 [452 0x1c4] PUSH1           0x40                                                                # Place 1 byte item on stack.
 247 [454 0x1c6] MLOAD                                                                               # Load word from memory.
 248 [455 0x1c7] DUP1                                                                                # Duplicate 1st stack item.
 249 [456 0x1c8] DUP3                                                                                # Duplicate 3rd stack item.
 250 [457 0x1c9] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 251 [478 0x1de] AND                                                                                 # Bitwise AND operation.
 252 [479 0x1df] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 253 [500 0x1f4] AND                                                                                 # Bitwise AND operation.
 254 [501 0x1f5] DUP2                                                                                # Duplicate 2nd stack item.
 255 [502 0x1f6] MSTORE                                                                              # Save word to memory.
 256 [503 0x1f7] PUSH1           0x20                                                                # Place 1 byte item on stack.
 257 [505 0x1f9] ADD                                                                                 # Addition operation.
 258 [506 0x1fa] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 259 [507 0x1fb] POP                                                                                 # Remove item from stack.
 260 [508 0x1fc] POP                                                                                 # Remove item from stack.
 261 [509 0x1fd] PUSH1           0x40                                                                # Place 1 byte item on stack.
 262 [511 0x1ff] MLOAD                                                                               # Load word from memory.
 263 [512 0x200] DUP1                                                                                # Duplicate 1st stack item.
 264 [513 0x201] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 265 [514 0x202] SUB                                                                                 # Subtraction operation.
 266 [515 0x203] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 267 [516 0x204] RETURN                                                                              # Halt execution returning output data.

:loc_0x205
 268 [517 0x205] JUMPDEST                                             JUMPI@0x82                     # Mark a valid destination for jumps.
 269 [518 0x206] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 270 [519 0x207] DUP1                                                                                # Duplicate 1st stack item.
 271 [520 0x208] ISZERO                                                                              # Simple not operator
 272 [521 0x209] PUSH2           0x0211                                                              # Place 2-byte item on stack.
 273 [524 0x20c] JUMPI           @0x211                                                              # Conditionally alter the program counter.

 274 [525 0x20d] PUSH1           0x00                                                                # Place 1 byte item on stack.
 275 [527 0x20f] DUP1                                                                                # Duplicate 1st stack item.
 276 [528 0x210] REVERT                                                                              # throw an error
:loc_0x211
 277 [529 0x211] JUMPDEST                                             JUMPI@0x20c                    # Mark a valid destination for jumps.
 278 [530 0x212] POP                                                                                 # Remove item from stack.
 279 [531 0x213] PUSH2           0x021a                                                              # Place 2-byte item on stack.
 280 [534 0x216] PUSH2           0x060b                                                              # Place 2-byte item on stack.
 281 [537 0x219] JUMP            @0x60b                                                              # Alter the program counter.

:loc_0x21a
 282 [538 0x21a] JUMPDEST                                                                            # Mark a valid destination for jumps.
 283 [539 0x21b] PUSH1           0x40                                                                # Place 1 byte item on stack.
 284 [541 0x21d] MLOAD                                                                               # Load word from memory.
 285 [542 0x21e] DUP1                                                                                # Duplicate 1st stack item.
 286 [543 0x21f] DUP3                                                                                # Duplicate 3rd stack item.
 287 [544 0x220] ISZERO                                                                              # Simple not operator
 288 [545 0x221] ISZERO                                                                              # Simple not operator
 289 [546 0x222] ISZERO                                                                              # Simple not operator
 290 [547 0x223] ISZERO                                                                              # Simple not operator
 291 [548 0x224] DUP2                                                                                # Duplicate 2nd stack item.
 292 [549 0x225] MSTORE                                                                              # Save word to memory.
 293 [550 0x226] PUSH1           0x20                                                                # Place 1 byte item on stack.
 294 [552 0x228] ADD                                                                                 # Addition operation.
 295 [553 0x229] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 296 [554 0x22a] POP                                                                                 # Remove item from stack.
 297 [555 0x22b] POP                                                                                 # Remove item from stack.
 298 [556 0x22c] PUSH1           0x40                                                                # Place 1 byte item on stack.
 299 [558 0x22e] MLOAD                                                                               # Load word from memory.
 300 [559 0x22f] DUP1                                                                                # Duplicate 1st stack item.
 301 [560 0x230] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 302 [561 0x231] SUB                                                                                 # Subtraction operation.
 303 [562 0x232] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 304 [563 0x233] RETURN                                                                              # Halt execution returning output data.

:loc_0x234
 305 [564 0x234] JUMPDEST                                             JUMPI@0x8d                     # Mark a valid destination for jumps.
 306 [565 0x235] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 307 [566 0x236] DUP1                                                                                # Duplicate 1st stack item.
 308 [567 0x237] ISZERO                                                                              # Simple not operator
 309 [568 0x238] PUSH2           0x0240                                                              # Place 2-byte item on stack.
 310 [571 0x23b] JUMPI           @0x240                                                              # Conditionally alter the program counter.

 311 [572 0x23c] PUSH1           0x00                                                                # Place 1 byte item on stack.
 312 [574 0x23e] DUP1                                                                                # Duplicate 1st stack item.
 313 [575 0x23f] REVERT                                                                              # throw an error
:loc_0x240
 314 [576 0x240] JUMPDEST                                             JUMPI@0x23b                    # Mark a valid destination for jumps.
 315 [577 0x241] POP                                                                                 # Remove item from stack.
 316 [578 0x242] PUSH2           0x0249                                                              # Place 2-byte item on stack.
 317 [581 0x245] PUSH2           0x061c                                                              # Place 2-byte item on stack.
 318 [584 0x248] JUMP            @0x61c                                                              # Alter the program counter.

:loc_0x249
 319 [585 0x249] JUMPDEST                                                                            # Mark a valid destination for jumps.
 320 [586 0x24a] PUSH1           0x40                                                                # Place 1 byte item on stack.
 321 [588 0x24c] MLOAD                                                                               # Load word from memory.
 322 [589 0x24d] DUP1                                                                                # Duplicate 1st stack item.
 323 [590 0x24e] DUP3                                                                                # Duplicate 3rd stack item.
 324 [591 0x24f] DUP2                                                                                # Duplicate 2nd stack item.
 325 [592 0x250] MSTORE                                                                              # Save word to memory.
 326 [593 0x251] PUSH1           0x20                                                                # Place 1 byte item on stack.
 327 [595 0x253] ADD                                                                                 # Addition operation.
 328 [596 0x254] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 329 [597 0x255] POP                                                                                 # Remove item from stack.
 330 [598 0x256] POP                                                                                 # Remove item from stack.
 331 [599 0x257] PUSH1           0x40                                                                # Place 1 byte item on stack.
 332 [601 0x259] MLOAD                                                                               # Load word from memory.
 333 [602 0x25a] DUP1                                                                                # Duplicate 1st stack item.
 334 [603 0x25b] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 335 [604 0x25c] SUB                                                                                 # Subtraction operation.
 336 [605 0x25d] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 337 [606 0x25e] RETURN                                                                              # Halt execution returning output data.

:loc_0x25f
 338 [607 0x25f] JUMPDEST                                             JUMPI@0x98                     # Mark a valid destination for jumps.
 339 [608 0x260] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 340 [609 0x261] DUP1                                                                                # Duplicate 1st stack item.
 341 [610 0x262] ISZERO                                                                              # Simple not operator
 342 [611 0x263] PUSH2           0x026b                                                              # Place 2-byte item on stack.
 343 [614 0x266] JUMPI           @0x26b                                                              # Conditionally alter the program counter.

 344 [615 0x267] PUSH1           0x00                                                                # Place 1 byte item on stack.
 345 [617 0x269] DUP1                                                                                # Duplicate 1st stack item.
 346 [618 0x26a] REVERT                                                                              # throw an error
:loc_0x26b
 347 [619 0x26b] JUMPDEST                                             JUMPI@0x266                    # Mark a valid destination for jumps.
 348 [620 0x26c] POP                                                                                 # Remove item from stack.
 349 [621 0x26d] PUSH2           0x0274                                                              # Place 2-byte item on stack.
 350 [624 0x270] PUSH2           0x071b                                                              # Place 2-byte item on stack.
 351 [627 0x273] JUMP            @0x71b                                                              # Alter the program counter.

:loc_0x274
 352 [628 0x274] JUMPDEST                                                                            # Mark a valid destination for jumps.
 353 [629 0x275] PUSH1           0x40                                                                # Place 1 byte item on stack.
 354 [631 0x277] MLOAD                                                                               # Load word from memory.
 355 [632 0x278] DUP1                                                                                # Duplicate 1st stack item.
 356 [633 0x279] DUP3                                                                                # Duplicate 3rd stack item.
 357 [634 0x27a] ISZERO                                                                              # Simple not operator
 358 [635 0x27b] ISZERO                                                                              # Simple not operator
 359 [636 0x27c] ISZERO                                                                              # Simple not operator
 360 [637 0x27d] ISZERO                                                                              # Simple not operator
 361 [638 0x27e] DUP2                                                                                # Duplicate 2nd stack item.
 362 [639 0x27f] MSTORE                                                                              # Save word to memory.
 363 [640 0x280] PUSH1           0x20                                                                # Place 1 byte item on stack.
 364 [642 0x282] ADD                                                                                 # Addition operation.
 365 [643 0x283] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 366 [644 0x284] POP                                                                                 # Remove item from stack.
 367 [645 0x285] POP                                                                                 # Remove item from stack.
 368 [646 0x286] PUSH1           0x40                                                                # Place 1 byte item on stack.
 369 [648 0x288] MLOAD                                                                               # Load word from memory.
 370 [649 0x289] DUP1                                                                                # Duplicate 1st stack item.
 371 [650 0x28a] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 372 [651 0x28b] SUB                                                                                 # Subtraction operation.
 373 [652 0x28c] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 374 [653 0x28d] RETURN                                                                              # Halt execution returning output data.

:loc_0x28e
 375 [654 0x28e] JUMPDEST                                             JUMPI@0xa3                     # Mark a valid destination for jumps.
 376 [655 0x28f] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 377 [656 0x290] DUP1                                                                                # Duplicate 1st stack item.
 378 [657 0x291] ISZERO                                                                              # Simple not operator
 379 [658 0x292] PUSH2           0x029a                                                              # Place 2-byte item on stack.
 380 [661 0x295] JUMPI           @0x29a                                                              # Conditionally alter the program counter.

 381 [662 0x296] PUSH1           0x00                                                                # Place 1 byte item on stack.
 382 [664 0x298] DUP1                                                                                # Duplicate 1st stack item.
 383 [665 0x299] REVERT                                                                              # throw an error
:loc_0x29a
 384 [666 0x29a] JUMPDEST                                             JUMPI@0x295                    # Mark a valid destination for jumps.
 385 [667 0x29b] POP                                                                                 # Remove item from stack.
 386 [668 0x29c] PUSH2           0x02cf                                                              # Place 2-byte item on stack.
 387 [671 0x29f] PUSH1           0x04                                                                # Place 1 byte item on stack.
 388 [673 0x2a1] DUP1                                                                                # Duplicate 1st stack item.
 389 [674 0x2a2] CALLDATASIZE                                                                        # Get size of input data in current environment.
 390 [675 0x2a3] SUB                                                                                 # Subtraction operation.
 391 [676 0x2a4] DUP2                                                                                # Duplicate 2nd stack item.
 392 [677 0x2a5] ADD                                                                                 # Addition operation.
 393 [678 0x2a6] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 394 [679 0x2a7] DUP1                                                                                # Duplicate 1st stack item.
 395 [680 0x2a8] DUP1                                                                                # Duplicate 1st stack item.
 396 [681 0x2a9] CALLDATALOAD                                                                        # Get input data of current environment.
 397 [682 0x2aa] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 398 [703 0x2bf] AND                                                                                 # Bitwise AND operation.
 399 [704 0x2c0] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 400 [705 0x2c1] PUSH1           0x20                                                                # Place 1 byte item on stack.
 401 [707 0x2c3] ADD                                                                                 # Addition operation.
 402 [708 0x2c4] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 403 [709 0x2c5] SWAP3                                                                               # Exchange 1st and 4th stack items.
 404 [710 0x2c6] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 405 [711 0x2c7] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 406 [712 0x2c8] POP                                                                                 # Remove item from stack.
 407 [713 0x2c9] POP                                                                                 # Remove item from stack.
 408 [714 0x2ca] POP                                                                                 # Remove item from stack.
 409 [715 0x2cb] PUSH2           0x072e                                                              # Place 2-byte item on stack.
 410 [718 0x2ce] JUMP            @0x72e                                                              # Alter the program counter.

:loc_0x2cf
 411 [719 0x2cf] JUMPDEST                                                                            # Mark a valid destination for jumps.
 412 [720 0x2d0] STOP                                                                                # Halts execution.

:loc_0x2d1
 413 [721 0x2d1] JUMPDEST                                             JUMPI@0xae                     # Mark a valid destination for jumps.
 414 [722 0x2d2] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 415 [723 0x2d3] DUP1                                                                                # Duplicate 1st stack item.
 416 [724 0x2d4] ISZERO                                                                              # Simple not operator
 417 [725 0x2d5] PUSH2           0x02dd                                                              # Place 2-byte item on stack.
 418 [728 0x2d8] JUMPI           @0x2dd                                                              # Conditionally alter the program counter.

 419 [729 0x2d9] PUSH1           0x00                                                                # Place 1 byte item on stack.
 420 [731 0x2db] DUP1                                                                                # Duplicate 1st stack item.
 421 [732 0x2dc] REVERT                                                                              # throw an error
:loc_0x2dd
 422 [733 0x2dd] JUMPDEST                                             JUMPI@0x2d8                    # Mark a valid destination for jumps.
 423 [734 0x2de] POP                                                                                 # Remove item from stack.
 424 [735 0x2df] PUSH2           0x02e6                                                              # Place 2-byte item on stack.
 425 [738 0x2e2] PUSH2           0x0883                                                              # Place 2-byte item on stack.
 426 [741 0x2e5] JUMP            @0x883                                                              # Alter the program counter.

:loc_0x2e6
 427 [742 0x2e6] JUMPDEST                                                                            # Mark a valid destination for jumps.
 428 [743 0x2e7] PUSH1           0x40                                                                # Place 1 byte item on stack.
 429 [745 0x2e9] MLOAD                                                                               # Load word from memory.
 430 [746 0x2ea] DUP1                                                                                # Duplicate 1st stack item.
 431 [747 0x2eb] DUP3                                                                                # Duplicate 3rd stack item.
 432 [748 0x2ec] ISZERO                                                                              # Simple not operator
 433 [749 0x2ed] ISZERO                                                                              # Simple not operator
 434 [750 0x2ee] ISZERO                                                                              # Simple not operator
 435 [751 0x2ef] ISZERO                                                                              # Simple not operator
 436 [752 0x2f0] DUP2                                                                                # Duplicate 2nd stack item.
 437 [753 0x2f1] MSTORE                                                                              # Save word to memory.
 438 [754 0x2f2] PUSH1           0x20                                                                # Place 1 byte item on stack.
 439 [756 0x2f4] ADD                                                                                 # Addition operation.
 440 [757 0x2f5] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 441 [758 0x2f6] POP                                                                                 # Remove item from stack.
 442 [759 0x2f7] POP                                                                                 # Remove item from stack.
 443 [760 0x2f8] PUSH1           0x40                                                                # Place 1 byte item on stack.
 444 [762 0x2fa] MLOAD                                                                               # Load word from memory.
 445 [763 0x2fb] DUP1                                                                                # Duplicate 1st stack item.
 446 [764 0x2fc] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 447 [765 0x2fd] SUB                                                                                 # Subtraction operation.
 448 [766 0x2fe] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 449 [767 0x2ff] RETURN                                                                              # Halt execution returning output data.

:loc_0x300
 450 [768 0x300] JUMPDEST                                             JUMPI@0xb9                     # Mark a valid destination for jumps.
 451 [769 0x301] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 452 [770 0x302] DUP1                                                                                # Duplicate 1st stack item.
 453 [771 0x303] ISZERO                                                                              # Simple not operator
 454 [772 0x304] PUSH2           0x030c                                                              # Place 2-byte item on stack.
 455 [775 0x307] JUMPI           @0x30c                                                              # Conditionally alter the program counter.

 456 [776 0x308] PUSH1           0x00                                                                # Place 1 byte item on stack.
 457 [778 0x30a] DUP1                                                                                # Duplicate 1st stack item.
 458 [779 0x30b] REVERT                                                                              # throw an error
:loc_0x30c
 459 [780 0x30c] JUMPDEST                                             JUMPI@0x307                    # Mark a valid destination for jumps.
 460 [781 0x30d] POP                                                                                 # Remove item from stack.
 461 [782 0x30e] PUSH2           0x0315                                                              # Place 2-byte item on stack.
 462 [785 0x311] PUSH2           0x0954                                                              # Place 2-byte item on stack.
 463 [788 0x314] JUMP            @0x954                                                              # Alter the program counter.

:loc_0x315
 464 [789 0x315] JUMPDEST                                                                            # Mark a valid destination for jumps.
 465 [790 0x316] PUSH1           0x40                                                                # Place 1 byte item on stack.
 466 [792 0x318] MLOAD                                                                               # Load word from memory.
 467 [793 0x319] DUP1                                                                                # Duplicate 1st stack item.
 468 [794 0x31a] DUP3                                                                                # Duplicate 3rd stack item.
 469 [795 0x31b] ISZERO                                                                              # Simple not operator
 470 [796 0x31c] ISZERO                                                                              # Simple not operator
 471 [797 0x31d] ISZERO                                                                              # Simple not operator
 472 [798 0x31e] ISZERO                                                                              # Simple not operator
 473 [799 0x31f] DUP2                                                                                # Duplicate 2nd stack item.
 474 [800 0x320] MSTORE                                                                              # Save word to memory.
 475 [801 0x321] PUSH1           0x20                                                                # Place 1 byte item on stack.
 476 [803 0x323] ADD                                                                                 # Addition operation.
 477 [804 0x324] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 478 [805 0x325] POP                                                                                 # Remove item from stack.
 479 [806 0x326] POP                                                                                 # Remove item from stack.
 480 [807 0x327] PUSH1           0x40                                                                # Place 1 byte item on stack.
 481 [809 0x329] MLOAD                                                                               # Load word from memory.
 482 [810 0x32a] DUP1                                                                                # Duplicate 1st stack item.
 483 [811 0x32b] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 484 [812 0x32c] SUB                                                                                 # Subtraction operation.
 485 [813 0x32d] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 486 [814 0x32e] RETURN                                                                              # Halt execution returning output data.

:loc_0x32f
 487 [815 0x32f] JUMPDEST                                             JUMP@0xd3                      # Mark a valid destination for jumps.
 488 [816 0x330] PUSH1           0x04                                                                # Place 1 byte item on stack.
 489 [818 0x332] SLOAD                                                                               # Load word from storage.
 490 [819 0x333] DUP2                                                                                # Duplicate 2nd stack item.
 491 [820 0x334] JUMP                                                                                # Alter the program counter.

:loc_0x335
 492 [821 0x335] JUMPDEST                                             JUMP@0xfe                      # Mark a valid destination for jumps.
 493 [822 0x336] PUSH1           0x02                                                                # Place 1 byte item on stack.
 494 [824 0x338] PUSH1           0x00                                                                # Place 1 byte item on stack.
 495 [826 0x33a] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 496 [827 0x33b] SLOAD                                                                               # Load word from storage.
 497 [828 0x33c] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 498 [829 0x33d] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 499 [832 0x340] EXP                                                                                 # Exponential operation.
 500 [833 0x341] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 501 [834 0x342] DIV                                                                                 # Integer division operation.
 502 [835 0x343] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 503 [856 0x358] AND                                                                                 # Bitwise AND operation.
 504 [857 0x359] DUP2                                                                                # Duplicate 2nd stack item.
 505 [858 0x35a] JUMP                                                                                # Alter the program counter.

:loc_0x35b
 506 [859 0x35b] JUMPDEST                                             JUMP@0x155                     # Mark a valid destination for jumps.
 507 [860 0x35c] PUSH1           0x05                                                                # Place 1 byte item on stack.
 508 [862 0x35e] SLOAD                                                                               # Load word from storage.
 509 [863 0x35f] DUP2                                                                                # Duplicate 2nd stack item.
 510 [864 0x360] JUMP                                                                                # Alter the program counter.

:loc_0x361
 511 [865 0x361] JUMPDEST                                             JUMP@0x180                     # Mark a valid destination for jumps.
 512 [866 0x362] PUSH1           0x03                                                                # Place 1 byte item on stack.
 513 [868 0x364] SLOAD                                                                               # Load word from storage.
 514 [869 0x365] DUP2                                                                                # Duplicate 2nd stack item.
 515 [870 0x366] JUMP                                                                                # Alter the program counter.

:loc_0x367
 516 [871 0x367] JUMPDEST                                             JUMP@0x1ab                     # Mark a valid destination for jumps.
 517 [872 0x368] PUSH1           0x00                                                                # Place 1 byte item on stack.
 518 [874 0x36a] DUP1                                                                                # Duplicate 1st stack item.
 519 [875 0x36b] PUSH1           0x00                                                                # Place 1 byte item on stack.
 520 [877 0x36d] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 521 [878 0x36e] SLOAD                                                                               # Load word from storage.
 522 [879 0x36f] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 523 [880 0x370] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 524 [883 0x373] EXP                                                                                 # Exponential operation.
 525 [884 0x374] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 526 [885 0x375] DIV                                                                                 # Integer division operation.
 527 [886 0x376] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 528 [907 0x38b] AND                                                                                 # Bitwise AND operation.
 529 [908 0x38c] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 530 [929 0x3a1] AND                                                                                 # Bitwise AND operation.
 531 [930 0x3a2] CALLER                                                                              # Get caller address.This is the address of the account that is directly responsible for this execution.
 532 [931 0x3a3] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 533 [952 0x3b8] AND                                                                                 # Bitwise AND operation.
 534 [953 0x3b9] EQ                                                                                  # Equality  comparison
 535 [954 0x3ba] ISZERO                                                                              # Simple not operator
 536 [955 0x3bb] ISZERO                                                                              # Simple not operator
 537 [956 0x3bc] PUSH2           0x03c4                                                              # Place 2-byte item on stack.
 538 [959 0x3bf] JUMPI           @0x3c4                                                              # Conditionally alter the program counter.

 539 [960 0x3c0] PUSH1           0x00                                                                # Place 1 byte item on stack.
 540 [962 0x3c2] DUP1                                                                                # Duplicate 1st stack item.
 541 [963 0x3c3] REVERT                                                                              # throw an error
:loc_0x3c4
 542 [964 0x3c4] JUMPDEST                                             JUMPI@0x3bf                    # Mark a valid destination for jumps.
 543 [965 0x3c5] PUSH1           0x02                                                                # Place 1 byte item on stack.
 544 [967 0x3c7] PUSH1           0x14                                                                # Place 1 byte item on stack.
 545 [969 0x3c9] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 546 [970 0x3ca] SLOAD                                                                               # Load word from storage.
 547 [971 0x3cb] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 548 [972 0x3cc] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 549 [975 0x3cf] EXP                                                                                 # Exponential operation.
 550 [976 0x3d0] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 551 [977 0x3d1] DIV                                                                                 # Integer division operation.
 552 [978 0x3d2] PUSH1           0xff                                                                # Place 1 byte item on stack.
 553 [980 0x3d4] AND                                                                                 # Bitwise AND operation.
 554 [981 0x3d5] ISZERO                                                                              # Simple not operator
 555 [982 0x3d6] ISZERO                                                                              # Simple not operator
 556 [983 0x3d7] PUSH2           0x03df                                                              # Place 2-byte item on stack.
 557 [986 0x3da] JUMPI           @0x3df                                                              # Conditionally alter the program counter.

 558 [987 0x3db] PUSH1           0x00                                                                # Place 1 byte item on stack.
 559 [989 0x3dd] DUP1                                                                                # Duplicate 1st stack item.
 560 [990 0x3de] REVERT                                                                              # throw an error
:loc_0x3df
 561 [991 0x3df] JUMPDEST                                             JUMPI@0x3da                    # Mark a valid destination for jumps.
 562 [992 0x3e0] PUSH1           0x02                                                                # Place 1 byte item on stack.
 563 [994 0x3e2] PUSH1           0x15                                                                # Place 1 byte item on stack.
 564 [996 0x3e4] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 565 [997 0x3e5] SLOAD                                                                               # Load word from storage.
 566 [998 0x3e6] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 567 [999 0x3e7] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 568 [1002 0x3ea] EXP                                                                                 # Exponential operation.
 569 [1003 0x3eb] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 570 [1004 0x3ec] DIV                                                                                 # Integer division operation.
 571 [1005 0x3ed] PUSH1           0xff                                                                # Place 1 byte item on stack.
 572 [1007 0x3ef] AND                                                                                 # Bitwise AND operation.
 573 [1008 0x3f0] ISZERO                                                                              # Simple not operator
 574 [1009 0x3f1] ISZERO                                                                              # Simple not operator
 575 [1010 0x3f2] ISZERO                                                                              # Simple not operator
 576 [1011 0x3f3] PUSH2           0x03fb                                                              # Place 2-byte item on stack.
 577 [1014 0x3f6] JUMPI           @0x3fb                                                              # Conditionally alter the program counter.

 578 [1015 0x3f7] PUSH1           0x00                                                                # Place 1 byte item on stack.
 579 [1017 0x3f9] DUP1                                                                                # Duplicate 1st stack item.
 580 [1018 0x3fa] REVERT                                                                              # throw an error
:loc_0x3fb
 581 [1019 0x3fb] JUMPDEST                                             JUMPI@0x3f6                    # Mark a valid destination for jumps.
 582 [1020 0x3fc] PUSH2           0x0403                                                              # Place 2-byte item on stack.
 583 [1023 0x3ff] PUSH2           0x060b                                                              # Place 2-byte item on stack.
 584 [1026 0x402] JUMP            @0x60b                                                              # Alter the program counter.

:loc_0x403
 585 [1027 0x403] JUMPDEST                                                                            # Mark a valid destination for jumps.
 586 [1028 0x404] ISZERO                                                                              # Simple not operator
 587 [1029 0x405] ISZERO                                                                              # Simple not operator
 588 [1030 0x406] PUSH2           0x040e                                                              # Place 2-byte item on stack.
 589 [1033 0x409] JUMPI           @0x40e                                                              # Conditionally alter the program counter.

 590 [1034 0x40a] PUSH1           0x00                                                                # Place 1 byte item on stack.
 591 [1036 0x40c] DUP1                                                                                # Duplicate 1st stack item.
 592 [1037 0x40d] REVERT                                                                              # throw an error
:loc_0x40e
 593 [1038 0x40e] JUMPDEST                                             JUMPI@0x409                    # Mark a valid destination for jumps.
 594 [1039 0x40f] PUSH2           0x0416                                                              # Place 2-byte item on stack.
 595 [1042 0x412] PUSH2           0x061c                                                              # Place 2-byte item on stack.
 596 [1045 0x415] JUMP            @0x61c                                                              # Alter the program counter.

:loc_0x416
 597 [1046 0x416] JUMPDEST                                                                            # Mark a valid destination for jumps.
 598 [1047 0x417] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 599 [1048 0x418] POP                                                                                 # Remove item from stack.
 600 [1049 0x419] PUSH1           0x01                                                                # Place 1 byte item on stack.
 601 [1051 0x41b] PUSH1           0x00                                                                # Place 1 byte item on stack.
 602 [1053 0x41d] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 603 [1054 0x41e] SLOAD                                                                               # Load word from storage.
 604 [1055 0x41f] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 605 [1056 0x420] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 606 [1059 0x423] EXP                                                                                 # Exponential operation.
 607 [1060 0x424] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 608 [1061 0x425] DIV                                                                                 # Integer division operation.
 609 [1062 0x426] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 610 [1083 0x43b] AND                                                                                 # Bitwise AND operation.
 611 [1084 0x43c] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 612 [1105 0x451] AND                                                                                 # Bitwise AND operation.
 613 [1106 0x452] PUSH4           0xa9059cbb  (*ambiguous* 'function many_msg_babbage(bytes1)')                                # Place 4-byte item on stack.
 614 [1111 0x457] PUSH1           0x02                                                                # Place 1 byte item on stack.
 615 [1113 0x459] PUSH1           0x00                                                                # Place 1 byte item on stack.
 616 [1115 0x45b] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 617 [1116 0x45c] SLOAD                                                                               # Load word from storage.
 618 [1117 0x45d] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 619 [1118 0x45e] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 620 [1121 0x461] EXP                                                                                 # Exponential operation.
 621 [1122 0x462] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 622 [1123 0x463] DIV                                                                                 # Integer division operation.
 623 [1124 0x464] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 624 [1145 0x479] AND                                                                                 # Bitwise AND operation.
 625 [1146 0x47a] DUP4                                                                                # Duplicate 4th stack item.
 626 [1147 0x47b] PUSH1           0x40                                                                # Place 1 byte item on stack.
 627 [1149 0x47d] MLOAD                                                                               # Load word from memory.
 628 [1150 0x47e] DUP4                                                                                # Duplicate 4th stack item.
 629 [1151 0x47f] PUSH4           0xffffffff                                                          # Place 4-byte item on stack.
 630 [1156 0x484] AND                                                                                 # Bitwise AND operation.
 631 [1157 0x485] PUSH29          0x0100000000000000000000000000000000000000000000000000000000                                # Place 29-byte item on stack.
 632 [1187 0x4a3] MUL                                                                                 # Multiplication operation.
 633 [1188 0x4a4] DUP2                                                                                # Duplicate 2nd stack item.
 634 [1189 0x4a5] MSTORE                                                                              # Save word to memory.
 635 [1190 0x4a6] PUSH1           0x04                                                                # Place 1 byte item on stack.
 636 [1192 0x4a8] ADD                                                                                 # Addition operation.
 637 [1193 0x4a9] DUP1                                                                                # Duplicate 1st stack item.
 638 [1194 0x4aa] DUP4                                                                                # Duplicate 4th stack item.
 639 [1195 0x4ab] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 640 [1216 0x4c0] AND                                                                                 # Bitwise AND operation.
 641 [1217 0x4c1] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 642 [1238 0x4d6] AND                                                                                 # Bitwise AND operation.
 643 [1239 0x4d7] DUP2                                                                                # Duplicate 2nd stack item.
 644 [1240 0x4d8] MSTORE                                                                              # Save word to memory.
 645 [1241 0x4d9] PUSH1           0x20                                                                # Place 1 byte item on stack.
 646 [1243 0x4db] ADD                                                                                 # Addition operation.
 647 [1244 0x4dc] DUP3                                                                                # Duplicate 3rd stack item.
 648 [1245 0x4dd] DUP2                                                                                # Duplicate 2nd stack item.
 649 [1246 0x4de] MSTORE                                                                              # Save word to memory.
 650 [1247 0x4df] PUSH1           0x20                                                                # Place 1 byte item on stack.
 651 [1249 0x4e1] ADD                                                                                 # Addition operation.
 652 [1250 0x4e2] SWAP3                                                                               # Exchange 1st and 4th stack items.
 653 [1251 0x4e3] POP                                                                                 # Remove item from stack.
 654 [1252 0x4e4] POP                                                                                 # Remove item from stack.
 655 [1253 0x4e5] POP                                                                                 # Remove item from stack.
 656 [1254 0x4e6] PUSH1           0x20                                                                # Place 1 byte item on stack.
 657 [1256 0x4e8] PUSH1           0x40                                                                # Place 1 byte item on stack.
 658 [1258 0x4ea] MLOAD                                                                               # Load word from memory.
 659 [1259 0x4eb] DUP1                                                                                # Duplicate 1st stack item.
 660 [1260 0x4ec] DUP4                                                                                # Duplicate 4th stack item.
 661 [1261 0x4ed] SUB                                                                                 # Subtraction operation.
 662 [1262 0x4ee] DUP2                                                                                # Duplicate 2nd stack item.
 663 [1263 0x4ef] PUSH1           0x00                                                                # Place 1 byte item on stack.
 664 [1265 0x4f1] DUP8                                                                                # Duplicate 8th stack item.
 665 [1266 0x4f2] DUP1                                                                                # Duplicate 1st stack item.
 666 [1267 0x4f3] EXTCODESIZE                                                                         # Get size of an account’s code.
 667 [1268 0x4f4] ISZERO                                                                              # Simple not operator
 668 [1269 0x4f5] DUP1                                                                                # Duplicate 1st stack item.
 669 [1270 0x4f6] ISZERO                                                                              # Simple not operator
 670 [1271 0x4f7] PUSH2           0x04ff                                                              # Place 2-byte item on stack.
 671 [1274 0x4fa] JUMPI           @0x4ff                                                              # Conditionally alter the program counter.

 672 [1275 0x4fb] PUSH1           0x00                                                                # Place 1 byte item on stack.
 673 [1277 0x4fd] DUP1                                                                                # Duplicate 1st stack item.
 674 [1278 0x4fe] REVERT                                                                              # throw an error
:loc_0x4ff
 675 [1279 0x4ff] JUMPDEST                                             JUMPI@0x4fa                    # Mark a valid destination for jumps.
 676 [1280 0x500] POP                                                                                 # Remove item from stack.
 677 [1281 0x501] GAS                                                                                 # Get the amount of available gas, including the corresponding reduction
 678 [1282 0x502] CALL                                                                                # Message-call into an account.
 679 [1283 0x503] ISZERO                                                                              # Simple not operator
 680 [1284 0x504] DUP1                                                                                # Duplicate 1st stack item.
 681 [1285 0x505] ISZERO                                                                              # Simple not operator
 682 [1286 0x506] PUSH2           0x0513                                                              # Place 2-byte item on stack.
 683 [1289 0x509] JUMPI           @0x513                                                              # Conditionally alter the program counter.

 684 [1290 0x50a] RETURNDATASIZE                                                                      # Push the size of the return data buffer onto the stack.
 685 [1291 0x50b] PUSH1           0x00                                                                # Place 1 byte item on stack.
 686 [1293 0x50d] DUP1                                                                                # Duplicate 1st stack item.
 687 [1294 0x50e] RETURNDATACOPY                                                                      # Copy data from the return data buffer.
 688 [1295 0x50f] RETURNDATASIZE                                                                      # Push the size of the return data buffer onto the stack.
 689 [1296 0x510] PUSH1           0x00                                                                # Place 1 byte item on stack.
 690 [1298 0x512] REVERT                                                                              # throw an error
:loc_0x513
 691 [1299 0x513] JUMPDEST                                             JUMPI@0x509                    # Mark a valid destination for jumps.
 692 [1300 0x514] POP                                                                                 # Remove item from stack.
 693 [1301 0x515] POP                                                                                 # Remove item from stack.
 694 [1302 0x516] POP                                                                                 # Remove item from stack.
 695 [1303 0x517] POP                                                                                 # Remove item from stack.
 696 [1304 0x518] PUSH1           0x40                                                                # Place 1 byte item on stack.
 697 [1306 0x51a] MLOAD                                                                               # Load word from memory.
 698 [1307 0x51b] RETURNDATASIZE                                                                      # Push the size of the return data buffer onto the stack.
 699 [1308 0x51c] PUSH1           0x20                                                                # Place 1 byte item on stack.
 700 [1310 0x51e] DUP2                                                                                # Duplicate 2nd stack item.
 701 [1311 0x51f] LT                                                                                  # Lesser-than comparison
 702 [1312 0x520] ISZERO                                                                              # Simple not operator
 703 [1313 0x521] PUSH2           0x0529                                                              # Place 2-byte item on stack.
 704 [1316 0x524] JUMPI           @0x529                                                              # Conditionally alter the program counter.

 705 [1317 0x525] PUSH1           0x00                                                                # Place 1 byte item on stack.
 706 [1319 0x527] DUP1                                                                                # Duplicate 1st stack item.
 707 [1320 0x528] REVERT                                                                              # throw an error
:loc_0x529
 708 [1321 0x529] JUMPDEST                                             JUMPI@0x524                    # Mark a valid destination for jumps.
 709 [1322 0x52a] DUP2                                                                                # Duplicate 2nd stack item.
 710 [1323 0x52b] ADD                                                                                 # Addition operation.
 711 [1324 0x52c] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 712 [1325 0x52d] DUP1                                                                                # Duplicate 1st stack item.
 713 [1326 0x52e] DUP1                                                                                # Duplicate 1st stack item.
 714 [1327 0x52f] MLOAD                                                                               # Load word from memory.
 715 [1328 0x530] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 716 [1329 0x531] PUSH1           0x20                                                                # Place 1 byte item on stack.
 717 [1331 0x533] ADD                                                                                 # Addition operation.
 718 [1332 0x534] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 719 [1333 0x535] SWAP3                                                                               # Exchange 1st and 4th stack items.
 720 [1334 0x536] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 721 [1335 0x537] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 722 [1336 0x538] POP                                                                                 # Remove item from stack.
 723 [1337 0x539] POP                                                                                 # Remove item from stack.
 724 [1338 0x53a] POP                                                                                 # Remove item from stack.
 725 [1339 0x53b] POP                                                                                 # Remove item from stack.
 726 [1340 0x53c] PUSH32          0x9cf9e3ab58b33f06d81842ea0ad850b6640c6430d6396973312e1715792e7a91                                # Place 32-byte (full word) item on stack.
 727 [1373 0x55d] PUSH1           0x02                                                                # Place 1 byte item on stack.
 728 [1375 0x55f] PUSH1           0x00                                                                # Place 1 byte item on stack.
 729 [1377 0x561] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 730 [1378 0x562] SLOAD                                                                               # Load word from storage.
 731 [1379 0x563] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 732 [1380 0x564] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 733 [1383 0x567] EXP                                                                                 # Exponential operation.
 734 [1384 0x568] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 735 [1385 0x569] DIV                                                                                 # Integer division operation.
 736 [1386 0x56a] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 737 [1407 0x57f] AND                                                                                 # Bitwise AND operation.
 738 [1408 0x580] DUP3                                                                                # Duplicate 3rd stack item.
 739 [1409 0x581] PUSH1           0x40                                                                # Place 1 byte item on stack.
 740 [1411 0x583] MLOAD                                                                               # Load word from memory.
 741 [1412 0x584] DUP1                                                                                # Duplicate 1st stack item.
 742 [1413 0x585] DUP4                                                                                # Duplicate 4th stack item.
 743 [1414 0x586] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 744 [1435 0x59b] AND                                                                                 # Bitwise AND operation.
 745 [1436 0x59c] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 746 [1457 0x5b1] AND                                                                                 # Bitwise AND operation.
 747 [1458 0x5b2] DUP2                                                                                # Duplicate 2nd stack item.
 748 [1459 0x5b3] MSTORE                                                                              # Save word to memory.
 749 [1460 0x5b4] PUSH1           0x20                                                                # Place 1 byte item on stack.
 750 [1462 0x5b6] ADD                                                                                 # Addition operation.
 751 [1463 0x5b7] DUP3                                                                                # Duplicate 3rd stack item.
 752 [1464 0x5b8] DUP2                                                                                # Duplicate 2nd stack item.
 753 [1465 0x5b9] MSTORE                                                                              # Save word to memory.
 754 [1466 0x5ba] PUSH1           0x20                                                                # Place 1 byte item on stack.
 755 [1468 0x5bc] ADD                                                                                 # Addition operation.
 756 [1469 0x5bd] SWAP3                                                                               # Exchange 1st and 4th stack items.
 757 [1470 0x5be] POP                                                                                 # Remove item from stack.
 758 [1471 0x5bf] POP                                                                                 # Remove item from stack.
 759 [1472 0x5c0] POP                                                                                 # Remove item from stack.
 760 [1473 0x5c1] PUSH1           0x40                                                                # Place 1 byte item on stack.
 761 [1475 0x5c3] MLOAD                                                                               # Load word from memory.
 762 [1476 0x5c4] DUP1                                                                                # Duplicate 1st stack item.
 763 [1477 0x5c5] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 764 [1478 0x5c6] SUB                                                                                 # Subtraction operation.
 765 [1479 0x5c7] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 766 [1480 0x5c8] LOG1            0x60                                                                # Append log record with one topic.
 767 [1482 0x5ca] ADD                                                                                 # Addition operation.
 768 [1483 0x5cb] PUSH1           0x02                                                                # Place 1 byte item on stack.
 769 [1485 0x5cd] PUSH1           0x15                                                                # Place 1 byte item on stack.
 770 [1487 0x5cf] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 771 [1490 0x5d2] EXP                                                                                 # Exponential operation.
 772 [1491 0x5d3] DUP2                                                                                # Duplicate 2nd stack item.
 773 [1492 0x5d4] SLOAD                                                                               # Load word from storage.
 774 [1493 0x5d5] DUP2                                                                                # Duplicate 2nd stack item.
 775 [1494 0x5d6] PUSH1           0xff                                                                # Place 1 byte item on stack.
 776 [1496 0x5d8] MUL                                                                                 # Multiplication operation.
 777 [1497 0x5d9] NOT                                                                                 # Bitwise NOT operation.
 778 [1498 0x5da] AND                                                                                 # Bitwise AND operation.
 779 [1499 0x5db] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 780 [1500 0x5dc] DUP4                                                                                # Duplicate 4th stack item.
 781 [1501 0x5dd] ISZERO                                                                              # Simple not operator
 782 [1502 0x5de] ISZERO                                                                              # Simple not operator
 783 [1503 0x5df] MUL                                                                                 # Multiplication operation.
 784 [1504 0x5e0] OR                                                                                  # Bitwise OR operation.
 785 [1505 0x5e1] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 786 [1506 0x5e2] SSTORE                                                                              # Save word to storage.
 787 [1507 0x5e3] POP                                                                                 # Remove item from stack.
 788 [1508 0x5e4] POP                                                                                 # Remove item from stack.
 789 [1509 0x5e5] JUMP                                                                                # Alter the program counter.

:loc_0x5e6
 790 [1510 0x5e6] JUMPDEST                                             JUMP@0x1c2                     # Mark a valid destination for jumps.
 791 [1511 0x5e7] PUSH1           0x00                                                                # Place 1 byte item on stack.
 792 [1513 0x5e9] DUP1                                                                                # Duplicate 1st stack item.
 793 [1514 0x5ea] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 794 [1515 0x5eb] SLOAD                                                                               # Load word from storage.
 795 [1516 0x5ec] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 796 [1517 0x5ed] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 797 [1520 0x5f0] EXP                                                                                 # Exponential operation.
 798 [1521 0x5f1] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 799 [1522 0x5f2] DIV                                                                                 # Integer division operation.
 800 [1523 0x5f3] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 801 [1544 0x608] AND                                                                                 # Bitwise AND operation.
 802 [1545 0x609] DUP2                                                                                # Duplicate 2nd stack item.
 803 [1546 0x60a] JUMP                                                                                # Alter the program counter.

:loc_0x60b
 804 [1547 0x60b] JUMPDEST                                             JUMP@0x219,JUMP@0x402          # Mark a valid destination for jumps.
 805 [1548 0x60c] PUSH1           0x00                                                                # Place 1 byte item on stack.
 806 [1550 0x60e] DUP1                                                                                # Duplicate 1st stack item.
 807 [1551 0x60f] TIMESTAMP                                                                           # Get the block’s timestamp.
 808 [1552 0x610] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 809 [1553 0x611] POP                                                                                 # Remove item from stack.
 810 [1554 0x612] PUSH1           0x04                                                                # Place 1 byte item on stack.
 811 [1556 0x614] SLOAD                                                                               # Load word from storage.
 812 [1557 0x615] DUP2                                                                                # Duplicate 2nd stack item.
 813 [1558 0x616] GT                                                                                  # Greater-than comparison
 814 [1559 0x617] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 815 [1560 0x618] POP                                                                                 # Remove item from stack.
 816 [1561 0x619] POP                                                                                 # Remove item from stack.
 817 [1562 0x61a] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 818 [1563 0x61b] JUMP                                                                                # Alter the program counter.

:loc_0x61c
 819 [1564 0x61c] JUMPDEST                                             JUMP@0x905,JUMP@0x415,JUMP@0x248 # Mark a valid destination for jumps.
 820 [1565 0x61d] PUSH1           0x00                                                                # Place 1 byte item on stack.
 821 [1567 0x61f] PUSH1           0x01                                                                # Place 1 byte item on stack.
 822 [1569 0x621] PUSH1           0x00                                                                # Place 1 byte item on stack.
 823 [1571 0x623] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 824 [1572 0x624] SLOAD                                                                               # Load word from storage.
 825 [1573 0x625] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 826 [1574 0x626] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 827 [1577 0x629] EXP                                                                                 # Exponential operation.
 828 [1578 0x62a] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 829 [1579 0x62b] DIV                                                                                 # Integer division operation.
 830 [1580 0x62c] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 831 [1601 0x641] AND                                                                                 # Bitwise AND operation.
 832 [1602 0x642] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 833 [1623 0x657] AND                                                                                 # Bitwise AND operation.
 834 [1624 0x658] PUSH4           0x70a08231  ('function balanceOf(address)')                                # Place 4-byte item on stack.
 835 [1629 0x65d] ADDRESS                                                                             # Get address of currently executing account.
 836 [1630 0x65e] PUSH1           0x40                                                                # Place 1 byte item on stack.
 837 [1632 0x660] MLOAD                                                                               # Load word from memory.
 838 [1633 0x661] DUP3                                                                                # Duplicate 3rd stack item.
 839 [1634 0x662] PUSH4           0xffffffff                                                          # Place 4-byte item on stack.
 840 [1639 0x667] AND                                                                                 # Bitwise AND operation.
 841 [1640 0x668] PUSH29          0x0100000000000000000000000000000000000000000000000000000000                                # Place 29-byte item on stack.
 842 [1670 0x686] MUL                                                                                 # Multiplication operation.
 843 [1671 0x687] DUP2                                                                                # Duplicate 2nd stack item.
 844 [1672 0x688] MSTORE                                                                              # Save word to memory.
 845 [1673 0x689] PUSH1           0x04                                                                # Place 1 byte item on stack.
 846 [1675 0x68b] ADD                                                                                 # Addition operation.
 847 [1676 0x68c] DUP1                                                                                # Duplicate 1st stack item.
 848 [1677 0x68d] DUP3                                                                                # Duplicate 3rd stack item.
 849 [1678 0x68e] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 850 [1699 0x6a3] AND                                                                                 # Bitwise AND operation.
 851 [1700 0x6a4] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 852 [1721 0x6b9] AND                                                                                 # Bitwise AND operation.
 853 [1722 0x6ba] DUP2                                                                                # Duplicate 2nd stack item.
 854 [1723 0x6bb] MSTORE                                                                              # Save word to memory.
 855 [1724 0x6bc] PUSH1           0x20                                                                # Place 1 byte item on stack.
 856 [1726 0x6be] ADD                                                                                 # Addition operation.
 857 [1727 0x6bf] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 858 [1728 0x6c0] POP                                                                                 # Remove item from stack.
 859 [1729 0x6c1] POP                                                                                 # Remove item from stack.
 860 [1730 0x6c2] PUSH1           0x20                                                                # Place 1 byte item on stack.
 861 [1732 0x6c4] PUSH1           0x40                                                                # Place 1 byte item on stack.
 862 [1734 0x6c6] MLOAD                                                                               # Load word from memory.
 863 [1735 0x6c7] DUP1                                                                                # Duplicate 1st stack item.
 864 [1736 0x6c8] DUP4                                                                                # Duplicate 4th stack item.
 865 [1737 0x6c9] SUB                                                                                 # Subtraction operation.
 866 [1738 0x6ca] DUP2                                                                                # Duplicate 2nd stack item.
 867 [1739 0x6cb] PUSH1           0x00                                                                # Place 1 byte item on stack.
 868 [1741 0x6cd] DUP8                                                                                # Duplicate 8th stack item.
 869 [1742 0x6ce] DUP1                                                                                # Duplicate 1st stack item.
 870 [1743 0x6cf] EXTCODESIZE                                                                         # Get size of an account’s code.
 871 [1744 0x6d0] ISZERO                                                                              # Simple not operator
 872 [1745 0x6d1] DUP1                                                                                # Duplicate 1st stack item.
 873 [1746 0x6d2] ISZERO                                                                              # Simple not operator
 874 [1747 0x6d3] PUSH2           0x06db                                                              # Place 2-byte item on stack.
 875 [1750 0x6d6] JUMPI           @0x6db                                                              # Conditionally alter the program counter.

 876 [1751 0x6d7] PUSH1           0x00                                                                # Place 1 byte item on stack.
 877 [1753 0x6d9] DUP1                                                                                # Duplicate 1st stack item.
 878 [1754 0x6da] REVERT                                                                              # throw an error
:loc_0x6db
 879 [1755 0x6db] JUMPDEST                                             JUMPI@0x6d6                    # Mark a valid destination for jumps.
 880 [1756 0x6dc] POP                                                                                 # Remove item from stack.
 881 [1757 0x6dd] GAS                                                                                 # Get the amount of available gas, including the corresponding reduction
 882 [1758 0x6de] CALL                                                                                # Message-call into an account.
 883 [1759 0x6df] ISZERO                                                                              # Simple not operator
 884 [1760 0x6e0] DUP1                                                                                # Duplicate 1st stack item.
 885 [1761 0x6e1] ISZERO                                                                              # Simple not operator
 886 [1762 0x6e2] PUSH2           0x06ef                                                              # Place 2-byte item on stack.
 887 [1765 0x6e5] JUMPI           @0x6ef                                                              # Conditionally alter the program counter.

 888 [1766 0x6e6] RETURNDATASIZE                                                                      # Push the size of the return data buffer onto the stack.
 889 [1767 0x6e7] PUSH1           0x00                                                                # Place 1 byte item on stack.
 890 [1769 0x6e9] DUP1                                                                                # Duplicate 1st stack item.
 891 [1770 0x6ea] RETURNDATACOPY                                                                      # Copy data from the return data buffer.
 892 [1771 0x6eb] RETURNDATASIZE                                                                      # Push the size of the return data buffer onto the stack.
 893 [1772 0x6ec] PUSH1           0x00                                                                # Place 1 byte item on stack.
 894 [1774 0x6ee] REVERT                                                                              # throw an error
:loc_0x6ef
 895 [1775 0x6ef] JUMPDEST                                             JUMPI@0x6e5                    # Mark a valid destination for jumps.
 896 [1776 0x6f0] POP                                                                                 # Remove item from stack.
 897 [1777 0x6f1] POP                                                                                 # Remove item from stack.
 898 [1778 0x6f2] POP                                                                                 # Remove item from stack.
 899 [1779 0x6f3] POP                                                                                 # Remove item from stack.
 900 [1780 0x6f4] PUSH1           0x40                                                                # Place 1 byte item on stack.
 901 [1782 0x6f6] MLOAD                                                                               # Load word from memory.
 902 [1783 0x6f7] RETURNDATASIZE                                                                      # Push the size of the return data buffer onto the stack.
 903 [1784 0x6f8] PUSH1           0x20                                                                # Place 1 byte item on stack.
 904 [1786 0x6fa] DUP2                                                                                # Duplicate 2nd stack item.
 905 [1787 0x6fb] LT                                                                                  # Lesser-than comparison
 906 [1788 0x6fc] ISZERO                                                                              # Simple not operator
 907 [1789 0x6fd] PUSH2           0x0705                                                              # Place 2-byte item on stack.
 908 [1792 0x700] JUMPI           @0x705                                                              # Conditionally alter the program counter.

 909 [1793 0x701] PUSH1           0x00                                                                # Place 1 byte item on stack.
 910 [1795 0x703] DUP1                                                                                # Duplicate 1st stack item.
 911 [1796 0x704] REVERT                                                                              # throw an error
:loc_0x705
 912 [1797 0x705] JUMPDEST                                             JUMPI@0x700                    # Mark a valid destination for jumps.
 913 [1798 0x706] DUP2                                                                                # Duplicate 2nd stack item.
 914 [1799 0x707] ADD                                                                                 # Addition operation.
 915 [1800 0x708] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 916 [1801 0x709] DUP1                                                                                # Duplicate 1st stack item.
 917 [1802 0x70a] DUP1                                                                                # Duplicate 1st stack item.
 918 [1803 0x70b] MLOAD                                                                               # Load word from memory.
 919 [1804 0x70c] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 920 [1805 0x70d] PUSH1           0x20                                                                # Place 1 byte item on stack.
 921 [1807 0x70f] ADD                                                                                 # Addition operation.
 922 [1808 0x710] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 923 [1809 0x711] SWAP3                                                                               # Exchange 1st and 4th stack items.
 924 [1810 0x712] SWAP2                                                                               # Exchange 1st and 3rd stack items.
 925 [1811 0x713] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 926 [1812 0x714] POP                                                                                 # Remove item from stack.
 927 [1813 0x715] POP                                                                                 # Remove item from stack.
 928 [1814 0x716] POP                                                                                 # Remove item from stack.
 929 [1815 0x717] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 930 [1816 0x718] POP                                                                                 # Remove item from stack.
 931 [1817 0x719] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 932 [1818 0x71a] JUMP                                                                                # Alter the program counter.

:loc_0x71b
 933 [1819 0x71b] JUMPDEST                                             JUMP@0x273                     # Mark a valid destination for jumps.
 934 [1820 0x71c] PUSH1           0x02                                                                # Place 1 byte item on stack.
 935 [1822 0x71e] PUSH1           0x14                                                                # Place 1 byte item on stack.
 936 [1824 0x720] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 937 [1825 0x721] SLOAD                                                                               # Load word from storage.
 938 [1826 0x722] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 939 [1827 0x723] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 940 [1830 0x726] EXP                                                                                 # Exponential operation.
 941 [1831 0x727] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 942 [1832 0x728] DIV                                                                                 # Integer division operation.
 943 [1833 0x729] PUSH1           0xff                                                                # Place 1 byte item on stack.
 944 [1835 0x72b] AND                                                                                 # Bitwise AND operation.
 945 [1836 0x72c] DUP2                                                                                # Duplicate 2nd stack item.
 946 [1837 0x72d] JUMP                                                                                # Alter the program counter.

:loc_0x72e
 947 [1838 0x72e] JUMPDEST                                             JUMP@0x2ce                     # Mark a valid destination for jumps.
 948 [1839 0x72f] PUSH1           0x00                                                                # Place 1 byte item on stack.
 949 [1841 0x731] DUP1                                                                                # Duplicate 1st stack item.
 950 [1842 0x732] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 951 [1843 0x733] SLOAD                                                                               # Load word from storage.
 952 [1844 0x734] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 953 [1845 0x735] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 954 [1848 0x738] EXP                                                                                 # Exponential operation.
 955 [1849 0x739] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 956 [1850 0x73a] DIV                                                                                 # Integer division operation.
 957 [1851 0x73b] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 958 [1872 0x750] AND                                                                                 # Bitwise AND operation.
 959 [1873 0x751] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 960 [1894 0x766] AND                                                                                 # Bitwise AND operation.
 961 [1895 0x767] CALLER                                                                              # Get caller address.This is the address of the account that is directly responsible for this execution.
 962 [1896 0x768] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 963 [1917 0x77d] AND                                                                                 # Bitwise AND operation.
 964 [1918 0x77e] EQ                                                                                  # Equality  comparison
 965 [1919 0x77f] ISZERO                                                                              # Simple not operator
 966 [1920 0x780] ISZERO                                                                              # Simple not operator
 967 [1921 0x781] PUSH2           0x0789                                                              # Place 2-byte item on stack.
 968 [1924 0x784] JUMPI           @0x789                                                              # Conditionally alter the program counter.

 969 [1925 0x785] PUSH1           0x00                                                                # Place 1 byte item on stack.
 970 [1927 0x787] DUP1                                                                                # Duplicate 1st stack item.
 971 [1928 0x788] REVERT                                                                              # throw an error
:loc_0x789
 972 [1929 0x789] JUMPDEST                                             JUMPI@0x784                    # Mark a valid destination for jumps.
 973 [1930 0x78a] PUSH1           0x00                                                                # Place 1 byte item on stack.
 974 [1932 0x78c] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 975 [1953 0x7a1] AND                                                                                 # Bitwise AND operation.
 976 [1954 0x7a2] DUP2                                                                                # Duplicate 2nd stack item.
 977 [1955 0x7a3] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 978 [1976 0x7b8] AND                                                                                 # Bitwise AND operation.
 979 [1977 0x7b9] EQ                                                                                  # Equality  comparison
 980 [1978 0x7ba] ISZERO                                                                              # Simple not operator
 981 [1979 0x7bb] ISZERO                                                                              # Simple not operator
 982 [1980 0x7bc] ISZERO                                                                              # Simple not operator
 983 [1981 0x7bd] PUSH2           0x07c5                                                              # Place 2-byte item on stack.
 984 [1984 0x7c0] JUMPI           @0x7c5                                                              # Conditionally alter the program counter.

 985 [1985 0x7c1] PUSH1           0x00                                                                # Place 1 byte item on stack.
 986 [1987 0x7c3] DUP1                                                                                # Duplicate 1st stack item.
 987 [1988 0x7c4] REVERT                                                                              # throw an error
:loc_0x7c5
 988 [1989 0x7c5] JUMPDEST                                             JUMPI@0x7c0                    # Mark a valid destination for jumps.
 989 [1990 0x7c6] DUP1                                                                                # Duplicate 1st stack item.
 990 [1991 0x7c7] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
 991 [2012 0x7dc] AND                                                                                 # Bitwise AND operation.
 992 [2013 0x7dd] PUSH1           0x00                                                                # Place 1 byte item on stack.
 993 [2015 0x7df] DUP1                                                                                # Duplicate 1st stack item.
 994 [2016 0x7e0] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 995 [2017 0x7e1] SLOAD                                                                               # Load word from storage.
 996 [2018 0x7e2] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 997 [2019 0x7e3] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 998 [2022 0x7e6] EXP                                                                                 # Exponential operation.
 999 [2023 0x7e7] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1000 [2024 0x7e8] DIV                                                                                 # Integer division operation.
1001 [2025 0x7e9] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
1002 [2046 0x7fe] AND                                                                                 # Bitwise AND operation.
1003 [2047 0x7ff] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
1004 [2068 0x814] AND                                                                                 # Bitwise AND operation.
1005 [2069 0x815] PUSH32          0x8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e0                                # Place 32-byte (full word) item on stack.
1006 [2102 0x836] PUSH1           0x40                                                                # Place 1 byte item on stack.
1007 [2104 0x838] MLOAD                                                                               # Load word from memory.
1008 [2105 0x839] PUSH1           0x40                                                                # Place 1 byte item on stack.
1009 [2107 0x83b] MLOAD                                                                               # Load word from memory.
1010 [2108 0x83c] DUP1                                                                                # Duplicate 1st stack item.
1011 [2109 0x83d] SWAP2                                                                               # Exchange 1st and 3rd stack items.
1012 [2110 0x83e] SUB                                                                                 # Subtraction operation.
1013 [2111 0x83f] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1014 [2112 0x840] LOG3            0x806000                                                            # Append log record with three topics.
1015 [2116 0x844] DUP1                                                                                # Duplicate 1st stack item.
1016 [2117 0x845] PUSH2           0x0100                                                              # Place 2-byte item on stack.
1017 [2120 0x848] EXP                                                                                 # Exponential operation.
1018 [2121 0x849] DUP2                                                                                # Duplicate 2nd stack item.
1019 [2122 0x84a] SLOAD                                                                               # Load word from storage.
1020 [2123 0x84b] DUP2                                                                                # Duplicate 2nd stack item.
1021 [2124 0x84c] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
1022 [2145 0x861] MUL                                                                                 # Multiplication operation.
1023 [2146 0x862] NOT                                                                                 # Bitwise NOT operation.
1024 [2147 0x863] AND                                                                                 # Bitwise AND operation.
1025 [2148 0x864] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1026 [2149 0x865] DUP4                                                                                # Duplicate 4th stack item.
1027 [2150 0x866] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
1028 [2171 0x87b] AND                                                                                 # Bitwise AND operation.
1029 [2172 0x87c] MUL                                                                                 # Multiplication operation.
1030 [2173 0x87d] OR                                                                                  # Bitwise OR operation.
1031 [2174 0x87e] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1032 [2175 0x87f] SSTORE                                                                              # Save word to storage.
1033 [2176 0x880] POP                                                                                 # Remove item from stack.
1034 [2177 0x881] POP                                                                                 # Remove item from stack.
1035 [2178 0x882] JUMP                                                                                # Alter the program counter.

:loc_0x883
1036 [2179 0x883] JUMPDEST                                             JUMP@0x2e5                     # Mark a valid destination for jumps.
1037 [2180 0x884] PUSH1           0x00                                                                # Place 1 byte item on stack.
1038 [2182 0x886] DUP1                                                                                # Duplicate 1st stack item.
1039 [2183 0x887] PUSH1           0x00                                                                # Place 1 byte item on stack.
1040 [2185 0x889] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1041 [2186 0x88a] SLOAD                                                                               # Load word from storage.
1042 [2187 0x88b] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1043 [2188 0x88c] PUSH2           0x0100                                                              # Place 2-byte item on stack.
1044 [2191 0x88f] EXP                                                                                 # Exponential operation.
1045 [2192 0x890] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1046 [2193 0x891] DIV                                                                                 # Integer division operation.
1047 [2194 0x892] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
1048 [2215 0x8a7] AND                                                                                 # Bitwise AND operation.
1049 [2216 0x8a8] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
1050 [2237 0x8bd] AND                                                                                 # Bitwise AND operation.
1051 [2238 0x8be] CALLER                                                                              # Get caller address.This is the address of the account that is directly responsible for this execution.
1052 [2239 0x8bf] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                                # Place 20-byte item on stack.
1053 [2260 0x8d4] AND                                                                                 # Bitwise AND operation.
1054 [2261 0x8d5] EQ                                                                                  # Equality  comparison
1055 [2262 0x8d6] ISZERO                                                                              # Simple not operator
1056 [2263 0x8d7] ISZERO                                                                              # Simple not operator
1057 [2264 0x8d8] PUSH2           0x08e0                                                              # Place 2-byte item on stack.
1058 [2267 0x8db] JUMPI           @0x8e0                                                              # Conditionally alter the program counter.

1059 [2268 0x8dc] PUSH1           0x00                                                                # Place 1 byte item on stack.
1060 [2270 0x8de] DUP1                                                                                # Duplicate 1st stack item.
1061 [2271 0x8df] REVERT                                                                              # throw an error
:loc_0x8e0
1062 [2272 0x8e0] JUMPDEST                                             JUMPI@0x8db                    # Mark a valid destination for jumps.
1063 [2273 0x8e1] PUSH1           0x02                                                                # Place 1 byte item on stack.
1064 [2275 0x8e3] PUSH1           0x14                                                                # Place 1 byte item on stack.
1065 [2277 0x8e5] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1066 [2278 0x8e6] SLOAD                                                                               # Load word from storage.
1067 [2279 0x8e7] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1068 [2280 0x8e8] PUSH2           0x0100                                                              # Place 2-byte item on stack.
1069 [2283 0x8eb] EXP                                                                                 # Exponential operation.
1070 [2284 0x8ec] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1071 [2285 0x8ed] DIV                                                                                 # Integer division operation.
1072 [2286 0x8ee] PUSH1           0xff                                                                # Place 1 byte item on stack.
1073 [2288 0x8f0] AND                                                                                 # Bitwise AND operation.
1074 [2289 0x8f1] ISZERO                                                                              # Simple not operator
1075 [2290 0x8f2] ISZERO                                                                              # Simple not operator
1076 [2291 0x8f3] ISZERO                                                                              # Simple not operator
1077 [2292 0x8f4] PUSH2           0x08fc                                                              # Place 2-byte item on stack.
1078 [2295 0x8f7] JUMPI           @0x8fc                                                              # Conditionally alter the program counter.

1079 [2296 0x8f8] PUSH1           0x00                                                                # Place 1 byte item on stack.
1080 [2298 0x8fa] DUP1                                                                                # Duplicate 1st stack item.
1081 [2299 0x8fb] REVERT                                                                              # throw an error
:loc_0x8fc
1082 [2300 0x8fc] JUMPDEST                                             JUMPI@0x8f7                    # Mark a valid destination for jumps.
1083 [2301 0x8fd] PUSH1           0x00                                                                # Place 1 byte item on stack.
1084 [2303 0x8ff] PUSH2           0x0906                                                              # Place 2-byte item on stack.
1085 [2306 0x902] PUSH2           0x061c                                                              # Place 2-byte item on stack.
1086 [2309 0x905] JUMP            @0x61c                                                              # Alter the program counter.

:loc_0x906
1087 [2310 0x906] JUMPDEST                                                                            # Mark a valid destination for jumps.
1088 [2311 0x907] GT                                                                                  # Greater-than comparison
1089 [2312 0x908] ISZERO                                                                              # Simple not operator
1090 [2313 0x909] ISZERO                                                                              # Simple not operator
1091 [2314 0x90a] PUSH2           0x0912                                                              # Place 2-byte item on stack.
1092 [2317 0x90d] JUMPI           @0x912                                                              # Conditionally alter the program counter.

1093 [2318 0x90e] PUSH1           0x00                                                                # Place 1 byte item on stack.
1094 [2320 0x910] DUP1                                                                                # Duplicate 1st stack item.
1095 [2321 0x911] REVERT                                                                              # throw an error
:loc_0x912
1096 [2322 0x912] JUMPDEST                                             JUMPI@0x90d                    # Mark a valid destination for jumps.
1097 [2323 0x913] TIMESTAMP                                                                           # Get the block’s timestamp.
1098 [2324 0x914] PUSH1           0x03                                                                # Place 1 byte item on stack.
1099 [2326 0x916] DUP2                                                                                # Duplicate 2nd stack item.
1100 [2327 0x917] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1101 [2328 0x918] SSTORE                                                                              # Save word to storage.
1102 [2329 0x919] POP                                                                                 # Remove item from stack.
1103 [2330 0x91a] PUSH2           0x0930                                                              # Place 2-byte item on stack.
1104 [2333 0x91d] PUSH1           0x05                                                                # Place 1 byte item on stack.
1105 [2335 0x91f] SLOAD                                                                               # Load word from storage.
1106 [2336 0x920] PUSH1           0x03                                                                # Place 1 byte item on stack.
1107 [2338 0x922] SLOAD                                                                               # Load word from storage.
1108 [2339 0x923] PUSH2           0x0967                                                              # Place 2-byte item on stack.
1109 [2342 0x926] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1110 [2343 0x927] SWAP2                                                                               # Exchange 1st and 3rd stack items.
1111 [2344 0x928] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1112 [2345 0x929] PUSH4           0xffffffff                                                          # Place 4-byte item on stack.
1113 [2350 0x92e] AND                                                                                 # Bitwise AND operation.
1114 [2351 0x92f] JUMP                                                                                # Alter the program counter.

:loc_0x930
1115 [2352 0x930] JUMPDEST                                                                            # Mark a valid destination for jumps.
1116 [2353 0x931] PUSH1           0x04                                                                # Place 1 byte item on stack.
1117 [2355 0x933] DUP2                                                                                # Duplicate 2nd stack item.
1118 [2356 0x934] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1119 [2357 0x935] SSTORE                                                                              # Save word to storage.
1120 [2358 0x936] POP                                                                                 # Remove item from stack.
1121 [2359 0x937] PUSH1           0x01                                                                # Place 1 byte item on stack.
1122 [2361 0x939] PUSH1           0x02                                                                # Place 1 byte item on stack.
1123 [2363 0x93b] PUSH1           0x14                                                                # Place 1 byte item on stack.
1124 [2365 0x93d] PUSH2           0x0100                                                              # Place 2-byte item on stack.
1125 [2368 0x940] EXP                                                                                 # Exponential operation.
1126 [2369 0x941] DUP2                                                                                # Duplicate 2nd stack item.
1127 [2370 0x942] SLOAD                                                                               # Load word from storage.
1128 [2371 0x943] DUP2                                                                                # Duplicate 2nd stack item.
1129 [2372 0x944] PUSH1           0xff                                                                # Place 1 byte item on stack.
1130 [2374 0x946] MUL                                                                                 # Multiplication operation.
1131 [2375 0x947] NOT                                                                                 # Bitwise NOT operation.
1132 [2376 0x948] AND                                                                                 # Bitwise AND operation.
1133 [2377 0x949] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1134 [2378 0x94a] DUP4                                                                                # Duplicate 4th stack item.
1135 [2379 0x94b] ISZERO                                                                              # Simple not operator
1136 [2380 0x94c] ISZERO                                                                              # Simple not operator
1137 [2381 0x94d] MUL                                                                                 # Multiplication operation.
1138 [2382 0x94e] OR                                                                                  # Bitwise OR operation.
1139 [2383 0x94f] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1140 [2384 0x950] SSTORE                                                                              # Save word to storage.
1141 [2385 0x951] POP                                                                                 # Remove item from stack.
1142 [2386 0x952] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1143 [2387 0x953] JUMP                                                                                # Alter the program counter.

:loc_0x954
1144 [2388 0x954] JUMPDEST                                             JUMP@0x314                     # Mark a valid destination for jumps.
1145 [2389 0x955] PUSH1           0x02                                                                # Place 1 byte item on stack.
1146 [2391 0x957] PUSH1           0x15                                                                # Place 1 byte item on stack.
1147 [2393 0x959] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1148 [2394 0x95a] SLOAD                                                                               # Load word from storage.
1149 [2395 0x95b] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1150 [2396 0x95c] PUSH2           0x0100                                                              # Place 2-byte item on stack.
1151 [2399 0x95f] EXP                                                                                 # Exponential operation.
1152 [2400 0x960] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1153 [2401 0x961] DIV                                                                                 # Integer division operation.
1154 [2402 0x962] PUSH1           0xff                                                                # Place 1 byte item on stack.
1155 [2404 0x964] AND                                                                                 # Bitwise AND operation.
1156 [2405 0x965] DUP2                                                                                # Duplicate 2nd stack item.
1157 [2406 0x966] JUMP                                                                                # Alter the program counter.

:loc_0x967
1158 [2407 0x967] JUMPDEST                                                                            # Mark a valid destination for jumps.
1159 [2408 0x968] PUSH1           0x00                                                                # Place 1 byte item on stack.
1160 [2410 0x96a] DUP1                                                                                # Duplicate 1st stack item.
1161 [2411 0x96b] DUP3                                                                                # Duplicate 3rd stack item.
1162 [2412 0x96c] DUP5                                                                                # Duplicate 5th stack item.
1163 [2413 0x96d] ADD                                                                                 # Addition operation.
1164 [2414 0x96e] SWAP1                                                                               # Exchange 1st and 2nd stack items.
1165 [2415 0x96f] POP                                                                                 # Remove item from stack.
1166 [2416 0x970] DUP4                                                                                # Duplicate 4th stack item.
1167 [2417 0x971] DUP2                                                                                # Duplicate 2nd stack item.
1168 [2418 0x972] LT                                                                                  # Lesser-than comparison
1169 [2419 0x973] ISZERO                                                                              # Simple not operator
1170 [2420 0x974] ISZERO                                                                              # Simple not operator
1171 [2421 0x975] ISZERO                                                                              # Simple not operator
1172 [2422 0x976] PUSH2           0x097b                                                              # Place 2-byte item on stack.
1173 [2425 0x979] JUMPI           @0x97b                                                              # Conditionally alter the program counter.

1174 [2426 0x97a] UNKNOWN_0xfe                                                                        # Invalid opcode
:loc_0x97b
1175 [2427 0x97b] JUMPDEST                                             JUMPI@0x979                    # Mark a valid destination for jumps.
1176 [2428 0x97c] DUP1                                                                                # Duplicate 1st stack item.
1177 [2429 0x97d] SWAP2                                                                               # Exchange 1st and 3rd stack items.
1178 [2430 0x97e] POP                                                                                 # Remove item from stack.
1179 [2431 0x97f] POP                                                                                 # Remove item from stack.
1180 [2432 0x980] SWAP3                                                                               # Exchange 1st and 4th stack items.
1181 [2433 0x981] SWAP2                                                                               # Exchange 1st and 3rd stack items.
1182 [2434 0x982] POP                                                                                 # Remove item from stack.
1183 [2435 0x983] POP                                                                                 # Remove item from stack.
1184 [2436 0x984] JUMP                                                                                # Alter the program counter.

1185 [2437 0x985] STOP                                                                                # Halts execution.

1186 [2438 0x986] LOG1            0x65                                                                # Append log record with one topic.
1187 [2440 0x988] PUSH3           0x7a7a72                                                            # Place 3-byte item on stack.
1188 [2444 0x98c] ADDRESS                                                                             # Get address of currently executing account.
1189 [2445 0x98d] PC                                                                                  # Get the value of the program counter prior to the increment.
1190 [2446 0x98e] SHA3                                                                                # Compute Keccak-256 hash.
1191 [2447 0x98f] PUSH10          0x642cdfbf8b49cb944b12                                              # Place 10-byte item on stack.
1192 [2458 0x99a] ORIGIN                                                                              # Get execution origination address.
1193 [2459 0x99b] DUP11                                                                               # Duplicate 11th stack item.
1194 [2460 0x99c] UNKNOWN_0xdd                                                                        # Invalid opcode
1195 [2461 0x99d] UNKNOWN_0x2c                                                                        # Invalid opcode
1196 [2462 0x99e] DUP2                                                                                # Duplicate 2nd stack item.
1197 [2463 0x99f] UNKNOWN_0xc3                                                                        # Invalid opcode
1198 [2464 0x9a0] SSTORE                                                                              # Save word to storage.
1199 [2465 0x9a1] PUSH23          0x00ed88f94b907c0d547a6251db0029                                    # Place 23-byte item on stack.
```
