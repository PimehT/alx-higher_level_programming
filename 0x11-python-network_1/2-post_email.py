#!/usr/bin/python3
"""
Python script that takes URL and an email,
sends a POST request with the email as arg
display the body in utf-8
"""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """ post email to url using urllib """
    value = {'email': email}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        page = resp.read()
        page = page.decode('utf-8')
        print(page)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
