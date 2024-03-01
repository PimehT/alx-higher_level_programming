#!/bin/bash
# Sends a post request to the passed URL, and displays the body of the message
curl -sX POST -d '{"email":"test@gmail.com", "subject":"I will always be here for PLD"}' "$1"
