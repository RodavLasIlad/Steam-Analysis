# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 10:57:59 2014

@author: Brett
"""
# Import 
from bs4 import BeautifulSoup
import requests
import re

gamesdictionary = {}

gtaURL = "http://www.metacritic.com/game/pc/grand-theft-auto-v"
fakeHeader = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(gtaURL, headers=fakeHeader)
data = r.text
soup = BeautifulSoup(data)

gameName = soup.findAll("span", {"class" : "product_name"})
print gameName[0].get_text()

userScore = soup.findAll("div", {"class" : "metascore_w user large game positive"})
print userScore[0].get_text()

metaScore = soup.findAll("span", {"itemprop" : "ratingValue"})
print metaScore[0].get_text()

reviews = soup.findAll("div", {"class" : "review_body"})
for i in range(len(reviews)):
    temp = reviews[i].get_text().lower()
    tempText = re.split('\W+', temp)
    print tempText
    print "-" * 25
    
critics = soup.findAll("div", {"class" : "review_critic"})

for i in range(len(critics)):
    critics.findAll("href")
    print critics[i].get_text()
    
reviews = soup.findAll("div", {"class" : "review_section"})
temp[0]'

r = soup.findAll("div", {"class" : "review_btm"})
r[27].findAll("div", {"class" : "review_critic"})




##### list of games

from bs4 import BeautifulSoup
import requests
import re

fakeHeader = {'User-Agent': 'Mozilla/5.0'}
URLStart = "http://www.metacritic.com/game"

gameDict = {}

games = ["grand-theft-auto-v"]
platforms = ["pc", "playstation-3", "playstation-4", "xbox-360", "xbox-one"]


for game in games:
    for platform in platforms:          
        currURL = URLStart + "/" + platform + "/" + game
        r = requests.get(currURL, headers=fakeHeader)
        data = r.text
        currSoup = BeautifulSoup(data)
        
        # Name
        gameName = currSoup.findAll("span", {"itemprop" : "name"})[0].get_text().strip()
        ## Summary
        summary = currSoup.findAll("ul", {"class" : "summary_details"})
        # Published Date
        datePublished = summary[0].findAll("span", {"itemprop" : "datePublished"})[0].get_text().strip()
        # Publisher
        publisher = summary[2].findAll("span", {"class" : "data"})[0].get_text().strip()
        # Genre
        genre = summary[2].findAll("span", {"itemprop" : "genre"})[0].get_text().strip()
        # Metascore
        metaScore = currSoup.findAll("span", {"itemprop" : "ratingValue"})[0].get_text().strip()
        # Description (rating)
        desc = currSoup.findAll("span", {"class" : "desc"})[0].get_text().strip()
        # Review Count
        revCount = currSoup.findAll("span", {"itemprop" : "reviewCount"})[0].get_text().strip()
        

## Build dictionary with general info on game

# Systems
# Amount of critics

## Build a dictionary of reviews from bigger companies
# Review text
# Game Company
# Review Score

## Build a dictionary of reviews from users
# Review text
# Helpful rating
# Review score
# Name of reviewer
# When reviewed
