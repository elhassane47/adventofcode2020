from collections import defaultdict, Counter
numbers = []
num_of_numbers = defaultdict(list)

for line in open('input.txt', 'r'):
    numbers.append(line.strip())

for n in numbers:
    for i in range(len(n)):
        num_of_numbers[i].append(n[i])


gamma = []
epsi = []

for v in num_of_numbers:
    counter = Counter(num_of_numbers[v]).most_common(2)
    gamma.append(counter[0][0])
    epsi.append(counter[1][0])


def lit_to_binary(digits):
    return int("".join(map(str, digits)), 2)


print("value", lit_to_binary(gamma)*lit_to_binary(epsi))

#### Part two

oxygen = numbers.copy()
co2 = numbers.copy()


# result {0: Counter({'1': 7, '0': 5}), 1: Counter({'0': 7, '1': 5}), 2: Counter({'1': 8, '0': 4}),
# 3: Counter({'1': 7, '0': 5}), 4: Counter({'0': 7, '1': 5})}

x = len(oxygen)
while x > 1:
    num_of = defaultdict(list)

    for n in oxygen:
        for i in range(len(n)):
            num_of[i].append(n[i])
    result = {p: Counter(g) for p, g in num_of.items()}

    for key in result.keys():

        most_com = result[key].most_common(2)

        value = most_com[0][0]
        if most_com[0][1] == most_com[1][1]:
            value = '1'
        oxygen = [ox for ox in oxygen if ox[key] == value]

        num_of = defaultdict(list)
        for n in oxygen:
            for i in range(len(n)):
                num_of[i].append(n[i])

        result = {p: Counter(g) for p, g in num_of.items()}

        x = len(oxygen)

print("oxygen", lit_to_binary(oxygen))



# 11110, 10110, 10111, 10101, 11100, 10000, and 11001.