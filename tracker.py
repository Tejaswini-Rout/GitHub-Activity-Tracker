import requests
# Ask user for GitHub username
GITHUB_USERNAME = input("Enter GitHub username: ").strip()

# Predefined event types for selection
EVENT_TYPES = [
    "PushEvent", "PullRequestEvent", "IssuesEvent", 
    "ForkEvent", "WatchEvent", "CreateEvent"
]

# Display choices
print("\nSelect an event type to filter:")
for i, event in enumerate(EVENT_TYPES, start=1):
    print(f"{i}. {event}")

# Get user selection
try:
    choice = int(input("\nEnter your choice (1-6): "))
    if 1 <= choice <= len(EVENT_TYPES):
        EVENT_TYPE = EVENT_TYPES[choice - 1]
    else:
        print("❌ Invalid choice. Defaulting to 'PushEvent'.")
        EVENT_TYPE = "PushEvent"
except ValueError:
    print("❌ Invalid input. Defaulting to 'PushEvent'.")
    EVENT_TYPE = "PushEvent"

# GitHub API URL to fetch user events
URL = f"https://api.github.com/users/{GITHUB_USERNAME}/events"

# Fetch data from GitHub API
try:
    response = requests.get(URL, timeout=10)
    response.raise_for_status()  # Raise an error for bad responses

    events = response.json()
    filtered_events = [event for event in events if event["type"] == EVENT_TYPE]

    if filtered_events:
        print(f"\n✅ Fetched {len(filtered_events)} '{EVENT_TYPE}' events for {GITHUB_USERNAME}")
        for event in filtered_events[:5]:  # Show only the latest 5 filtered events
            created_at = event.get("created_at", "Unknown Time")
            repo_name = event.get("repo", {}).get("name", "Unknown Repo")
            print(f"➡️ {EVENT_TYPE} in {repo_name} at {created_at}")
    else:
        print(f"\n⚠️ No '{EVENT_TYPE}' events found for {GITHUB_USERNAME}.")
except requests.exceptions.RequestException as e:
    print(f"❌ Error fetching data: {e}")
