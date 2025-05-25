#!/usr/bin/env python3

import os
import requests

feedback_dir = "/data/feedback"
url = "http://35.188.213.78/feedback/"

for file_name in os.listdir(feedback_dir):
    file_path = os.path.join(feedback_dir, file_name)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.read().strip().split('\n')
            feedback = {
                'title': lines[0],
                'name': lines[1],
                'date': lines[2],
                'feedback': '\n'.join(lines[3:])
            }

        print(f"📦 Sending from {file_name}:\n{feedback}")
        response = requests.post(url, json=feedback)

        if response.status_code == 201:
            print(f"✅ Successfully posted {file_name}")
        else:
            print(f"❌ Error posting {file_name}: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"❌ Error processing {file_name}: {e}")

