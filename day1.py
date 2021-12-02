from collections import defaultdict

def read_file(ff):
    for n in open(ff, 'r'):
        yield n

numbers = []

for n in open('input.txt', 'r'):
    numbers.append(int(n))

########## Part one

def nbm_increment(values):
    inc = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            inc +=1
    return inc


########## Part two


windows = defaultdict()

for i in range(len(numbers)):
    windows[i] = numbers[i:i+3]

valeurs = [sum(val) for val in windows.values() if len(val) == 3]

print("hee", valeurs)
xx = nbm_increment(valeurs)
print("new inc", xx)