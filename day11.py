import sys

fl_count = 0
flashes = []


def read_file(path):
    octopus = [[int(x) for x in line.strip()] for line in open(path, 'r')]
    return octopus


def step(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1

            if matrix[i][j] > 9:
                flashes.append((i, j))

    global fl_count

    while flashes:
        fl_count += 1
        flash = flashes.pop()
        matrix = update_flash(matrix, flash[0], flash[1])

    return matrix


def update_flash(matrix, i, j):
    matrix[i][j] = 0
    all_adjacents = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i + 1, j + 1), (i - 1, j - 1),
                     (i - 1, j + 1), (i + 1, j - 1)]

    for adj in all_adjacents:
        x, y = adj[0], adj[1]

        if 0 <= x < len(matrix) and 0 <= y < len(matrix[i]):
            if matrix[x][y] != 0 and adj not in flashes:
                matrix[adj[0]][adj[1]] += 1

                if matrix[adj[0]][adj[1]] > 9:
                    flashes.append((x, y))

    return matrix


def mtx_to_str(matrix):
    s = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            s += str(matrix[i][j])
        s += "\n"

    return s


def part_two(mtx):
    return sum(sum(line) for line in mtx) == 0


if __name__ == "__main__":
    mtx = read_file('input.txt')
    DAYS = 100
    day = 1
    #  part one
    # while day <= DAYS:
    #     mtx = step(mtx)
    #     day += 1
    # print("total", fl_count)

    while True:
        mtx = step(mtx)
        val = part_two(mtx)
        if val:
            print("finished at", day)
            sys.exit()
        day += 1


