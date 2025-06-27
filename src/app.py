from flask import Flask, request, jsonify
from model import classify_log
from flask_cors import CORS
from router import send_slack_alert


app = Flask(__name__)
CORS(app)  # For frontend integration later

@app.route("/")
def home():
    return "Incident Classifier API is running"

@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json()
    log_message = data.get("log", "")
    if not log_message:
        return jsonify({"error": "Missing 'log' in request"}), 400


    incident_type = classify_log(log_message)
    send_slack_alert(log_message, incident_type)
    return jsonify({"incident_type": incident_type})


if __name__ == "__main__":
    app.run(debug=True)
