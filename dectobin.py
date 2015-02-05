__author__ = 'garvit'

import stack
from timeit import Timer


def convert(num, base):
    rem = stack.Stack();
    digits = "0123456789ABCDEF"

    while num > 0:
        rem.push(num % base)
        num = num // base;

    string = ""
    while not rem.isEmpty():
        string += digits[rem.pop()]

    return string

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = stack.Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(convert(11, 16))
print(baseConverter(11, 16))


t1 = Timer("convert(25, 16)", "from __main__ import convert")
print("convert ", t1.timeit(number=1000), "milliseconds")

t1 = Timer("baseConverter(25, 16)", "from __main__ import baseConverter")
print("baseConverter ", t1.timeit(number=1000), "milliseconds")