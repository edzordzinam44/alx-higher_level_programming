#!/bin/bash
# Scripts makes a request to 0.0.0.0:5000/catch_me that get the message "You got me!
curl -sL -X PUT -H "Origin: HoolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
