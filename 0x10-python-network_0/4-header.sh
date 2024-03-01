#!/bin/bash
# Takes in a URL as an arg, sends a GET request to the URL and display body of response
curl -sfLH "X-School-User-Id: 98" "$1"
