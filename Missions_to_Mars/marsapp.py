from flask import Flask, render_template, redirect
from flask_pymongo import Pymongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = Pymongo.MongoClient(conn)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = Pymongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.mars.find_one()
    
    return render_template("index.html", data=mars_data)

@app.route("/scrape")
def scrape():  
    scraped_data = scrape_mars.scrape()
    print(scraped_data)
    mongo.db.mars.update({}, scraped_data, upsert=True)
    return redirect("/", code=302)

    if __name__ == "__main__":
        app.run(debug=True)

