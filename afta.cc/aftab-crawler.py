import requests 
from bs4 import BeautifulSoup as bs
import re 
import datetime

print(datetime.datetime.now())

def search_key_word():
    
    words = dict()
    for i in range(1714,1,-1):
        print(f"checking {i}")
        req = requests.get(f"https://aftab.cc/article/{i}")
        soup = bs(req.text, 'html.parser')
        story = soup.find('div', attrs={'class': 'storycontent'})
    
        
        try:
            for i in story.text.split(' '):
                words[i] = words.get(i, 0) + 1
        except AttributeError as error:
            print(error)
            continue
    
    print(datetime.datetime.now())

    
    with open('aftab.counter', 'w') as f:
        for word in sorted(words, key=words.get, reverse=True):
        
            f.write(f"{word} => {words[word]}" + '\n')

search_key_word()
