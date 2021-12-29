mycroft-stop skills
pkill -f "python3 -m debugpy"
python3 -m debugpy --listen 0.0.0.0:5678 -m mycroft.skills > /var/log/mycroft/skills.log 2>&1 &
