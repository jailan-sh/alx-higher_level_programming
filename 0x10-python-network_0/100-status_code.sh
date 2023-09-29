#!/bin/bash
#  status
curl -s -w "%http_code" "$1"
