# app.py
from flask import Flask, render_template, request
from scraper import scrape_quotes
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    quotes = []
    if os.path.exists("quotes.json"):
        with open("quotes.json", "r", encoding="utf-8") as f:
            quotes = json.load(f)
    return render_template("index.html", quotes=quotes)

@app.route("/scrape", methods=["POST"])
def run_scraper():
    quotes = scrape_quotes()
    return render_template("index.html", quotes=quotes)

if __name__ == "__main__":
    app.run(debug=True)