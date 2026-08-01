#!/bin/bash
# Displays the body of a GET response, only if the status code is 200
code=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ "$code" -eq 200 ] && curl -s "$1"
