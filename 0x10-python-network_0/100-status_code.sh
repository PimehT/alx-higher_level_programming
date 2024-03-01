#!/bin/bash
# sends a request to a URL passed as an argument, displays only the status code
curl -sI "$1" | head -n 1 | cut -d " " -f 
