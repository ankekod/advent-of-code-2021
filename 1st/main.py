
test_data = open("test_input.txt", "r")
data = open("input.txt", "r")

test_depths = test_data.read().split()
depths = data.read().split()

def check_depth(depths):
    # starting depth
    previous_depth = depths[0]

    # check if the depth has increased or decreases
    increases, decreases = 0, 0
    for depth in depths[1:]:
        if int(depth) > int(previous_depth):
            increases += 1
        else:
            decreases += 1
        previous_depth = depth

    print("There were {increases} increases and {decreases} decreases in depth respectively.".format(increases = increases, decreases = decreases))
    
    return increases, decreases

def check_depth_sums(depths):
    # converts str to int
    depths = list(map(int, depths))
    
    # starting depth
    previous_depth = sum(depths[0:3])

    # check if the depth has increased or decreases
    increases, decreases = 0, 0
    for i in range(1, len(depths) - 2):
        new_depth = sum(depths[i:i+3])
        if new_depth > previous_depth:
            increases += 1
        else:
            decreases += 1
        previous_depth = new_depth

    print("There were {increases} increases and {decreases} decreases in depth respectively.".format(increases = increases, decreases = decreases))

    return increases, decreases

check_depth(test_depths)
check_depth_sums(test_depths)

check_depth(depths)
check_depth_sums(depths)
