import requests

# Replace this with your GitHub username
GITHUB_USERNAME = "Tejaswini-Rout"

# GitHub API URL to fetch user events
URL = f"https://api.github.com/users/{GITHUB_USERNAME}/events"

response = requests.get(URL)

if response.status_code == 200:
    events = response.json()
    print(f"Fetched {len(events)} events for {GITHUB_USERNAME}")
else:
    print("Failed to fetch data. Check your internet or GitHub username.")
