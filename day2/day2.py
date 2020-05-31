# Day 2: Intcode
# Opcode 1 adds together numbers read from two positions and stores the result in a third position.
# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
# Opcode 99 halts the program

OP_ADD = 1
OP_MUL = 2
OP_END = 99

# with open("input.txt", "r") as f:
#     codes = f.readline().split(",")
#     codes = list(map(int, codes))  # use map to cast each elem as an int
#     index = 0
#     current = codes[index]
#     while current != OP_END:
#         op_one = codes[codes[index + 1]]
#         op_two = codes[codes[index + 2]]
#         op_dest = codes[index + 3]

#         codes[op_dest] = (op_one + op_two) if (current ==
#                                                OP_ADD) else (op_one * op_two)
#         index += 4
#         current = codes[index]
#     print("value at position 0: ", codes[0])

# PART 2
# Find inputs for address one and two to output 19690720
# both must be values between 0 and 99, inclusive

for noun in range(0, 99):
    for verb in range(0, 99):
        with open("input.txt", "r") as f:
            codes = f.readline().split(",")
            codes = list(map(int, codes))

            index = 0
            codes[1] = noun
            codes[2] = verb
            current = codes[index]

            while current != OP_END:
                op_one = codes[codes[index + 1]]
                op_two = codes[codes[index + 2]]
                op_dest = codes[index + 3]
                codes[op_dest] = (op_one + op_two) if (current ==
                                                       OP_ADD) else (op_one * op_two)
                index += 4
                current = codes[index]

            if codes[0] == 19690720:
                print("output achieved. answer = ", 100 * noun + verb)
                break
