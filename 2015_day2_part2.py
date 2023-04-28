puzzle_input = input("Enter your puzzle input file: ")

result = 0

with open(puzzle_input, "r") as file:
    file_contents = file.read()

puzzle_array = file_contents.split("\n")

for dimension in puzzle_array:
    noxs = dimension.split('x')
    numbers = [int(i) for i in noxs]
    ascending = sorted(numbers)
    ribbon = ascending[0] + ascending[0] + ascending[1] + ascending[1] + (ascending[0] * ascending[1] * ascending[2])
    result += ribbon

print("Answer:", result)