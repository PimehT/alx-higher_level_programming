#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header
"""
import requests
import sys


def hbtn_header_req(url):
    """ prints value of X-Request-Id in response header of url"""
    r = requests.get(url)
    data = r.headers['X-Request-Id']
    print(data)


if __name__ == "__main__":
    url = sys.argv[1]
    hbtn_header_req(url)
