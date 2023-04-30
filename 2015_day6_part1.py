import re

puzzle_input = input("Enter your puzzle input file: ")

with open(puzzle_input, "r") as file:
    file_contents = file.read()

puzzle_array = file_contents.split("\n")

count = 0
grid = [[None]*1000 for _ in range(1000)]

for x in range(1000):
    for y in range(1000):
        grid[x][y] = False

for line in puzzle_array:
    numbers = re.findall('\d+', line)
    for x in range(int(numbers[0]), int(numbers[2]) + 1):
        for y in range(int(numbers[1]), int(numbers[3]) + 1):
            if line.startswith("turn on"):
                grid[x][y] = True
            elif line.startswith("turn off"):
                grid[x][y] = False
            elif line.startswith("toggle"):
                if grid[x][y] == True:
                    grid[x][y] = False
                elif grid[x][y] == False:
                    grid[x][y] = True

for x in range(1000):
    for y in range(1000):
        if grid[x][y] == True:
            count += 1

print("Answer:", count)