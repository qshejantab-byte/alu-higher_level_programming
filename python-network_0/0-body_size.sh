#!/bin/bash
# Displays the size, in bytes, of the body of a response to a URL
curl -s "$1" | wc -c
