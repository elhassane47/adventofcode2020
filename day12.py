
"""
A very good revision of DFS algorithm ,
I resolve it with help of this video https://www.youtube.com/watch?v=dlPoe04FoQk
"""
from collections import defaultdict


def parse_graph(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    nodes = defaultdict(set)
    for line in lines:
        depart, arr = line.strip().split("-")
        nodes[depart].add(arr)
        nodes[arr].add(depart)

    return nodes


def calculate_paths(graph):
    stack = [('start',)]
    all_paths = set()
    count_paths = 0

    while stack:
        path = stack.pop()

        if path[-1] == "end":
            all_paths.add(path)
            count_paths += 1
            continue

        for nei in graph[path[-1]]:

            # part one
            if not (nei.islower() and nei in path):
                stack.append((*path, nei))

    return all_paths


def part_two(graph):
    stack = [(('start',), False)]
    count_paths = 0

    while stack:
        path, twice = stack.pop()
        if path[-1] == "end":
            count_paths += 1
            continue

        for nei in graph[path[-1]]:
            if nei == "start":
                continue

            if nei.isupper() or nei not in path:
                stack.append(((*path, nei), twice))

            elif not twice and path.count(nei) == 1:
                stack.append(((*path, nei), True))


    return count_paths


if __name__ == "__main__":

    graph = parse_graph('input.txt')
    xx = part_two(graph)
    print(xx)
