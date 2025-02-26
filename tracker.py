import requests

# Replace with your GitHub username
GITHUB_USERNAME = "Tejaswini-Rout"
URL = f"https://api.github.com/users/{GITHUB_USERNAME}/events"

response = requests.get(URL)

if response.status_code == 200:
    events = response.json()
    print(f"Fetched {len(events)} events for {GITHUB_USERNAME}")

    # Print recent events
    for event in events[:5]:  # Show only the latest 5 events
        print(f"➡️ Event: {event['type']} at {event['created_at']}")
else:
    print("Failed to fetch data. Check your internet or GitHub username.")
