



def read_file(path):

    crabs_pos = []
    for line in open(path, 'r'):
        line = line.strip()
        for c in line.split(","):
            crabs_pos.append(int(c))
    return crabs_pos


def step_cost_part_one(e, x):
    return abs(e - x)


def step_cost_part_two(e, x):
    dist = step_cost_part_one(e, x)
    return sum(range(dist + 1))


if __name__ == "__main__":
    positions = read_file('input.txt')
    xx = step_cost_part_two(16, 5)
    print("xxxx", xx)
    # positions = [16,1,2,0,4,2,7,1,2,14]
    positions.sort()
    min = positions[0]
    max = positions[-1]

    actual = sum([step_cost_part_two(e, min) for e in positions])
    for x in range(min, max+1):
        distances = sum([step_cost_part_two(e,x) for e in positions])
        if distances <= actual:
            actual = distances

    print("val", actual)






