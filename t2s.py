from bs4 import BeautifulSoup
import urllib
from gtts import gTTS
import re
import sys

dialogue = []
def twitterAccountFeed(feed):
    html = urllib.request.urlopen('https://twitter.com/'+feed)
    if html.getcode() == 200 and feed != '':
        parseTweets(html, feed)
    else:
        print("Invalid Twitter Feed")
        sys.exit(1)

def parseTweets(html, feed):
    bt = BeautifulSoup(html)
    for div in bt.findAll("div", {"class":"js-tweet-text-container"}):
        noUrl = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', div.text) # code from http://stackoverflow.com/questions/11331982/how-to-remove-any-url-within-a-string-in-python
        dialogue.append(noUrl)
    speech = ''.join(dialogue)
    try:
        tts = gTTS(text=speech, lang='en')
        tts.save(feed + '.mp3')
        print("Twitter feed has been converted to an mp3")
    except Exception as e:
        print("Error on audio conversion: ")
        print(e)
    # return menu()  # Use if you want to return to the menu after completion.

def menu():
    print(" ")
    print("/-- Tweet2Speech - Converts a user's Twitter feed to a spoken mp3 file --\\")
    print(" ")
    print("    [*] Be sure to have gTTS and bs4 modules installed before running")
    print("    [*] Input a twitter handle without the @ (i.e. DalaiLama)")
    print("    [*] An mp3 file will be output in the home folder")
    print("  ")
    feed = input("Enter the Twitter Name you want to capture (i.e. DalaiLama) : ")
    twitterAccountFeed(feed)

if __name__ == '__main__':
    menu()
