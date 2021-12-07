test_data = open("test_input.txt", "r").read().split()
data = open("input.txt", "r").read().split()

def move_sub(moves):
    # depth and horizontal position
    depth, horizontal = 0, 0

    for i in range(0, len(moves), 2):
        direction = moves[i]
        magnitude = int(moves[i+1])
        if direction == "forward":
            horizontal += magnitude
        elif direction == "down":
            depth += magnitude
        elif direction == "up":
            depth -= magnitude

    return depth * horizontal

def move_sub2(moves):
    # depth and horizontal position
    aim, depth, horizontal = 0, 0, 0

    for i in range(0, len(moves), 2):
        direction = moves[i]
        magnitude = int(moves[i+1])
        if direction == "forward":
            horizontal += magnitude
            depth += magnitude * aim
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude

    return depth * horizontal

# should be 150
print(move_sub(test_data))

# should be the answer to part 1
print(move_sub(data))

# should be the answer to part 2
print(move_sub2(data))