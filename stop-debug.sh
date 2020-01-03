#!/usr/bin/env bash

if [[ $( pgrep -f " -m mycroft.skills" ) ]] ; then
    pid=$( pgrep -f " -m mycroft.skills" )            
    echo "Killing skills (${pid})..."
    kill -9 ${pid}
    echo "killed."
fi
if [[ $( pgrep -f "ptvsd" ) ]] ; then
    pid=$( pgrep -f "ptvsd" )            
    echo "Killing PTVSD (${pid})..."
    kill -9 ${pid}
    echo "killed."
fi
python3 -m mycroft.skills >> /var/log/mycroft/skills.log 2>&1 &
