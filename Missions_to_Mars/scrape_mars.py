#Import dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import pymongo

#url to be scraped
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape():
    browser = init_browser()

    mars_scrape = {}

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    title_results = soup.find_all('div', class_='content_title')[0]
