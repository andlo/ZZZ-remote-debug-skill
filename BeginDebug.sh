#!/bin/bash
pkill -9 -f " -m mycroft.skills" ; pkill -9 -f "ptvsd" ; python3 -m ptvsd --host 0.0.0.0 --port 5678 -m mycroft.skills > /var/log/mycroft/skills.log 2>&1 &
