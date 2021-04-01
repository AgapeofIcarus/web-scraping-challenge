from flask import Flask, render_template, redirect
from flask_pymongo import Pymongo
import scrape_mars
import sys

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def index():
    mars_data = mongo.db.mars.find_one()
    
    return render_template("index.html", data=mars_data)

@app.route("/scrape")
def scrape():  
    scraped_data = scrape_mars.scrape()
    print(scraped_data)
    mongo.db.mars.update({}, scraped_data, upsert=True)
    return redirect("http://localhost:5000/", code=302)

    if __name__ == "__main__":
        app.run(debug=True)

