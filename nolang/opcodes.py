
""" Opcode declaration
"""

class Opcode(object):
    def __init__(self, name, numargs, stack_effect, description):
        self.name = name
        self.numargs = numargs
        self.stack_effect = stack_effect
        self.description = description

    def __repr__(self):
        return '<%s>' % self.name

opcodes = [
    Opcode('INVALID', 0, 0, 'invalid opcode'),
    Opcode('LOAD_NONE', 0, 1, 'load None onto stack'),
    Opcode('LOAD_VARIABLE', 1, 1, 'load variable onto stack'),
    Opcode('LOAD_GLOBAL', 1, 1, 'load global variable'),
    Opcode('LOAD_CONSTANT', 1, 1, 'load constant onto stack'),
    Opcode('STORE', 1, -1, 'store top of the stack into variable'),
    Opcode('DISCARD', 1, -1, 'discard top of the stack'),
    # binary ops
    Opcode('ADD', 0, -1, 'load two values from the stack and store the result'
                         ' of addition'),
    Opcode('LT', 0, -1, 'load two value from the stack and store the result'
                        ' of lower than comparison'),
    # jumps
    Opcode('JUMP_IF_FALSE', 1, -1, 'pop value from the stack and jump if false'
                                   ' to a given position'),
    Opcode('JUMP_ABSOLUTE', 1, 0, 'jump to an absolute position'),
    Opcode('CALL', 1, 255, 'take N arguments from the stack, pack them into'
                           'args and call the next element'),
    Opcode('RETURN', 0, -1, 'return the top of stack')
]

def setup():
    for i, opcode in enumerate(opcodes):
        globals()[opcode.name] = i

setup()