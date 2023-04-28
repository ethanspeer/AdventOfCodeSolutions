puzzle_input = input("Enter your puzzle input file: ")

result = 0

with open(puzzle_input, "r") as file:
    file_contents = file.read()

puzzle_array = file_contents.split("\n")

for dimension in puzzle_array:
    noxs = dimension.split('x')
    numbers = [int(i) for i in noxs]
    pair_1 = numbers[0] * numbers[1]
    pair_2 = numbers[1] * numbers[2]
    pair_3 = numbers[0] * numbers[2]
    wrapping = (2 * pair_1) + (2 * pair_2) + (2 * pair_3) + min(pair_1, pair_2, pair_3)
    result += wrapping

print("Answer:", result)