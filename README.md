# Archiving of a podcast

After announcing the end of the **User Error** I wanted to backup all episodes. Youtube-dl could download episodes from current rss podcast feed, but there isn't every episode. So I created this set of scripts.

# Files

## download_podcast.py

- downloads all episodes listed in *urls.json* file.
- you don't need any additional dependencies to run it
- if you want to see progressbar, install module progressbar2 - `pip install progressbar2`
- it will resume from interrupted download (will redownload unfinished file)
- if you want to download to different directory, specify it as a command line argument, e.g. *./download_podcast.py different/direcotory/*

## parse_metadata.py

- scrapes JB website for links and titles of every episode and saves it to *urls.json* file as a list of objects
- to make this script run, install dependencies from requirements file - `pip install -r requirements.txt` (I recommend setting up virtual environment, use google)
- you don't need to run this script, output is already saved in *urls.json* file

## urls.json

- list of episodes
- each episode has title and url from the JB website