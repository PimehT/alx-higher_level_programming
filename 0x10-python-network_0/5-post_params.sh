#!/bin/bash
# Sends a post request to the passed URL, and displays the body of the message
curl -sX POST --data-urlencode "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"
