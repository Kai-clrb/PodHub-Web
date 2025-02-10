from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
import requests
from waitress import serve

app = Flask(__name__)


REPLIT_URL = "https://f3000fa3-e3db-4044-81af-e677b1311973-00-24ik16vgp1blm.sisko.replit.dev/"

podcasts_by_category = {
    "Sports": [
        {"title": "Anshul Jubli & Ranveer Allahbadia", "description": "In this episode of The Ranveer Show, Ranveer Allahbadia engages in a conversation with Anshul Jubli, an Indian mixed martial artist. They discuss Anshul's early life, his journey into martial arts, challenges, and the aggression inherent in the sport. Anshul shares insights into his training regimen, the state of MMA in India, and his aspirations for the future. The discussion provides a deep dive into the life of a professional fighter and the dedication required to succeed in the sport. ", "file": "static/Podcasts/Anshul Jubli & Ranveer Allahbadia.mp3"},
        {"title": "Sunil Chhetri & Raj Shamani", "description": "In this episode of the Figuring Out podcast, Raj Shamani sits down with Sunil Chhetri, the captain of the Indian national football team. They discuss Chhetri's early life, his passion for football, and the challenges he faced in his career. The conversation covers topics such as leadership, discipline, and the growth of football in India. Chhetri shares anecdotes from his journey, offering inspiration and insights into the life of a professional athlete.", "file": "static/Podcasts/Sunil Chhetri & Raj Shamani.mp3"},
        {"title": "Kapil Dev & Ranveer Allahbadia", "description": "In this episode of The Ranveer Show, Ranveer Allahbadia interviews Kapil Dev, the legendary Indian cricketer. They discuss Kapil Dev's early life, his cricketing career, and the historic 1983 World Cup win. The conversation touches upon leadership, teamwork, and the evolution of cricket in India. Kapil Dev shares insights into his philosophy of life, fitness, and the importance of staying grounded despite success.", "file": "static/Podcasts/Kapil Dev & Ranveer Allahbadia.mp3"},
    ],
    "Politics": [
        {"title": "Arvind Kejriwal & Prakhar Gupta", "description": "On the Figuring Out podcast, Raj Shamani interviews Arvind Kejriwal, the Chief Minister of Delhi. The discussion covers Kejriwal's journey from an IRS officer to a political leader, his views on governance, and the challenges of politics in India. They delve into topics such as education, healthcare, and the vision for Delhi's development. Kejriwal shares his experiences and the principles that guide his political career.", "file": "static/Podcasts/Arvind Kejriwal & Prakhar Gupta.mp3"},
    ],
    "Infrastructure and Development": [
        {"title": "Nitin Gadkari & Raj Shamani", "description": "On the Figuring Out podcast, host Raj Shamani converses with Shri Nitin Gadkari, India's Minister for Road Transport and Highways. The episode delves into Gadkari's visionary approach to infrastructure development and sustainable transportation in India. He discusses building world-class highways, promoting electric mobility, and innovative solutions to urban congestion and pollution. Gadkari also touches upon his broader vision for economic growth, job creation, and rural development. The conversation offers valuable insights into the future of India's transportation landscape. ", "file": "static/Podcasts/Nitin Gadkari & Raj Shamani.mp3"}
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
