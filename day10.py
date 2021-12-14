"""
classic problem i resolve this thanks to this video :
https://www.youtube.com/watch?v=WTzjTskDFMg

"""

string_test = ["([])", "{()()()", "{()()()>", "(((()))}"]

parentheses = {"(": ")", "[": "]", "{": "}", "<": ">"}
coef = {")": 3, "]": 57, "}": 1197, ">": 25137}


def is_balanced_parentheses(st):
    stack = []
    score = 0
    for c in st:
        if c in parentheses:
            stack.append(c)
        else:
            cur = stack.pop()
            if parentheses[cur] != c:
                return stack, coef[c]

    return stack, score



final_sc = 0


auto_completes_scores = []
for line in open('input.txt'):
    line = line.strip()
    final_sc += is_balanced_parentheses(line)[1]


print("final", final_sc)






