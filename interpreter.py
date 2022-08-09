from collections import deque
from dataclasses import dataclass
import sys
from memory import Memory



@dataclass
class Interpreter:
    mem_size:int
    def __post_init__(self):
        self.memory = Memory(self.mem_size)

    def __call__(self,code):
        Interpreter.check_syntax(code)
        block_stack = deque()
        current_pointer = 0
        code_length = len(code)
        while current_pointer < code_length:
            match code[current_pointer]:
                case '>':
                    self.memory.pointer += 1
                case '<':
                    self.memory.pointer -= 1
                case '+':
                    self.memory.current += 1
                case '-':
                    self.memory.current -= 1
                case '.':
                    sys.stdout.write(chr(self.memory.current))
                case ',':
                    self.memory.current = self.input()
                case '[':
                    if not self.memory.current == 0:
                        block_stack.append(current_pointer)
                    else:
                        current_pointer = get_closed_bracket(code,current_pointer)
                case ']':
                    if not self.memory.current == 0:
                        if len(block_stack) > 0:
                            current_pointer = block_stack[-1]
                        else:
                            current_pointer = 0
                    else:
                        
                        block_stack.pop()
            current_pointer += 1
            
    def check_syntax(code):
        lines = code.split()
        block_stack = deque()
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == '[':
                    block_stack.append((i,j))
                if c == ']':
                    if len(block_stack) > 0:
                        block_stack.pop()
                    else:
                        i,j = block_stack.pop()
                        error_message = make_error_message(lines[i],i,j," unmatched ']'")
                        raise SyntaxError(error_message)

        if len(block_stack) > 0:
            error_message = '\n'
            while len(block_stack) > 0:
                i,j = block_stack.pop()
                error_message += make_error_message(lines[i],i,j,"'[' was never closed")
            raise SyntaxError(error_message)

def make_error_message(line,i,j,error_message):
    message = ''
    message += f"line {i}:{j}\n"
    message += f"{line[i]} \n"
    message += f"{' '* j}^\n"
    message += error_message+"\n"
    return message

def get_closed_bracket(code,current):
    length = len(code)
    while current < length:
        if code[current] == ']':
            return current
        current += 1
    return current
