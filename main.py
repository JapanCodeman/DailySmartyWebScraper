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
body = soup.body

post_item = soup.find_all('a', class_='post-link-title')

post = post_item
print(post)

links = []
