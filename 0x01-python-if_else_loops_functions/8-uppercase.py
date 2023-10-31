#!/usr/bin/python3
def uppercase(str):
    if not str:
        return
    for i in range(0, len(str)):
        char = ord(str[i])
        if char > 96 and char < 123:
            char = char - 32
        if len(str) - i == 1:
            print("{}".format(chr(char)))
        else:
            print("{}".format(chr(char)), end='')
