puzzle_input = input("Enter your puzzle input file: ")

with open(puzzle_input, "r") as file:
    file_contents = file.read()

puzzle_array = file_contents.split("\n")

def count_vowels(s):
    count = 0
    for c in s:
        if c in "aeiouAEIOU":
            count += 1
    if count >= 3:
        return True
    return False

def double_letter(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True
    return False

def not_has_patterns(s):
    if not ("ab" in s or "cd" in s or "pq" in s or "xy" in s):
        return True
    return False

count = 0
for s in puzzle_array:
    if count_vowels(s) and double_letter(s) and not_has_patterns(s):
        count += 1

print("Answer:", count)
