#!/bin/bash
pkill -9 -f " -m mycroft.skills" ; pkill -9 -f "ptvsd" ; python3 -m mycroft.skills > /var/log/mycroft/skills.log 2>&1 &
