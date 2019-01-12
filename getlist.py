#! usr/bin/env python

import re
import os
import pafy
from bs4 import BeautifulSoup

# This program downloads your youtube playlist. Display the youtube playlist in your browser and export it as html to a file.

list_name = input("Please enter the name of the html file: ")

dlocation = input("Press 1 for default path and 2 to select path: ")
if dlocation == "1":
    dlocation = os.getcwd()
if dlocation == "2":
    dlocation = input("Please enter the download path: ")
    #print(set([item for item in os.listdir(dlocation) if not re.match("\.", item)]))


# Opens the html file in the same directory as the program
with open(os.getcwd() + f"/{list_name}") as file:
    raw = file.read()

soup = BeautifulSoup(raw, "html.parser")

# Iterates over a genearted list of youtube video ids matched with regular expressions and downloads them
for counter, link in enumerate(set(re.findall(r"watch\?v=.{11}", soup.text)), 1):
    print(counter, link[8:], end =" ")
    video = pafy.new("https://www.youtube.com/" + link)
    print(video.title, end="  /n")
    # check for duplicates not implemented yet
    # if video.title + "." + video.getbest().extension not in os.listdir():
    video.getbest().download(quiet=False, filepath=dlocation)
    # else:
    #    print("Video already downloaded")


