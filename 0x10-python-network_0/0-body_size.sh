#!/usr/bin/env bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -w %{size_download}"\n" "$1" -o /dev/null
