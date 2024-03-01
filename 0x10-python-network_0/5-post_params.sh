#!/bin/bash
#Script takes url sends a POST to url and display the body of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "{$1}"
