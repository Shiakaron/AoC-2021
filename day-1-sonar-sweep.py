file = open("puzzle-input.txt", "r")
count = -1
prev_depth = 0
for x in file:
    new_depth = int(x)
    print(new_depth)
    if new_depth > prev_depth:
        count += 1
    prev_depth = new_depth

print(count)
