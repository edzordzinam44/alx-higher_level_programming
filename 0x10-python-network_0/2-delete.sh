#!/bin/bash
#Script that sends DELETE to url as first argument and display body response
curl -sX DELETE "{$1}"
