#!/usr/bin/bash
# get url and send http request to url

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"

curl -sI $1 | grep -i Content-Length | cut -d ' ' -f 2