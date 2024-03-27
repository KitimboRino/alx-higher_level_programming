#!/bin/bash
# cURL body size

# Send request using curl, measure the size of the response body, and output it
curl -sw '%{size_download}\n' -o /dev/null "$1"
