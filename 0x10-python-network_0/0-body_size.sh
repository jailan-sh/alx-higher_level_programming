#!usr/bin/env bash
#sends a request to URL, and displays the size of the body of the response

url=$1

curl -Is -w "%{content_lenght}\n" "$1url"
