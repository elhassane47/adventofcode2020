
class Board:

    def __init__(self, numbers):
        self.numbers = numbers
        self.flags = [[0] * 5 for i in range(5)]

    def number_exist(self, n):
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if self.numbers[i][j] == n:
                    self.flags[i][j] = 1
                    return True
        return False

    @property
    def columns(self):
        return [[line[i] for line in self.flags] for i in range(5)]

    def sum_numbers(self):
        sum = 0
        for i in range(len(self.numbers)):
            for j in range(len(self.numbers)):
                if not self.flags[i][j]:
                    sum += self.numbers[i][j]

        return sum

    def is_bingo(self):
        for line in self.flags:
            if sum(line) == 5:
                return True

        for c in self.columns:
            if sum(c) == 5:
                return True
        return False


def read_file(path):

    drawn_numbers = []
    boards = []

    with open(path, 'r') as f:
        lines = f.readlines()

        numbers = lines[0].strip()
        for c in numbers.split(","):
            drawn_numbers.append(int(c))

        board = []
        for line in lines[1:]:
            if line == "\n":
                continue
            else:
                line = line.strip().replace("  ", " ")
                board.append([int(x) for x in line.split(" ")])
                if len(board) == 5:
                    boards.append(board)
                    board = []

        return drawn_numbers, boards


if __name__ == "__main__":
    drawn_numbers, boards = read_file('input.txt')
    boards_obj = []
    for b in boards:
        boards_obj.append(Board(b))

    winners = []
    for dr_n in drawn_numbers:
        for idx, bo in enumerate(boards_obj):
            bo.number_exist(dr_n)
            if bo.is_bingo() and idx not in winners:
                winners.append(idx)

                if len(winners) == len(boards_obj):
                    sx = bo.sum_numbers()
                    print("this is it", dr_n * sx)



    # ex = boards_obj[0].number_exist(22)
    # ex = boards_obj[0].number_exist(11)
    # bingo = boards_obj[0].is_bingo()
