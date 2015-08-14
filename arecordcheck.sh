#!/bin/sh

# cheap way to fire a script on time intervals
# this should be run in the background and needs x perms

while true

do

    python /home/path/to/script/script.py

    sleep 43200 # 12 hours

done

