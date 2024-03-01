#!/bin/bash
#Scripts sends url and displays the codes status as response to the body
curl -s -o /dev/null -w "%{http_code}" "{$1}"
