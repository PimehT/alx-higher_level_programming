#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
use no other packages other than urllib
"""
import urllib.request


def hbtn_status():
    """ function that fetches url using urllib """
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as resp:
        page = resp.read()
        try:
            print("Body response:\n\t- type: {}".format(type(page)))
            print("\t- content: {}".format(page))
            print("\t- utf8 content: {}".format(page.decode('utf-8')))
        except UnicodeDecodeError:
            print("\nUnicode error while decoding")


if __name__ == "__main__":
    hbtn_status()
