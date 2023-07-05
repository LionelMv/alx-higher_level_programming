#!/bin/bash
#displays all methods on the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
