from bs4 import BeautifulSoup
import urllib
from gtts import gTTS
import re

dialogue = []
def twitterAccountFeed(feed):
    html = urllib.urlopen('https://twitter.com/'+feed)
    bt = BeautifulSoup(html)
    for div in bt.findAll("div", {"class":"js-tweet-text-container"}):
        noUrl = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', div.text) # code from http://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
        dialogue.append(noUrl)
    speech = ''.join(dialogue)
    tts = gTTS(text=speech, lang='en')
    tts.save(feed + '.mp3')


twitterAccountFeed("DalaiLama")