from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/podcasts")
def podcasts():
    podcast_data = [
        {"title": "Anshul Jubli & Ranveer Allahbadia", "description": "Description", "category": "Sports", "file": "static/Podcasts/Anshul Jubli & Ranveer Allahbadia.mp3" },
        {"title": "Arvind Kejriwal & Prakhar Gupta", "description": "Description", "category": "Politics", "file": "static/Podcasts/Arvind Kejriwal & Prakhar Gupta.mp3" },
        {"title": "Kapil Dev & Ranveer Allahbadia", "description": "Description", "category": "Comedy", "file": "static/Podcasts/Kapil Dev & Ranveer Allahbadia.mp3" },
        {"title": "Nitin Gadkari & Raj Shamani", "description": "Description", "category": "Sports", "file": "static/Podcasts/Nitin Gadkari & Raj Shamani.mp3" },
        {"title": "Sunil Chhetri & Raj Shamani", "description": "Description", "category": "Sports", "file": "static/Podcasts/Sunil Chhetri & Raj Shamani.mp3"},
    ]
    return render_template("podcasts.html", podcasts=podcast_data)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, host= '192.168.172.57')
