#!/bin/bash
#Scripts takes  url and display HTTP methods the server will accept
curl -sI "{$1}" | grep "Allow" | cut -d " " -f 2-
