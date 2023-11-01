#!/usr/bin/python3
i = 90
def add_or_not(a):
    if a % 2 == 0:
        return a + 32
    else:
        return a


while i > 64:
    print("{}".format(chr(add_or_not(i))), end='')
    i = i - 1
