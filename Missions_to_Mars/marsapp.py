from flask import Flask, render_template, redirect
from flask_pymongo import Pymongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/marsapp"
mongo = Pymongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.mars.find_one()
    
    return render_template("index.html", data=mars_data)

@app.route("/scrape")
def scrape(): 
    mars = mongo.db.mars 
    scraped_data = marsapp.scrape()
    print(scraped_data)
    mars.update({}, scraped_data, upsert=True)
    return redirect("/", code=302)

    if __name__ == "__main__":
        app.run(debug=True)

