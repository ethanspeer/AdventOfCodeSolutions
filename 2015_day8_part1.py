def main():

    puzzle_input = input("Enter your puzzle input file: ")
    with open(puzzle_input, "r") as file:
        file_contents = file.read()
    puzzle_array = file_contents.split("\n")


    string_chars = 0
    memory_chars = 0

    for line in puzzle_array:
        trimmed_line = line[1:-1]
        char_list = list(trimmed_line)
        i = 0
        for char in char_list:
            if char == '\\':
                if char_list[i+1] == '\\' or char_list[i+1] == '\"':
                    del char_list[i+1]
                elif char_list[i+1] == 'x':
                    del char_list[i+1:i+4]
            i += 1
        string_chars += len(line)
        memory_chars += len(char_list)

    print("Answer:", string_chars - memory_chars)


if __name__ == '__main__':
    main()