#!/usr/bin/python3
j = 1
for i in range(0, 10):
    for j in range(1, 10):
        if i >= j:
            continue
        if j == 9 and j - i == 1:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end='')
