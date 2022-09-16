#!/bin/bash

filename=$1

grep -oP '([a-zA-Z0-9\s_\\.\-\(\):]+\.js)' $filename | sort -u
