#!/usr/bin/env python3
"""
This script parses JB site and saves podcats titles and mp3 urls in json file
"""

from bs4 import BeautifulSoup
import requests
import time
import json

LIST_URL = "https://www.jupiterbroadcasting.com/show/error/page/"

podcasts = []

def get_audio_url(site_url):
    """
    Parse podcast site for mp3 url
    """
    res = requests.get(site_url)
    soup = BeautifulSoup(res.text, "html.parser")
    for direct_download in soup.find(id="direct-downloads").find('ul').findAll('li'):
        a = direct_download.find('a')
        if "Audio" in a.text:
            return a["href"]

    

if __name__ == "__main__":
    """Loop trough all podcasts and save info"""
    for i in range(1,9):
        res = requests.get(LIST_URL+str(i))
        soup = BeautifulSoup(res.text,"html.parser")
        videogallery = soup.find(id="videogallery")
        for videoitem in videogallery.select('.videoitem'):
            thumbnail = videoitem.find(class_="thumbnail")
            a = thumbnail.find('a')
            video_url = a['href']
            url = get_audio_url(video_url)
            video_title = a['title']
            video_title = video_title.rsplit('|',1)
            video_title.reverse()
            video_title = " | ".join(video_title)
            podcasts.append({
                "title":video_title,
                "url":url
            })
        time.sleep(5)

    """Write data to json file"""
    with open('urls.json','w') as fp:
        json.dump(podcasts, fp, indent = 4)
