
file = open("input.txt", "r")
depths = file.read().split()

def check_depth(depths):
    previous_depth = depths[0]
    print(previous_depth + " (N/A - no previous measurement)")

    increases, decreases = 0, 0
    for depth in depths[1:]:
        if int(depth) > int(previous_depth):
            increases += 1
            #print(depth + " (increased)")
        else:
            decreases += 1
            #print(depth + " (decreased)")
        previous_depth = depth

    return increases, decreases

increases, decreases = check_depth(depths)
print("There were {increases} increases and {decreases} decreases in depth respectively.".format(increases = increases, decreases = decreases))