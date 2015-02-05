__author__ = 'garvit'

import stack
from timeit import Timer


def check(string):
    s = stack.Stack()
    for e in string:
        if e == '(':
            s.push(e)
        elif e == ')':
            if not s.isEmpty():
                s.pop()
            else:
                return False
    return s.items == []


def parChecker(symbolString):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


t1 = Timer("check('((()))')", "from __main__ import check")
print("check ", t1.timeit(number=1000), "milliseconds")

t1 = Timer("parChecker('((()))')", "from __main__ import parChecker")
print("parChecker ", t1.timeit(number=1000), "milliseconds")
