#!/bin/bash
#  status
curl -s -o /dev/null -w "%{http_code}" "$1"
