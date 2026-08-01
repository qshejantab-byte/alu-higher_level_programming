#!/bin/bash
# Displays all HTTP methods a server accepts for a given URL
curl -sI "$1" | grep -i "^allow:" | cut -d' ' -f2- | tr -d '\r'
