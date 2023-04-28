puzzle_input = input("Enter your puzzle input file: ")

current_x = 0
current_y = 0
robot_x = 0
robot_y = 0

point_presents = {(0,0)}

with open(puzzle_input, "r") as file:
    file_contents = file.read()

for i in range(len(file_contents)):
    char = file_contents[i]
    if i % 2 == 0:
        if char == "^":
            current_y += 1
        elif char == "v":
            current_y -= 1
        elif char == ">":
            current_x += 1
        elif char == "<":
            current_x -= 1
        if (current_x, current_y) not in point_presents:
            point_presents.update({(current_x, current_y)})
    elif i % 2 == 1:
        if char == "^":
            robot_y += 1
        elif char == "v":
            robot_y -= 1
        elif char == ">":
            robot_x += 1
        elif char == "<":
            robot_x -= 1
        if (robot_x, robot_y) not in point_presents:
            point_presents.update({(robot_x, robot_y)})

print("Answer:", len(point_presents))
