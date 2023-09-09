
import os
import json
from EXE2PNG import EXE2PNG  # Assuming your EXE2PNG.py is in the same directory

def extract_icons_from_json(json_path):
    # Ensure the JSON file exists
    if not os.path.exists(json_path):
        print(f"File not found: {json_path}")
        return

    # Load JSON data
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Loop through each shortcut in the JSON data
    for shortcut in data['shortcuts']:
        # If 'icon' key exists, skip extraction
        if 'icon' in shortcut:
            continue

        exe_path = os.path.expandvars(shortcut['path'])  # This is to handle environment variables in the path
        EXE2PNG(exe_path)

if __name__ == '__main__':
    json_path = 'setting.json'
    extract_icons_from_json(json_path)
