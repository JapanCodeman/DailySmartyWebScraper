"""
Build a web scraping algorithm that pulls data from http://www.dailysmarty.com/topics/python

Should return the various post links in a normal English format

For example:


'Installing Anaconda Python Data Science Platform'

Suggested modules to use:

- requests
- inflection
- beautifulsoup4
"""

import requests
import inflection
import bs4 as bs
import pprint as pprint
import lxml

source = requests.get('http://www.dailysmarty.com/topics/python').text

soup = bs.BeautifulSoup(source, 'lxml')

tags = soup.find_all('a', href=True)

all_tags = []
card_titles = []
test_list = []

for tag in tags:
    all_tags.append(tag['href'])


def clean_up_tag(tag):
    if tag[0:7] == '/posts/':
        card_titles.append(tag[7:])


for tag in all_tags:
    clean_up_tag(tag)


for i in card_titles:
    print(inflection.titleize(i))


