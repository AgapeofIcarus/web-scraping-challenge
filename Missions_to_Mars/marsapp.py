from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import flask_Pymongo
import scrape_mars
import sys

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

