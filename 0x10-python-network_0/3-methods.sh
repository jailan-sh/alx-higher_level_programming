#!/bin/bash
#Display only body of delete response
#curl -sI -X OPTIONS "$1" | grep "Allow:" | awk '{for( i=2; i<=NF; i++ ){printf( "%s ", $i )}; printf( "\n"); }'
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
