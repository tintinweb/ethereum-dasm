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

       example: evmdasm.py [-L -F -v] <file_or_bytecode>
                evmdasm.py [-L -F -v] # read from stdin


Options:
  -h, --help            show this help message and exit
  -v VERBOSITY, --verbosity=VERBOSITY
                        available loglevels:
                        critical,fatal,error,warning,warn,info,debug,notset
                        [default: critical]
  -L, --listing         disables table mode, outputs assembly only
  -f, --lookup-function-signature
                        enable online function signature lookup

```
    #> echo "0x12345678" | python evmdasm.py -v critical
    #> python evmdasm.py -v critical "0x12345678"
    #> python evmdasm.py -v critical ether_contract.evm


## examples

* disasm with basic jumptable analysis (incomplete)
```python
#> python evmdasm.py -f 60806040526000600260146101000a81548160ff0219169083151502179055506000600260156101000a81548160ff0219169083151502179055506301caca0060055534801561004e57600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555073aa1ae5e57dc05981d83ec7fca0b3c7ee2565b7d6600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555073ad7f8e3d2df049c8ea32cd6c4252e1a77b6c3005600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506109b1806101486000396000f3006080604052600436106100ba576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806316243356146100bf57806338af3eed146100ea5780636e15266a14610141578063834ee4171461016c57806386d1a69f146101975780638da5cb5b146101ae5780639b7faaf0146102055780639e1a4d1914610234578063a4e2d6341461025f578063f2fde38b1461028e578063f83d08ba146102d1578063fa2a899714610300575b600080fd5b3480156100cb57600080fd5b506100d461032f565b6040518082815260200191505060405180910390f35b3480156100f657600080fd5b506100ff610335565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561014d57600080fd5b5061015661035b565b6040518082815260200191505060405180910390f35b34801561017857600080fd5b50610181610361565b6040518082815260200191505060405180910390f35b3480156101a357600080fd5b506101ac610367565b005b3480156101ba57600080fd5b506101c36105e6565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561021157600080fd5b5061021a61060b565b604051808215151515815260200191505060405180910390f35b34801561024057600080fd5b5061024961061c565b6040518082815260200191505060405180910390f35b34801561026b57600080fd5b5061027461071b565b604051808215151515815260200191505060405180910390f35b34801561029a57600080fd5b506102cf600480360381019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061072e565b005b3480156102dd57600080fd5b506102e6610883565b604051808215151515815260200191505060405180910390f35b34801561030c57600080fd5b50610315610954565b604051808215151515815260200191505060405180910390f35b60045481565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60055481565b60035481565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156103c457600080fd5b600260149054906101000a900460ff1615156103df57600080fd5b600260159054906101000a900460ff161515156103fb57600080fd5b61040361060b565b151561040e57600080fd5b61041661061c565b9050600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1663a9059cbb600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16836040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050602060405180830381600087803b1580156104ff57600080fd5b505af1158015610513573d6000803e3d6000fd5b505050506040513d602081101561052957600080fd5b8101908080519060200190929190505050507f9cf9e3ab58b33f06d81842ea0ad850b6640c6430d6396973312e1715792e7a91600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1682604051808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018281526020019250505060405180910390a16001600260156101000a81548160ff02191690831515021790555050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600080429050600454811191505090565b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166370a08231306040518263ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001915050602060405180830381600087803b1580156106db57600080fd5b505af11580156106ef573d6000803e3d6000fd5b505050506040513d602081101561070557600080fd5b8101908080519060200190929190505050905090565b600260149054906101000a900460ff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561078957600080fd5b600073ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16141515156107c557600080fd5b8073ffffffffffffffffffffffffffffffffffffffff166000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff167f8be0079c531659141344cd1fd0a4f28419497f9722a3daafe3b4186f6b6457e060405160405180910390a3806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161415156108e057600080fd5b600260149054906101000a900460ff161515156108fc57600080fd5b600061090661061c565b11151561091257600080fd5b4260038190555061093060055460035461096790919063ffffffff16565b6004819055506001600260146101000a81548160ff02191690831515021790555090565b600260159054906101000a900460ff1681565b600080828401905083811015151561097b57fe5b80915050929150505600a165627a7a7230582069642cdfbf8b49cb944b12328add2c81c3557600ed88f94b907c0d547a6251db0029

Inst addr  hex   mnemonic        operand                              xrefs                          description
------------------------------------------------------------------------------------------------------------------------------------------------------
   0 [  0 0x000] PUSH1           0x80                                                                # Place 1 byte item on stack.
   1 [  2 0x002] PUSH1           0x40                                                                # Place 1 byte item on stack.
   2 [  4 0x004] MSTORE                                                                              # Save word to memory.
   3 [  5 0x005] PUSH1           0x00                                                                # Place 1 byte item on stack.
   4 [  7 0x007] PUSH1           0x02                                                                # Place 1 byte item on stack.
   5 [  9 0x009] PUSH1           0x14                                                                # Place 1 byte item on stack.
   6 [ 11 0x00b] PUSH2           0x0100                                                              # Place 2-byte item on stack.
   7 [ 14 0x00e] EXP                                                                                 # Exponential operation.
   8 [ 15 0x00f] DUP2                                                                                # Duplicate 2nd stack item.
   9 [ 16 0x010] SLOAD                                                                               # Load word from storage.
  10 [ 17 0x011] DUP2                                                                                # Duplicate 2nd stack item.
  11 [ 18 0x012] PUSH1           0xff                                                                # Place 1 byte item on stack.
  12 [ 20 0x014] MUL                                                                                 # Multiplication operation.
  13 [ 21 0x015] NOT                                                                                 # Bitwise NOT operation.
  14 [ 22 0x016] AND                                                                                 # Bitwise AND operation.
  15 [ 23 0x017] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  16 [ 24 0x018] DUP4                                                                                # Duplicate 4th stack item.
  17 [ 25 0x019] ISZERO                                                                              # Simple not operator
  18 [ 26 0x01a] ISZERO                                                                              # Simple not operator
  19 [ 27 0x01b] MUL                                                                                 # Multiplication operation.
  20 [ 28 0x01c] OR                                                                                  # Bitwise OR operation.
  21 [ 29 0x01d] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  22 [ 30 0x01e] SSTORE                                                                              # Save word to storage.
  23 [ 31 0x01f] POP                                                                                 # Remove item from stack.
  24 [ 32 0x020] PUSH1           0x00                                                                # Place 1 byte item on stack.
  25 [ 34 0x022] PUSH1           0x02                                                                # Place 1 byte item on stack.
  26 [ 36 0x024] PUSH1           0x15                                                                # Place 1 byte item on stack.
  27 [ 38 0x026] PUSH2           0x0100                                                              # Place 2-byte item on stack.
  28 [ 41 0x029] EXP                                                                                 # Exponential operation.
  29 [ 42 0x02a] DUP2                                                                                # Duplicate 2nd stack item.
  30 [ 43 0x02b] SLOAD                                                                               # Load word from storage.
  31 [ 44 0x02c] DUP2                                                                                # Duplicate 2nd stack item.
  32 [ 45 0x02d] PUSH1           0xff                                                                # Place 1 byte item on stack.
  33 [ 47 0x02f] MUL                                                                                 # Multiplication operation.
  34 [ 48 0x030] NOT                                                                                 # Bitwise NOT operation.
  35 [ 49 0x031] AND                                                                                 # Bitwise AND operation.
  36 [ 50 0x032] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  37 [ 51 0x033] DUP4                                                                                # Duplicate 4th stack item.
  38 [ 52 0x034] ISZERO                                                                              # Simple not operator
  39 [ 53 0x035] ISZERO                                                                              # Simple not operator
  40 [ 54 0x036] MUL                                                                                 # Multiplication operation.
  41 [ 55 0x037] OR                                                                                  # Bitwise OR operation.
  42 [ 56 0x038] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  43 [ 57 0x039] SSTORE                                                                              # Save word to storage.
  44 [ 58 0x03a] POP                                                                                 # Remove item from stack.
  45 [ 59 0x03b] PUSH4           0x01caca00                                                          # Place 4-byte item on stack.
  46 [ 64 0x040] PUSH1           0x05                                                                # Place 1 byte item on stack.
  47 [ 66 0x042] SSTORE                                                                              # Save word to storage.
  48 [ 67 0x043] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
  49 [ 68 0x044] DUP1                                                                                # Duplicate 1st stack item.
  50 [ 69 0x045] ISZERO                                                                              # Simple not operator
  51 [ 70 0x046] PUSH2           0x004e                                                              # Place 2-byte item on stack.
  52 [ 73 0x049] JUMPI           @0x4e                                                               # Conditionally alter the program counter.

  53 [ 74 0x04a] PUSH1           0x00                                                                # Place 1 byte item on stack.
  54 [ 76 0x04c] DUP1                                                                                # Duplicate 1st stack item.
  55 [ 77 0x04d] REVERT                                                                              # throw an error
:loc_0x4e
  56 [ 78 0x04e] JUMPDEST                                             JUMPI@0x49                     # Mark a valid destination for jumps.
  57 [ 79 0x04f] POP                                                                                 # Remove item from stack.
  58 [ 80 0x050] CALLER                                                                              # Get caller address.This is the address of the account that is directly responsible for this execution.
  59 [ 81 0x051] PUSH1           0x00                                                                # Place 1 byte item on stack.
  60 [ 83 0x053] DUP1                                                                                # Duplicate 1st stack item.
  61 [ 84 0x054] PUSH2           0x0100                                                              # Place 2-byte item on stack.
  62 [ 87 0x057] EXP                                                                                 # Exponential operation.
  63 [ 88 0x058] DUP2                                                                                # Duplicate 2nd stack item.
  64 [ 89 0x059] SLOAD                                                                               # Load word from storage.
  65 [ 90 0x05a] DUP2                                                                                # Duplicate 2nd stack item.
  66 [ 91 0x05b] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                          # Place 20-byte item on stack.
  67 [112 0x070] MUL                                                                                 # Multiplication operation.
  68 [113 0x071] NOT                                                                                 # Bitwise NOT operation.
  69 [114 0x072] AND                                                                                 # Bitwise AND operation.
  70 [115 0x073] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  71 [116 0x074] DUP4                                                                                # Duplicate 4th stack item.
  72 [117 0x075] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                          # Place 20-byte item on stack.
  73 [138 0x08a] AND                                                                                 # Bitwise AND operation.
  74 [139 0x08b] MUL                                                                                 # Multiplication operation.
  75 [140 0x08c] OR                                                                                  # Bitwise OR operation.
  76 [141 0x08d] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  77 [142 0x08e] SSTORE                                                                              # Save word to storage.
  78 [143 0x08f] POP                                                                                 # Remove item from stack.
  79 [144 0x090] PUSH20          0xaa1ae5e57dc05981d83ec7fca0b3c7ee2565b7d6                          # Place 20-byte item on stack.
  80 [165 0x0a5] PUSH1           0x01                                                                # Place 1 byte item on stack.
  81 [167 0x0a7] PUSH1           0x00                                                                # Place 1 byte item on stack.
  82 [169 0x0a9] PUSH2           0x0100                                                              # Place 2-byte item on stack.
  83 [172 0x0ac] EXP                                                                                 # Exponential operation.
  84 [173 0x0ad] DUP2                                                                                # Duplicate 2nd stack item.
  85 [174 0x0ae] SLOAD                                                                               # Load word from storage.
  86 [175 0x0af] DUP2                                                                                # Duplicate 2nd stack item.
  87 [176 0x0b0] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                          # Place 20-byte item on stack.
  88 [197 0x0c5] MUL                                                                                 # Multiplication operation.
  89 [198 0x0c6] NOT                                                                                 # Bitwise NOT operation.
  90 [199 0x0c7] AND                                                                                 # Bitwise AND operation.
  91 [200 0x0c8] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  92 [201 0x0c9] DUP4                                                                                # Duplicate 4th stack item.
  93 [202 0x0ca] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                          # Place 20-byte item on stack.
  94 [223 0x0df] AND                                                                                 # Bitwise AND operation.
  95 [224 0x0e0] MUL                                                                                 # Multiplication operation.
  96 [225 0x0e1] OR                                                                                  # Bitwise OR operation.
  97 [226 0x0e2] SWAP1                                                                               # Exchange 1st and 2nd stack items.
  98 [227 0x0e3] SSTORE                                                                              # Save word to storage.
  99 [228 0x0e4] POP                                                                                 # Remove item from stack.
 100 [229 0x0e5] PUSH20          0xad7f8e3d2df049c8ea32cd6c4252e1a77b6c3005                          # Place 20-byte item on stack.
 101 [250 0x0fa] PUSH1           0x02                                                                # Place 1 byte item on stack.
 102 [252 0x0fc] PUSH1           0x00                                                                # Place 1 byte item on stack.
 103 [254 0x0fe] PUSH2           0x0100                                                              # Place 2-byte item on stack.
 104 [257 0x101] EXP                                                                                 # Exponential operation.
 105 [258 0x102] DUP2                                                                                # Duplicate 2nd stack item.
 106 [259 0x103] SLOAD                                                                               # Load word from storage.
 107 [260 0x104] DUP2                                                                                # Duplicate 2nd stack item.
 108 [261 0x105] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                          # Place 20-byte item on stack.
 109 [282 0x11a] MUL                                                                                 # Multiplication operation.
 110 [283 0x11b] NOT                                                                                 # Bitwise NOT operation.
 111 [284 0x11c] AND                                                                                 # Bitwise AND operation.
 112 [285 0x11d] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 113 [286 0x11e] DUP4                                                                                # Duplicate 4th stack item.
 114 [287 0x11f] PUSH20          0xffffffffffffffffffffffffffffffffffffffff                          # Place 20-byte item on stack.
 115 [308 0x134] AND                                                                                 # Bitwise AND operation.
 116 [309 0x135] MUL                                                                                 # Multiplication operation.
 117 [310 0x136] OR                                                                                  # Bitwise OR operation.
 118 [311 0x137] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 119 [312 0x138] SSTORE                                                                              # Save word to storage.
 120 [313 0x139] POP                                                                                 # Remove item from stack.
 121 [314 0x13a] PUSH2           0x09b1                                                              # Place 2-byte item on stack.
 122 [317 0x13d] DUP1                                                                                # Duplicate 1st stack item.
 123 [318 0x13e] PUSH2           0x0148                                                              # Place 2-byte item on stack.
 124 [321 0x141] PUSH1           0x00                                                                # Place 1 byte item on stack.
 125 [323 0x143] CODECOPY                                                                            # Copy code running in current environment to memory.
 126 [324 0x144] PUSH1           0x00                                                                # Place 1 byte item on stack.
 127 [326 0x146] RETURN                                                                              # Halt execution returning output data.

 128 [327 0x147] STOP                                                                                # Halts execution.

 129 [328 0x148] PUSH1           0x80                                                                # Place 1 byte item on stack.
 130 [330 0x14a] PUSH1           0x40                                                                # Place 1 byte item on stack.
 131 [332 0x14c] MSTORE                                                                              # Save word to memory.
 132 [333 0x14d] PUSH1           0x04                                                                # Place 1 byte item on stack.
 133 [335 0x14f] CALLDATASIZE                                                                        # Get size of input data in current environment.
 134 [336 0x150] LT                                                                                  # Lesser-than comparison
 135 [337 0x151] PUSH2           0x00ba                                                              # Place 2-byte item on stack.
 136 [340 0x154] JUMPI           @0xba                                                               # Conditionally alter the program counter.

 137 [341 0x155] PUSH1           0x00                                                                # Place 1 byte item on stack.
 138 [343 0x157] CALLDATALOAD                                                                        # Get input data of current environment.
 139 [344 0x158] PUSH29          0x0100000000000000000000000000000000000000000000000000000000        # Place 29-byte item on stack.
 140 [374 0x176] SWAP1                                                                               # Exchange 1st and 2nd stack items.
 141 [375 0x177] DIV                                                                                 # Integer division operation.
 142 [376 0x178] PUSH4           0xffffffff                                                          # Place 4-byte item on stack.
 143 [381 0x17d] AND                                                                                 # Bitwise AND operation.
 144 [382 0x17e] DUP1                                                                                # Duplicate 1st stack item.
 145 [383 0x17f] PUSH4           0x16243356                                                          # Place 4-byte item on stack.
 146 [388 0x184] EQ                                                                                  # Equality  comparison
 147 [389 0x185] PUSH2           0x00bf                                                              # Place 2-byte item on stack.
 148 [392 0x188] JUMPI           @0xbf                                                               # Conditionally alter the program counter.

 149 [393 0x189] DUP1                                                                                # Duplicate 1st stack item.
 150 [394 0x18a] PUSH4           0x38af3eed  ('function beneficiary()')                              # Place 4-byte item on stack.
 151 [399 0x18f] EQ                                                                                  # Equality  comparison
 152 [400 0x190] PUSH2           0x00ea                                                              # Place 2-byte item on stack.
 153 [403 0x193] JUMPI           @0xea                                                               # Conditionally alter the program counter.

 154 [404 0x194] DUP1                                                                                # Duplicate 1st stack item.
 155 [405 0x195] PUSH4           0x6e15266a                                                          # Place 4-byte item on stack.
 156 [410 0x19a] EQ                                                                                  # Equality  comparison
 157 [411 0x19b] PUSH2           0x0141                                                              # Place 2-byte item on stack.
 158 [414 0x19e] JUMPI           @0x141                                                              # Conditionally alter the program counter.

 159 [415 0x19f] DUP1                                                                                # Duplicate 1st stack item.
 160 [416 0x1a0] PUSH4           0x834ee417                                                          # Place 4-byte item on stack.
 161 [421 0x1a5] EQ                                                                                  # Equality  comparison
 162 [422 0x1a6] PUSH2           0x016c                                                              # Place 2-byte item on stack.
 163 [425 0x1a9] JUMPI           @0x16c                                                              # Conditionally alter the program counter.

 164 [426 0x1aa] DUP1                                                                                # Duplicate 1st stack item.
 165 [427 0x1ab] PUSH4           0x86d1a69f  ('function release()')                                  # Place 4-byte item on stack.
 166 [432 0x1b0] EQ                                                                                  # Equality  comparison
 167 [433 0x1b1] PUSH2           0x0197                                                              # Place 2-byte item on stack.
 168 [436 0x1b4] JUMPI           @0x197                                                              # Conditionally alter the program counter.

 169 [437 0x1b5] DUP1                                                                                # Duplicate 1st stack item.
 170 [438 0x1b6] PUSH4           0x8da5cb5b  (*ambiguous* 'function ideal_warn_timed(uint256,uint128)')  # Place 4-byte item on stack.
 171 [443 0x1bb] EQ                                                                                  # Equality  comparison
 172 [444 0x1bc] PUSH2           0x01ae                                                              # Place 2-byte item on stack.
 173 [447 0x1bf] JUMPI           @0x1ae                                                              # Conditionally alter the program counter.

 174 [448 0x1c0] DUP1                                                                                # Duplicate 1st stack item.
 175 [449 0x1c1] PUSH4           0x9b7faaf0  ('function lockOver()')                                 # Place 4-byte item on stack.
 176 [454 0x1c6] EQ                                                                                  # Equality  comparison
 177 [455 0x1c7] PUSH2           0x0205                                                              # Place 2-byte item on stack.
 178 [458 0x1ca] JUMPI           @0x205                                                              # Conditionally alter the program counter.

 179 [459 0x1cb] DUP1                                                                                # Duplicate 1st stack item.
 180 [460 0x1cc] PUSH4           0x9e1a4d19  ('function tokenBalance()')                             # Place 4-byte item on stack.
 181 [465 0x1d1] EQ                                                                                  # Equality  comparison
 182 [466 0x1d2] PUSH2           0x0234                                                              # Place 2-byte item on stack.
 183 [469 0x1d5] JUMPI           @0x234                                                              # Conditionally alter the program counter.

 184 [470 0x1d6] DUP1                                                                                # Duplicate 1st stack item.
 185 [471 0x1d7] PUSH4           0xa4e2d634  ('function isLocked()')                                 # Place 4-byte item on stack.
 186 [476 0x1dc] EQ                                                                                  # Equality  comparison
 187 [477 0x1dd] PUSH2           0x025f                                                              # Place 2-byte item on stack.
 188 [480 0x1e0] JUMPI           @0x25f                                                              # Conditionally alter the program counter.

 189 [481 0x1e1] DUP1                                                                                # Duplicate 1st stack item.
 190 [482 0x1e2] PUSH4           0xf2fde38b  ('function transferOwnership(address)')                 # Place 4-byte item on stack.
 191 [487 0x1e7] EQ                                                                                  # Equality  comparison
 192 [488 0x1e8] PUSH2           0x028e                                                              # Place 2-byte item on stack.
 193 [491 0x1eb] JUMPI           @0x28e                                                              # Conditionally alter the program counter.

 194 [492 0x1ec] DUP1                                                                                # Duplicate 1st stack item.
 195 [493 0x1ed] PUSH4           0xf83d08ba  ('function lock()')                                     # Place 4-byte item on stack.
 196 [498 0x1f2] EQ                                                                                  # Equality  comparison
 197 [499 0x1f3] PUSH2           0x02d1                                                              # Place 2-byte item on stack.
 198 [502 0x1f6] JUMPI           @0x2d1                                                              # Conditionally alter the program counter.

 199 [503 0x1f7] DUP1                                                                                # Duplicate 1st stack item.
 200 [504 0x1f8] PUSH4           0xfa2a8997                                                          # Place 4-byte item on stack.
 201 [509 0x1fd] EQ                                                                                  # Equality  comparison
 202 [510 0x1fe] PUSH2           0x0300                                                              # Place 2-byte item on stack.
 203 [513 0x201] JUMPI           @0x300                                                              # Conditionally alter the program counter.

:loc_0x202
 204 [514 0x202] JUMPDEST                                                                            # Mark a valid destination for jumps.
 205 [515 0x203] PUSH1           0x00                                                                # Place 1 byte item on stack.
 206 [517 0x205] DUP1                                                                                # Duplicate 1st stack item.
 207 [518 0x206] REVERT                                                                              # throw an error
:loc_0x207
 208 [519 0x207] JUMPDEST                                                                            # Mark a valid destination for jumps.
 209 [520 0x208] CALLVALUE                                                                           # Get deposited value by the instruction/transaction responsible for this execution.
 210 [521 0x209] DUP1                                                                                # Duplicate 1st stack item.
 211 [522 0x20a] ISZERO                                                                              # Simple not operator
 212 [523 0x20b] PUSH2           0x00cb                                                              # Place 2-byte item on stack.
 213 [526 0x20e] JUMPI           @0xcb                                                               # Conditionally alter the program counter.

 214 [527 0x20f] PUSH1           0x00                                                                # Place 1 byte item on stack.
 215 [529 0x211] DUP1                                                                                # Duplicate 1st stack item.
 216 [530 0x212] REVERT                                                                              # throw an error
:loc_0x213
 217 [531 0x213] JUMPDEST                                                                            # Mark a valid destination for jumps.
 218 [532 0x214] POP                                                                                 # Remove item from stack.
 219 [533 0x215] PUSH2           0x00d4                                                              # Place 2-byte item on stack.
 220 [536 0x218] PUSH2           0x032f                                                              # Place 2-byte item on stack.
 221 [539 0x21b] JUMP            @0x32f                                                              # Alter the program counter.
```
