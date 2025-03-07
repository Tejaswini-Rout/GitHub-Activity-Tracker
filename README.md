# Git Tracker

## Overview
Git Tracker is a web application that allows users to track their GitHub activity, including push events, pull requests, issues, forks, and more. The application fetches user activity from the GitHub API and displays it in an interactive UI.

## Features
- Track GitHub activity by entering a username.
- Filter events by type (Push, Pull Requests, Issues, etc.).
- Displays activity in a clean, structured format.
- Built with Flask (backend) and HTML, CSS, JavaScript (frontend).

## Installation
### Prerequisites
- Python 3 installed
- Flask installed (`pip install flask`)

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd git-tracker
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python app.py
   ```
4. Open the browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter a GitHub username in the input field.
2. Select an event type from the dropdown.
3. Click "Track Activity" to fetch and display GitHub activity.

## Technologies Used
- **Backend**: Flask, GitHub API
- **Frontend**: HTML, CSS, JavaScript

## Contributing
Feel free to fork this repository and submit pull requests.

## License
This project is open-source and available under the MIT License.

