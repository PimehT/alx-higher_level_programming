#!/usr/bin/python3
"""
Script that sends POST request with a letter as arg
if no letter, send empty arg
if json format is good, display '[<id>] <name>'
Otherwise:
    display 'Not a valid JSON' if invalid or
    display 'No result' if empty
"""
import requests
import sys


def json_api(char=None):
    """ return api search in json format """
    data = {}
    if char is None:
        data['q'] = ""
    else:
        data['q'] = char

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data)
        user = r.json()
        if not user:
            print("No result")
        else:
            print("[{}] {}".format(user['id'], user['name']))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) != 2 or len(sys.argv[1]) != 1:
        char = None
    else:
        char = sys.argv[1]
    json_api(char)
