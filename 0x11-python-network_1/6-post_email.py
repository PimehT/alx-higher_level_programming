#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as an arg,
finally displays the body of the response.
"""
import requests
import sys


def post_email_req(url, email):
    """ sends email to URL using POST method """
    data = {'email': email}
    r = requests.post(url, data=data)
    print(r.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email_req(url, email)
