#!/bin/bash
# Script take url and sends request to url and displays size of body
curl -s "$1" | wc -c

