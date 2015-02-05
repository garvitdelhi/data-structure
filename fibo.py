__author__ = 'garvit'

def fib(n):
    a, b = 0, 1
    while b < n:
        print(a, end = ' ')
        a, b = b, a + b
    print()
