#!/usr/bin/python3
import sys
import hidden_4


def print_cache():
    cache = [item for item in dir(hidden_4) if "__" not in item]
    for i in cache:
        print("{}".format(i))


if __name__ == "__main__":
    print_cache()
