from functools import reduce

def read_file(path):
    matrix = []
    for line in open(path, 'r'):
        xl = [int(x) for x in line.strip()]
        xl.insert(0, 9)
        xl.append(9)
        matrix.append(xl)

    dim_x = len(matrix[0])
    matrix.insert(0, [9] * dim_x)
    matrix.append([9] * dim_x)

    return matrix


def low_points(matrix):
    low = []
    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):
            down = matrix[i+1][j]
            up = matrix[i-1][j]
            left = matrix[i][j+1]
            right = matrix[i][j-1]

            if matrix[i][j] < up and matrix[i][j] < down and matrix[i][j] < left and matrix[i][j] < right:
                low.append(matrix[i][j])

    value = sum(low) + len(low)

    return value

seen_points = set()


def get_adj_bassins(i, j):
    adj = []
    sm = 0

    if matrix[i + 1][j] < 9 and (i+1, j) not in seen_points:
        sm += 1
        seen_points.add((i+1, j))
        sm += get_adj_bassins(i+1, j)

    if matrix[i -1][j] < 9 and (i-1, j) not in seen_points:
        sm += 1
        seen_points.add((i-1, j))
        sm += get_adj_bassins(i-1, j)

    if matrix[i][j + 1] < 9 and (i, j+1) not in seen_points:
        sm += 1
        seen_points.add((i, j+1))
        sm += get_adj_bassins(i, j+1)

    if matrix[i][j - 1] < 9 and (i, j-1) not in seen_points:
        sm += 1
        seen_points.add((i, j-1))
        sm += get_adj_bassins(i, j-1)

    seen_points.add((i, j))

    return sm


def part_two(matrix):

    bassins = []

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[i])-1):

            if matrix[i][j] < 9 and (i,j) not in seen_points:
                bassins.append(get_adj_bassins(i,j))


    return reduce(lambda x, y: x*y, sorted(bassins, reverse=True)[:3])


matrix = read_file('input.txt')
# print("matrix", matrix)
print(part_two(matrix))

