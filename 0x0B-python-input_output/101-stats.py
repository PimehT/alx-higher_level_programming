#!/usr/bin/python3
# 101-stats.py
""" reads stdin line by line and computes metrics """
import sys


def print_metrics(file_size, status_codes):
    """ reads stdin line by line and computes metrics """

    print("File size: {}".format(file_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))


def process_lines():
    file_size = 0
    status_codes = {
            "200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0
            }
    line_count = 0

    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) > 2:
                try:
                    file_size += int(tokens[-1])
                    status = tokens[-2]
                    if status in status_codes:
                        status_codes[status] += 1
                except ValueError:
                    pass
            line_count += 1
            if line_count % 10 == 0:
                print_metrics(file_size, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise


if __name__ == "__main__":
    process_lines()
