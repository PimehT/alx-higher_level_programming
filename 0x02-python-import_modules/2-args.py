#!/usr/bin/python3
import sys

def list_out():
    print("{} arguments".format(len(sys.argv) - 1), end='')
    if len(sys.argv) == 1:
        print(".")
    else:
        print(":")
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    list_out()
