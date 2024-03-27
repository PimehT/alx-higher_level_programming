#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
import sys


def error_code(url):
    """
    sends request to url and display the body of response
    or handles urllib.error.HTTPError
    """
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            page = resp.read().decode('utf-8')
            print(page)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1]
    error_code(url)
