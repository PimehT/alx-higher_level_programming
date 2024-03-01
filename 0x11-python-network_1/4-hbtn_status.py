#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
using requests package
"""
import requests


def hbtn_status_req():
    """using `requests` package to fetch url"""
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    hbtn_status_req()
