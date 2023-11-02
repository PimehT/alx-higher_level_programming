#!/usr/bin/python3
import sys


def add_all():
    argv = sys.argv
    result = 0
    if len(argv) == 1:
        print("0")
    else:
        for i in range(1, len(argv)):
            result += int(argv[i])
        print("{}".format(result))


if __name__ == "__main__":
    add_all()
