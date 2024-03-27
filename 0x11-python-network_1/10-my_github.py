#!/usr/bin/python3
"""
Script that uses GitHub API to display your GitHub user ID
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


def get_github_user_id(user, token):
    """ return GitHub user ID using GitHub API """
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(user, token)
    r = requests.get(url, auth=auth)
    user_info = r.json()
    return user_info.get('id')


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    user_id = get_github_user_id(username, token)
    if user_id is not None:
        print(user_id)
    else:
        print("None")
