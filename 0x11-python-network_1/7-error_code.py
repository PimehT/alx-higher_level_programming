#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import requests
import sys


def error_code_req(url):
    """send a request to URL and handles error code >= 400"""
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)


if __name__ == "__main__":
    url = sys.argv[1]
    error_code_req(url)
