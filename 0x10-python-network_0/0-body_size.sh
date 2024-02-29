#!/bin/bash
# Script take url and sends request to url and displays size of body
curl -sI "${1}" | grep -i 'Content-Length' | awk '{print $2}'
