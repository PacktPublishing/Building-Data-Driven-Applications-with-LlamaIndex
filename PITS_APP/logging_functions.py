from datetime import datetime
from global_settings import LOG_FILE
import os

def log_action(action, action_type):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp}: {action_type} : {action}\n"
    with open(LOG_FILE, 'a') as file:
        file.write(log_entry)

def reset_log():
    with open(LOG_FILE, 'w') as file:
        file.truncate(0)
