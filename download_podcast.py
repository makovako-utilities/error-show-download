#!/usr/bin/env python3

from urllib import request
import json
import sys
import re
import os

try:
    from progressbar import ProgressBar
except ImportError:
    porgress_bar_available = False
else:
    progress_bar_available = True


pbar = None

def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = ProgressBar(maxval=total_size)

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

if __name__ == "__main__":
    path = ""
    if len(sys.argv) > 1:
        path = sys.argv[1] + "/"

    with open('urls.json','r') as fp:
        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        request.install_opener(opener)
        
        podcasts = json.load(fp)
        for podcast in podcasts:
            filename = path + f"{podcast['title']}.mp3".replace("/","_") # Please, never use "/" in any name, see episode 86
            url = podcast['url']
            if os.path.exists(filename):
                site = request.urlopen(url)
                meta = site.info()
                if os.path.getsize(filename) >= int(meta["Content-Length"]):
                    print(f"Skipping {podcast['title']}")
                    continue
               
            print(f"Downloading {podcast['title']}")
            if progress_bar_available:
                request.urlretrieve(url, filename, show_progress)
            else:
                request.urlretrieve(url, filename)
            

    

