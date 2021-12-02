
# readfile to steps
steps = []

with open('input.txt', 'r') as f:
    for l in f.readlines():
        name, number = l.split()[0], l.split()[1]
        steps.append((name, int(number)))

horizontal = 0
depth = 0

# Part two
aim = 0

for st in steps:
    if st[0] == 'forward':
        horizontal += st[1]
        # Part two
        depth = depth + aim * st[1]

    if st[0] == 'down':
        # Part two uncomment first line and comment the 2nd
        # depth += st[1]
        aim += st[1]

    if st[0] == 'up':
        # Part two uncomment first line and comment the 2nd
        # depth -= st[1]
        aim -= st[1]

print("val", horizontal * depth)
