puzzle_input = input("Enter your puzzle input: ")

count = 0
result = 0

for i in range(len(puzzle_input)):
    char = puzzle_input[i]
    if char == "(":
        count += 1
    elif char == ")":
        count -= 1
    if count == -1:
        result = i
        break
        

print("Answer:", result + 1)