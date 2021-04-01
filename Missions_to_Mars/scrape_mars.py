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

    # Examine the results, then determine element that contains sought info
    # results are returned as an iterable list
    soup = BeautifulSoup(response.text, 'html.parser')
    title_results = soup.find_all('div', class_='content_title')[0]
    article_description = soup.find_all('div', class_='rollover_description_inner')[0]

    #Define title and content
    article_title = "NASA Ingenuity Mars Helicopter Prepares for First Flight"
    paragraph_text = "Now uncocooned from its protective carbon-fiber shield, the helicopter is being readied for its next steps."

    #Pull featured image using splinter
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    html = browser.html

    image_link = soup.find('img', class_='fancybox-image')['src']

    featured = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{image_link}'

    #Pull table from Mars Facts page
    mars_page = pd.read_html('https://space-facts.com/mars/')[0]

