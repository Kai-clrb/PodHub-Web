from flask import Flask, render_template

app = Flask(__name__)

# Organizing podcasts into categories dynamically
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

if __name__ == "__main__":
    app.run(debug=True, host="192.168.14.57")
