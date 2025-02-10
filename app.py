from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from waitress import serve

app = Flask(__name__)


REPLIT_URL = "https://f3000fa3-e3db-4044-81af-e677b1311973-00-24ik16vgp1blm.sisko.replit.dev/"

podcasts_by_category = {
    "Sports": [
        {"title": "Anshul Jubli & Ranveer Allahbadia", "description": "Description", "file": "static/Podcasts/Anshul Jubli & Ranveer Allahbadia.mp3"},
        {"title": "Nitin Gadkari & Raj Shamani", "description": "Description", "file": "static/Podcasts/Nitin Gadkari & Raj Shamani.mp3"},
        {"title": "Sunil Chhetri & Raj Shamani", "description": "Description", "file": "static/Podcasts/Sunil Chhetri & Raj Shamani.mp3"},
    ],
    "Politics": [
        {"title": "Arvind Kejriwal & Prakhar Gupta", "description": "Description", "file": "static/Podcasts/Arvind Kejriwal & Prakhar Gupta.mp3"},
    ],
    "Comedy": [
        {"title": "Kapil Dev & Ranveer Allahbadia", "description": "Description", "file": "static/Podcasts/Kapil Dev & Ranveer Allahbadia.mp3"},
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/podcasts")
def podcasts():
    return render_template("podcasts.html", categories=podcasts_by_category.keys(), podcasts_by_category=podcasts_by_category)

@app.route("/about")
def about():
    return render_template("about.html")

# Function to keep Replit awake
def keep_awake():
    try:
        requests.get(REPLIT_URL)
        print("✅ Pinging to keep Replit awake...")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error pinging the app: {e}")

# Schedule the pinging function every 5 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(func=keep_awake, trigger="interval", minutes=5)
scheduler.start()

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
