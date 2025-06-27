import time
import json
import requests

API_URL = "http://localhost:5000/classify"

with open("logs/sample_logs.jsonl") as f:
    for line in f:
        log = json.loads(line)
        print(f"Sending log: {log['message']}")
        try:
            res = requests.post(API_URL, json={"log": log["message"]})
            print("Response:", res.json())
        except Exception as e:
            print("Failed to send:", e)
        time.sleep(2)  # simulate log delay