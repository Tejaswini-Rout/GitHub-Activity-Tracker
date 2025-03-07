from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/{}/events"

def fetch_github_activity(username):
    """Fetch GitHub activity for a given username"""
    url = GITHUB_API_URL.format(username)  # Fixed URL formatting
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return []  # Return empty list if API fails

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/track", methods=["POST"])
def track():
    username = request.form["username"]
    events = fetch_github_activity(username)

    filtered_events = [
        {"type": event["type"], "repo": event["repo"]["name"], "created_at": event["created_at"]}
        for event in events
    ]

    return jsonify(filtered_events)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import requests
import logging

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/{}/events"

def fetch_github_activity(username):
    """Fetch GitHub activity for a given username"""
    try:
        url = GITHUB_API_URL.format(username)
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch GitHub activity: {e}")
        return []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/track", methods=["POST"])
def track():
    try:
        username = request.form["username"]
        if not username:
            return jsonify({"error": "Username is required"}), 400
        events = fetch_github_activity(username)
        filtered_events = [
            {"type": event["type"], "repo": event["repo"]["name"], "created_at": event["created_at"]}
            for event in events
        ]
        return jsonify(filtered_events)
    except Exception as e:
        logging.error(f"Failed to track GitHub activity: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)