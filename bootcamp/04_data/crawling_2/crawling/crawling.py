import requests
from bs4 import BeautifulSoup
import pandas as pd

# 크롤링할 페이지의 URL
url = 'https://finance.naver.com/item/sise_day.nhn?code=005930&page=1'

# 빈 데이터프레임 생성
samsung_stock = pd.DataFrame()

# 2022년 1월 1일부터 2022년 12월 31일까지의 데이터를 가져옴
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
for page in range(1, 61):
    pg_url = '{}&page={}'.format(url, page)
    response = requests.get(pg_url, headers=headers)
    html = BeautifulSoup(response.content, 'html.parser')
    table = html.select('table')
    table = pd.read_html(str(table))[0]
    table = table.dropna()
    samsung_stock = pd.concat([samsung_stock, table], ignore_index=True)


# 데이터프레임을 csv 파일로 저장
samsung_stock.to_csv('samsung_stock.csv', index=False, encoding='utf-8-sig')
