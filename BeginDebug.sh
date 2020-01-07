mycroft-stop skills
pkill -f "python3 -m ptvsd"
python3 -m ptvsd --host 0.0.0.0 --port 5678 -m mycroft.skills > /var/log/mycroft/skills.log 2>&1 &