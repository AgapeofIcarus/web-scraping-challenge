# web-scraping-challenge
 UNCC Data Bootcamp project for web scraping.
![Web-scraping-challenge](https://github.com/AgapeofIcarus/web-scraping-challenge/blob/main/mission_to_mars.png?raw=true)

In this project for UNCC's Data Analytics Bootcamp, we were to use scraping and splinter to pull facts about Mars, then place them onto a functional page. To accomplish this, I did the following:

* Scraped [NASA Mars News Site](https://mars.nasa.gov/news/) for the most recent news title and paragraph.
* Used splinter to pull the current featured image from (https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html).
* Used splinter to pull images of each of Mars' hemispheres from (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).
* Created flask application with scraped data to create a full display of data.
