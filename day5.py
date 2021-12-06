from collections import Counter

def parse_coordinates(coords):
    """694, 732 -> 290, 328"""
    one, two = coords.split(' -> ')
    x1, y1 = one.split(",")
    x2, y2 = two.split(",")

    return int(x1), int(y1), int(x2), int(y2)


def build_horizontal(points, lines):
    """x = (0, 9, 5, 9)"""
    step = 1 if points[0] < points[2] else -1

    for i in range(points[0], points[2] + step, step):
        coo = (i, points[1])
        lines.append(coo)


def build_vertical(points, lines):
    """x = (2,1,2,5)"""
    step = 1 if points[1] < points[3] else -1
    for i in range(points[1], points[3]+step, step):
        coo = (points[0], i)
        lines.append(coo)


def verify_diagonal(points):
    """
    diagonal tan(x) = tan(45degres) = b/a = 1
    """
    b = points[2] - points[0]
    a = points[3] - points[1]
    return abs(b/a) == 1


def build_diagonal(points, lines):
    stx = 1 if points[0] < points[2] else -1
    sty = 1 if points[1] < points[3] else -1

    dist = abs(points[3] - points[1])
    for i in range(dist+1):
        lines.append((points[0] + stx * i, points[1] + sty * i))


if __name__ == "__main__":

    starting_points = []

    for line in open('input.txt', 'r'):
        line = line.strip()
        starting_points.append(parse_coordinates(line))

    xlines = []
    for point in starting_points:
        if point[1] == point[3]:
            build_horizontal(point, xlines)
        elif point[0] == point[2]:
            build_vertical(point, xlines)
        elif verify_diagonal(point):
            build_diagonal(point, xlines)
    # point = (1,3,3,1)
    # build_diagonal(point, xlines)

    counter = Counter(xlines)

    nodes = sum(1 for i in counter.values() if i >= 2)
    print("nodes", nodes)



