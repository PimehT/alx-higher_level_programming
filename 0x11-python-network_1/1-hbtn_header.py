#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import urllib.request
import sys


def get_request_id(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as resp:
            # Check if the 'X-Request-Id' header exists in the response
            if 'X-Request-Id' in resp.headers:
                request_id = resp.headers['X-Request-Id']
                print(request_id)
            else:
                print("X-Request-Id not found in the response headers.")
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")


if __name__ == "__main__":
    url = sys.argv[1]
    get_request_id(url)
