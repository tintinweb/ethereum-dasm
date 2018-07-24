#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

from ethereum_dasm.asm.registry import *

try:
    # optional terminal colors
    import colorama

    colorama.init(autoreset=True)
except ImportError:
    colorama = None


class Color:
    """
    Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Style: DIM, NORMAL, BRIGHT, RESET_ALL
    """

    @staticmethod
    def location(s):
        if not colorama:
            return s
        return colorama.Fore.WHITE + colorama.Style.BRIGHT + s + colorama.Style.RESET_ALL

    @staticmethod
    def instruction(s):
        if not colorama:
            return s

        if any(s.startswith(i) for i in INSTRUCTION_MARKS_BASICBLOCK_END):
            return colorama.Fore.YELLOW + colorama.Style.BRIGHT + s + colorama.Style.RESET_ALL
        elif s in ("ADD", "MUL", "SUB", "DIV", "SDIV", "MOD", "SMOD", "ADDMOD", "MULMOD", "EXP", "SIGNEXTEND"):
            return colorama.Fore.CYAN + s + colorama.Style.RESET_ALL
        elif s in ("LT", "GT", "SLT", "SGT", "EQ", "ISZERO", "AND", "OR", "XOR", "NOT", "BYTE", "SHL", "SHR", "SAR"):
            return colorama.Fore.MAGENTA + colorama.Style.BRIGHT + s + colorama.Style.RESET_ALL
        elif any(s.startswith(i) for i in ("PUSH", "POP", "SWAP", "DUP")):
            return colorama.Back.RESET + colorama.Fore.YELLOW + colorama.Style.DIM + s + colorama.Style.RESET_ALL
        elif any(s.startswith(i) for i in ("CREATE", "CALL", "CALLCODE", "DELEGATECALL", "STATICCALL", "REVERT",
                                           "SELFDESTRUCT", "CALLDATALOAD", "CALLDATACOPY", "EXTCODECOPY")):
            return colorama.Back.RESET + colorama.Fore.RED + colorama.Style.BRIGHT + s + colorama.Style.RESET_ALL
        elif any(i in s for i in ("LOAD", "STORE", "LOG")):
            return colorama.Back.RESET + colorama.Fore.GREEN + colorama.Style.NORMAL + s + colorama.Style.RESET_ALL
        elif s.startswith("UNKNOWN"):
            return colorama.Back.LIGHTRED_EX + s + colorama.Style.RESET_ALL

        return s

    @staticmethod
    def address(s, fmt="3d"):
        if not colorama:
            return fmt % s

        return colorama.Back.RESET + colorama.Fore.GREEN + colorama.Style.DIM + fmt % s + colorama.Style.RESET_ALL

    @staticmethod
    def gas(s, fmt="%3d"):
        if not colorama:
            return fmt % s

        if s <= 0:
            return colorama.Fore.YELLOW + colorama.Style.DIM + colorama.Back.LIGHTYELLOW_EX + fmt % s + colorama.Style.RESET_ALL
        elif s < 10:
            return colorama.Back.RESET + colorama.Fore.YELLOW + colorama.Style.DIM + fmt % s + colorama.Style.RESET_ALL
        elif s < 30:
            return colorama.Back.RESET + colorama.Fore.YELLOW + colorama.Style.NORMAL + fmt % s + colorama.Style.RESET_ALL
        else:
            return colorama.Fore.YELLOW + colorama.Style.BRIGHT + fmt % s + colorama.Style.RESET_ALL

    @staticmethod
    def description(s):
        if not colorama:
            return s
        return colorama.Style.DIM + colorama.Fore.GREEN + s + colorama.Style.RESET_ALL