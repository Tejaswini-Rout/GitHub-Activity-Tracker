document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("track-form").addEventListener("submit", function (event) {
        event.preventDefault();
        
        let username = document.getElementById("username").value.trim();
        let activityList = document.getElementById("activity-list");
        let loading = document.getElementById("loading");

        if (!username) {
            alert("⚠️ Please enter a valid GitHub username.");
            return;
        }

        activityList.innerHTML = "";
        loading.classList.remove("hidden"); // Show loading message

        fetch("/track", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: "username=" + encodeURIComponent(username)
        })
        .then(response => response.json())
        .then(data => {
            loading.classList.add("hidden"); // Hide loading message
            if (data.length === 0) {
                activityList.innerHTML = "<p>No recent activity found.</p>";
                return;
            }

            data.forEach(event => {
                let listItem = document.createElement("li");
                listItem.innerHTML = `<strong>${event.type}</strong> - 🏷️ <b>${event.repo}</b> - 📅 ${new Date(event.created_at).toLocaleString()}`;
                activityList.appendChild(listItem);
            });
        })
        .catch(error => {
            loading.classList.add("hidden");
            console.error("Error fetching data:", error);
            alert("❌ Failed to fetch activity. Try again later.");
        });
    });
});
