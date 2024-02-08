from global_settings import SESSION_FILE

import yaml
import os

def save_session(state):
    state_to_save = {key: value for key, value in state.items()}
    with open(SESSION_FILE, 'w') as file:

def load_session(state):
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as file:
            try:
                loaded_state = yaml.safe_load(file) or {}
                for key, value in loaded_state.items():
                    state[key] = value
                return True
            except yaml.YAMLError:
                return False
    return False

def delete_session(state):
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    for key in list(state.keys()):
        del state[key]
