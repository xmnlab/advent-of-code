"""
--- Part Two ---
"Good, the new computer seems to be working correctly! Keep it nearby during this mission -
you'll probably use it again. Real Intcode computers support many more features than your new
one, but we'll let you know what they are as you need them."

"However, your current priority should be to complete your gravity assist around the Moon.
For this mission to succeed, we should settle on some terminology for the parts you've already built."
Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb?
(For example, if noun=12 and verb=2, the answer would be 1202.)

Intcode programs are given as a list of integers; these values are used as the initial state
for the computer's memory. When you run an Intcode program, make sure to start by initializing
memory to the program's values. A position in memory is called an address (for example, the
first value in memory is at "address 0").

Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately
after an opcode, if any, are called the instruction's parameters. For example, in the instruction
1,2,3,4, 1 is the opcode; 2, 3, and 4 are the parameters. The instruction 99 contains only
an opcode and has no parameters.

The address of the current instruction is called the instruction pointer; it starts at 0. After
an instruction finishes, the instruction pointer increases by the number of values in the instruction;
until you add more instructions to the computer, this is always 4 (1 opcode + 3 parameters) for the
add and multiply instructions. (The halt instruction would increase the instruction pointer by 1,
but it halts the program instead.)

"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need
to determine what pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2,
just like before. In this program, the value placed in address 1 is called the noun, and the value
placed in address 2 is called the verb. Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before. Each time you
try a pair of inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) -
in other words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb?
(For example, if noun=12 and verb=2, the answer would be 1202.)

"""


def _int(v):
    try:
        return int(v)
    except:
        return 99


opcodes_calc = {1: lambda a, b: a + b, 2: lambda a, b: a * b}


def calc_intcodes(opcodes_list: list, stop_at=None):
    result = opcodes_list[:]
    i = 0
    while i < len(result):
        v = result[i]

        if v == 99:
            # halt
            return result
        elif v in (1, 2):
            _input = result[result[i + 1]], result[result[i + 2]]
            i_output = result[i + 3]
            r = opcodes_calc[v](*_input)
            result[i_output] = r
            i += 4
        else:
            i += 1

        if stop_at is not None:
            if result[0] == stop_at:
                return result
    return result


# test 2
test_set = (
    ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
)
for i, (opcodes_list, opcodes_expected) in enumerate(test_set):
    result = calc_intcodes(opcodes_list)

    print("=" * 10, i)
    print("Original:", opcodes_list)
    print("Expected:", opcodes_expected)
    print("Result:", result)

    assert result == opcodes_expected


# =========== RUN ===========
def get_data():
    with open("day{}-input.txt".format(2), "r") as f:
        data_input = [_int(d) for d in f.read().split(",") if d != ""]
        # Recovery:
        # To do this, before running the program,
        # replace position 1 with the value 12 and replace position 2 with the value 2.
        # What value is left at position 0 after the program halts?
        data_input[1] = 12
        data_input[2] = 2
    return data_input


def calc_noun_verb(a, b):
    return 100 * a + b


data_input = get_data()

print("=" * 30, "RUN")
print("Input:", data_input)

result = calc_intcodes(data_input)

print("Result:", result)
print(
    "What value is left at position 0 after the program halts?",
    "R:",
    result[0],
)


print("=" * 30, "finding pair")
goal = 19690720

resp = None
run = True

for noun in range(100):
    if not run:
        break
    for verb in range(100):
        data_input = get_data()
        data_input[1] = noun
        data_input[2] = verb

        result = calc_intcodes(data_input)

        if result[0] == goal:
            run = False
            resp = noun, verb
            break

if resp is None:
    print("EE pair not found")
else:
    # Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb?
    # (For example, if noun=12 and verb=2, the answer would be 1202.)
    print("R:", calc_noun_verb(*resp))
