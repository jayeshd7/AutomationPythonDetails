import request
import requests
import bs4
import pandas as pd
import numpy as np
import tensorflow as tf
import sklearn
import moment

x = moment.now()
y = moment.date("12-18-2012", "%m-%d-%Y")

print(x)
print(y)


print(sklearn)
print(tf.__version__)





response = requests.get('https://en.wikipedia.org/wiki/Main_Page')

print(response.status_code)


#r = requests.post('https://facebook.com/post', data = {'key':'value'})

soup_obj = bs4.BeautifulSoup(response.text, 'lxml')

print(soup_obj.prettify())

text = soup_obj.select('title')[0].getText()

print(text)


links = soup_obj.findAll('a')

for link in links:
    print("--------------")
    print(link.get(0))
    print(link.get('href'))


print(tf.__version__)


#print(links.count())

