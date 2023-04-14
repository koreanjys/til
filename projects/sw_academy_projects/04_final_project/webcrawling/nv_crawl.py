import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# 네이버쇼핑 & 검색결과
base_url = 'https://search.shopping.naver.com/search/all?query='
query = input('검색어 입력 : ')
url = base_url + query

# url html 불러오기
html = requests.get(url).content

# bs로 파싱
bs = BeautifulSoup(html, 'lxml')

# # 'tag.class > tag'
# for text in bs.select_one('div.basicList_title__VfX3c > a'):
#     print(text)

# base => 네이버 랭킹 & 리뷰 많은 순서 정렬
for text in bs.select('em.basicList_num__sfz3h'):
    print(text)
    