#!/bin/bash
#Scripts sned JSON POST to url to display body of response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "{$1}"
