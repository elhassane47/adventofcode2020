from collections import Counter
fishes = []

for line in open('input.txt', 'r'):
    line = line.strip()
    for c in line.split(","):
        fishes.append(int(c))


def next_day(fish_list):

    for i in range(len(fish_list)):
        if fish_list[i] == 0:
            fish_list[i] = 6
            fish_list.append(8)
        else:
            fish_list[i] -= 1

    return fish_list


def part_two(fish_numbers):
    died = fish_numbers[0]
    for i in range(8):
        fish_numbers[i] = fish_numbers[i +1]

    fish_numbers[8] = died
    fish_numbers[6] += died
    return fish_numbers


fish_numbers = Counter(fishes)

DAYS_LENGTH = 256
current_day = 0
while current_day < DAYS_LENGTH:
    # next_day(fishes)
    fish_numbers = part_two(fish_numbers)
    current_day += 1
    total = sum(fish_numbers.values())

print("len de fishes list", total)



