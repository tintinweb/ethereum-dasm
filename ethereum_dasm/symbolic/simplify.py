#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

import z3
import logging
import mythril.laser.smt

logger = logging.getLogger(__name__)

def pp_hexint(a):
    return z3.z3printer.to_format(get_z3_value_hex(a))

z3.z3printer._Formatter.pp_bv = pp_hexint
z3.z3printer._Formatter.pp_int = pp_hexint
#z3.z3printer._z3_op_to_str[]


def format_comment_block(it, indent=0):
    s = [indent * " " + "/*******************************************************************"]
    for i in it:
        s.append((2+indent)*" "+ "%s" % i)
    s.append(indent*" "+ "*******************************************************************/")
    return "\n".join(s)

def get_z3_value_hex(item):

    if (type(item) == int):
        return hex(item)

    elif (type(item) == mythril.laser.smt.bitvec.BitVec and not item.symbolic):
        return hex(item.value)
    elif (type(item) == z3.BitVecNumRef):
        return hex(item.as_long())

    try:
        return hex(z3.simplify(item).as_long())
    except AttributeError:
        return str(z3.simplify(item)).replace("\n","\n    ")
    except z3.Z3Exception:
        return str(item).replace("\n","\n    ")

def get_z3_value(item):

    if (type(item) == int):
        return item

    elif (type(item) == mythril.laser.smt.bitvec.BitVec and not item.symbolic):
        return item.value
    elif (type(item) == z3.BitVecNumRef):
        return item.as_long()

    try:
        return z3.simplify(item).as_long()
    except AttributeError:
        return str(z3.simplify(item))
    except z3.Z3Exception:
        return str(item)


class MetaCode:

    @staticmethod
    def jump(asm_stmt):
        name = asm_stmt.evmcode.name_for_location.get(asm_stmt.instr.jumpto)
        name = "goto function_%s (LOC_%%(evm.pc)s)" % name if name else "goto LOC_%(evm.pc)s"

        return PseudoCodeStatement(asm=asm_stmt, fmt=name)

    @staticmethod
    def jumpi(asm_stmt):
        name = asm_stmt.evmcode.name_for_location.get(asm_stmt.instr.jumpto)
        name = "if (%%(condition)s) goto function_%s (LOC_%%(evm.pc)s)" % name if name else "if (%(condition)s) goto LOC_%(evm.pc)s"
        return PseudoCodeStatement(asm=asm_stmt, fmt=name)

    @staticmethod
    def jumpdest(asm_stmt):
        # funcsig = asm_stmt.evmcode.function_at.get(asm_stmt.instr.address)
        annotations = "\n"+format_comment_block(asm_stmt.instr.annotations, indent=2)+"\n" if asm_stmt.instr.annotations else ""

        name = asm_stmt.evmcode.name_for_location.get(asm_stmt.instr.address)
        name = "function_%s (LOC_%s)"%(name,hex(asm_stmt.instr.address)) if name else "LOC_%s"%hex(asm_stmt.instr.address)

        return PseudoCodeStatement(asm=asm_stmt, fmt=":%s %s"%(name,annotations))

    @staticmethod
    def cat_terminate(asm_stmt):
        return PseudoCodeStatement(asm=asm_stmt)

    @staticmethod
    def cat_event(asm_stmt):
        return PseudoCodeStatement(asm=asm_stmt)

    @staticmethod
    def cat_system(asm_stmt):
        return PseudoCodeStatement(asm=asm_stmt)

    @staticmethod
    def cat_storage(asm_stmt):
        if "STORE" not in asm_stmt.instr.name:
            return
        return PseudoCodeStatement(asm=asm_stmt,
                                   fmt=asm_stmt.instr.category+"[%(loc)s] = %(value)s")

    @staticmethod
    def cat_memory(asm_stmt):
        if "STORE" not in asm_stmt.instr.name:
            return
        return PseudoCodeStatement(asm=asm_stmt,
                                   fmt=asm_stmt.instr.category + "[%(offset)s] = %(value)s")



class AsmStatement(object):

    def __init__(self, instr, stack, evmcode):
        self.instr = instr
        self.stack = stack
        self.evmcode = evmcode

        self.args = tuple([])
        self.args_as_dict = {}
        self.returns = tuple([])
        self.returns_as_dict = {}
        try:
            self.stack_next = self.evmcode.symbolic_state_at[instr.next.address][0][1].mstate.stack
        except (KeyError, AttributeError):
            # keyerror: no state available
            # attributeerror: instr.next is none (last instr)
            self.stack_next = None  # stack unavailable.

        if self.stack:
            self.args = tuple(zip(map(str,instr.args), [get_z3_value_hex(self.stack[len(self.stack) - 1 - i]) for i in range(len(instr.args))]))
            self.args_as_dict = dict(self.args)

        if self.stack_next:
            self.returns = tuple(zip(map(str,instr.returns), [get_z3_value_hex(self.stack_next[len(self.stack_next) - 1 - i]) for i in range(len(instr.returns))]))
        else:
            self.returns = tuple(zip(map(str,instr.returns), ['?'] * len(instr.returns)))
        self.returns_as_dict = dict(self.returns)

        self._pseudocode = None

    def __str__(self):
        return "%s (%s) returns (%s)" % (self.instr,
                                         ", ".join("%s=%s"%(a, " ".join(l.strip() for l in get_z3_value_hex(b).split("\n"))) for a,b in self.args), # can be multiline... z3.PP formatter ftw
                                         ", ".join("%s=%s" % (a, " ".join(l.strip() for l in get_z3_value_hex(b).split("\n"))) for a, b in self.returns))

    def __repr__(self):
        return self.__str__()

    @property
    def as_pseudocode(self):
        if self._pseudocode is not None:
            return self._pseudocode

        f = getattr(MetaCode, self.instr.name.lower(), getattr(MetaCode, "cat_%s" % self.instr.category.lower(), None))
        if not f:
            self._pseudocode = False  # mark as not resolveable
        else:
            self._pseudocode = f(self)

        return self._pseudocode


class PseudoCodeStatement(object):

    def __init__(self, asm, fmt=None):
        self.asm = asm
        self.fmt = fmt

    def __str__(self):
        if self.fmt:
            #  use fmt if specified
            return self.fmt % self.asm.args_as_dict if self.asm.args else self.fmt

        return "%s(%s)" % (self.asm.instr.name,
                           (", ".join("%s=%s" % (a, b) for a, b in self.asm.args)))


def simplify(evmcode, show_asm=False, show_pseudocode=True, show_unreachable=False):
    """

    skip:
        * arithmetic
        * bitwise
    skip: (symbolic)
        * envinfo
        * sha3
        * blockinfo
    yield:
        * mem|storage store
        * JUMP(i)
        * JUMPDEST
        * LOG() -->cat event
        * SYSTEM_OPERATIONS -->
        * TERMINATE -->

    :param evmcode:
    :return:
    """
    yield ":init"
    for instr in evmcode.instructions:
        try:
            asm_stmt = AsmStatement(instr=instr,
                                    stack=evmcode.symbolic_state_at[instr.address][0][1].mstate.stack if not instr.name in ("JUMPDEST",) else None,
                                    evmcode=evmcode)
        except KeyError as ke:
            if show_unreachable: 
                yield("\t//UnreachableCodeException @:LOC_%s  [!!!!] <-- exception: %r --> %r" % (hex(instr.address), ke, instr))
            continue

        if show_asm and asm_stmt:
            yield "\t//%s"%asm_stmt

        if not show_pseudocode:
            continue

        if asm_stmt.as_pseudocode:
            # yield "// LOC_%s " % (hex(instr.address))
            if instr.category=="label":
                yield "\n%s"%asm_stmt.as_pseudocode  # yield blank line before printing label
            else:
                yield "\t%s"%"\n\t".join(str(asm_stmt.as_pseudocode).splitlines())
            if instr.category=="terminate":
                yield "\t/******* <<terminates execution>> *******/"

