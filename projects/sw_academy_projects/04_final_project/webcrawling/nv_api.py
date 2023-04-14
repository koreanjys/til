import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import os

keys = []

with open('API_KEY.txt', 'r') as key:
    for line in key.readlines():
        text = line.strip()
        if text != '':
            keys.append(text.split(':')[1])

query = '엘지 세탁기'
url = f'https://openapi.naver.com/v1/search/shop?query={query}'

headers = {
    'X-Naver-Client-Id' : keys[0], 
    'X-Naver-Client-Secret': keys[1]
}


response = requests.get(url, headers=headers)
text = response.json()

print(text['items'][0])

