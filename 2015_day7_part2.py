class Wire:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Instruction:
    def __init__(self, operation, left_signal, right_signal, wire):
        self.operation = operation
        self.left_signal = left_signal
        self.right_signal = right_signal
        self.wire = wire


def main():
    puzzle_input = input("Enter your puzzle input file: ")
    with open(puzzle_input, "r") as file:
        file_contents = file.read()
    puzzle_array = file_contents.split("\n")
    
    wires = []
    instructions = []

    def make_instructions():
        for line in puzzle_array:
            wire = Wire(line.split(" -> ")[1], None)
            wires.append(wire)
            operation = ""
            for char in line:
                if char.isupper():
                    operation += char
            line = ''.join([char for char in line if not char.isupper()]).split(" -> ")[0]
            split = line.split(" ")
            if(len(split) == 1):
                instructions.append(Instruction(operation, split[0], "_", wire.name))
            elif(len(split) == 2):
                instructions.append(Instruction(operation, split[1], "_", wire.name))
            elif (len(split) == 3):
                instructions.append(Instruction(operation, split[0], split[2], wire.name))

    def lookup_wire(wire_name):
        for wire in wires:
            if wire.name == wire_name:
                return wire
    
    def do_operation(op, left, right, wire):
        match op:
            case "":
                left_lookup = lookup_wire(left)
                if left.isdigit():
                    if right == "_":
                        for w in wires:
                            if w.name == wire:
                                w.number = int(left)
                else:
                    for w in wires:
                        if w.name == wire:
                            w.number = left_lookup.number
            case "LSHIFT":
                if left.isdigit() or right.isdigit():
                    if left.isdigit():
                        right_lshift = lookup_wire(right)
                        for w in wires:
                            if w.name == wire and right_lshift.number != None:
                                w.number = int(left) << right_lshift.number
                    elif right.isdigit():
                        left_lshift = lookup_wire(left)
                        for w in wires:
                            if w.name == wire and left_lshift.number != None:
                                w.number = left_lshift.number << int(right)
            case "RSHIFT":
                if left.isdigit() or right.isdigit():
                    if left.isdigit():
                        right_rshift = lookup_wire(right)
                        for w in wires:
                            if w.name == wire and right_rshift.number != None:
                                w.number = int(left) >> right_rshift.number
                    elif right.isdigit():
                        left_rshift = lookup_wire(left)
                        for w in wires:
                            if w.name == wire and left_rshift.number != None:
                                w.number = left_rshift.number >> int(right)
            case "AND":
                if left.isdigit() or right.isdigit():
                    if left.isdigit():
                        right_and = lookup_wire(right)
                        for w in wires:
                            if w.name == wire and right_and.number != None:
                                w.number = int(left) & right_and.number
                    elif right.isdigit():
                        left_and = lookup_wire(left)
                        for w in wires:
                            if w.name == wire and left_and.number != None:
                                w.number = left_and.number & int(right)
                else:
                    left_and = lookup_wire(left)
                    right_and = lookup_wire(right)
                    for w in wires:
                        if w.name == wire and left_and.number != None and right_and.number != None:
                            w.number = left_and.number & right_and.number
            case "OR":
                if left.isdigit() or right.isdigit():
                    if left.isdigit():
                        right_or = lookup_wire(right)
                        for w in wires:
                            if w.name == wire and right_or.number != None:
                                w.number = int(left) | right_or.number
                    elif right.isdigit():
                        left_or = lookup_wire(left)
                        for w in wires:
                            if w.name == wire and left_or.number != None:
                                w.number = left_or.number | int(right)
                else:
                    left_or = lookup_wire(left)
                    right_or = lookup_wire(right)
                    for w in wires:
                        if w.name == wire and left_or.number != None and right_or.number != None:
                            w.number = left_or.number | right_or.number
            case "NOT":
                left_not = lookup_wire(left)
                for w in wires:
                    if w.name == wire and left_not.number != None:
                        w.number = ~left_not.number
            case _:
                pass

    def execute_instructions(skipme):
        for instr in instructions:
                end_wire = lookup_wire(instr.wire)
                if end_wire.number != None:
                    continue
                if skipme == True:
                    if end_wire.name == "b":
                        continue
                do_operation(instr.operation, instr.left_signal, instr.right_signal, instr.wire)


    make_instructions()

    found = False
    while(found == False):
        execute_instructions(False)
        for wire in wires:
            if wire.name == "a" and wire.number != None:
                found = True

    answer = 0
    for wire in wires:
        if wire.name == "a":
            answer = wire.number
            break
    
    for wire in wires:
        wire.number = None
    
    for wire in wires:
        if wire.name == "b":
            wire.number = answer
            break
    
    found = False
    while(found == False):
        execute_instructions(True)
        for wire in wires:
            if wire.name == "a" and wire.number != None:
                found = True
    
    for wire in wires:
        if wire.name == "a":
            print("Answer:", wire.number)
            break

if __name__ == '__main__':
    main()