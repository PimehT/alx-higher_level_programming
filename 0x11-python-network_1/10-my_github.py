#!/usr/bin/python3
"""
Script that uses GitHub API to display your GitHub user ID
"""
import requests
import sys


def get_github_user_id(username, token):
    """ return GitHub user ID using GitHub API """
    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        user_info = response.json()
        return user_info['id']
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        return None
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return None
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return None
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
        return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    user_id = get_github_user_id(username, token)
    if user_id is not None:
        print(user_id)
    else:
        print("None")
