puzzle_input = input("Enter your puzzle input file: ")

with open(puzzle_input, "r") as file:
    file_contents = file.read()

puzzle_array = file_contents.split("\n")


def double_pattern(s):
    substrings = []
    for i in range(len(s)-1):
        substrings.append(s[i:i+2])
    
    for i in range(len(substrings)):
        for j in range(i + 1, len(substrings)):
            if substrings[i] == substrings[j] and j != i+1:
                return True
    return False
                

def letter_between(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            count += 1
    if count >= 1:
        return True
    return False

count = 0
for s in puzzle_array:
    if double_pattern(s) and letter_between(s):
        count += 1

print("Answer:", count)
