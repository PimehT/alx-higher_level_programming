#!/usr/bin/env bash
# get url and send http request to url

if [ -z "$" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL="$1"

curl -s -o /dev/null -w "%{size_download}" "URL"