puzzle_input = input("Enter your puzzle input: ")

count = puzzle_input.count("(") - puzzle_input.count(")")

print("Answer:", count)