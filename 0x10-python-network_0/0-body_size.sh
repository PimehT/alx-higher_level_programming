#!/bin/bash
# get url and send http request to url
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
