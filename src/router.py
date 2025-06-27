import requests
from config import SLACK_WEBHOOK_URL

CRITICAL_TYPES = {"CPU", "Memory", "Auth", "Crash"}

def send_slack_alert(message, incident_type):
    if incident_type not in CRITICAL_TYPES:
        print(f"Skipping non-critical incident: {incident_type}")
        return

    slack_msg = {
        "text": f":rotating_light: *{incident_type} Incident Detected!*\n```{message}```"
    }

    response = requests.post(SLACK_WEBHOOK_URL, json=slack_msg)

    print(f"Slack webhook status: {response.status_code}")
    print("Slack response:", response.text)

    if response.status_code != 200:
        print("Failed to send Slack alert!")






