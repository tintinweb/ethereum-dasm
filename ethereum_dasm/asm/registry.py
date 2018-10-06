#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author : <github.com/tintinweb>

from .instructions import Instruction

import evmdasm.registry

registry = evmdasm.registry.InstructionRegistry(instructions=evmdasm.registry.INSTRUCTIONS, _template_cls=Instruction)

# rebuild the registry with our extended Instruction class. (clone with our class as template)
INSTRUCTIONS = registry.instructions
INSTRUCTIONS_BY_OPCODE = registry.by_opcode
INSTRUCTIONS_BY_NAME = registry.by_name
INSTRUCTIONS_BY_CATEGORY = registry.by_category
INSTRUCTION_MARKS_BASICBLOCK_END = registry.instruction_marks_basicblock_end
create_instruction = registry.create_instruction
