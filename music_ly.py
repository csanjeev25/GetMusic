from bs4 import BeautifulSoup
import requests
import sys
import os


def show_lyrics():
    artist = input("enter the name of the ARTIST : ")
    artist = artist.lower().replace(" ","-")
    track = input("enter the name of the TRACK : ")
    track = track.lower().replace(" ","-")
    url = 'http://www.metrolyrics.com/' + track + '-lyrics-' + artist + '.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    lyrics = soup.find_all("p", {"class":"verse"})
    for i in lyrics:
        print(i.text)

show_lyrics()
