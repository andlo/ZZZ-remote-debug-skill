#!/bin/bash
pkill -9 -f "ptvsd" ; pkill -9 -f " -m mycroft.skills" ; python3 -m mycroft.skills > /var/log/mycroft/skills.log 2>&1 &
