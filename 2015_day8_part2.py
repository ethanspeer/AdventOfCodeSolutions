def main():

    puzzle_input = input("Enter your puzzle input file: ")
    with open(puzzle_input, "r") as file:
        file_contents = file.read()
    puzzle_array = file_contents.split("\n")


    string_chars = 0
    memory_chars = 0

    for line in puzzle_array:
        temp_count = 0
        char_list = list(line)
        i = 0
        for char in char_list:
            if char == '\\' or char == '\"':
                temp_count += 1
            i += 1
        string_chars += len(line)
        memory_chars += len(char_list) + temp_count + 2
        

    print("Answer:", memory_chars - string_chars)


if __name__ == '__main__':
    main()