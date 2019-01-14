from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

songs = pd.read_csv("/Users/vishalpatel/Documents/Coding/flatiron/Blog 2/songs.csv")

def iterate_over_songs(songs):
    for idx, song in songs.iterrows():
        song_name = songs['Name of Song'][idx]
        url = songs['Genius URL'][idx]
        scrape_lyrics_to_txt('https://genius.com/Eminem-rap-god-lyrics', 'Eminem - Rap God')

def scrape_lyrics_to_txt(url, song_name):

    req = requests.get(url)
    html = BeautifulSoup(req.content, 'html.parser')
    all_text = html.find('div', {'class': 'lyrics'}).text
    lines = all_text.split('\n')
    regex = re.compile('([\][])')
    regex.search('test')

    lyrics = [line  for line in lines if len(line)> 0 and not regex.search(line)]

    with open(song_name + '.txt', "w") as text_file:
        for lyric in lyrics:
            text_file.write(lyric + '\n')


iterate_over_songs(songs)
