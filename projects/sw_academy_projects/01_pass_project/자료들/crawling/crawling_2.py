import requests
from bs4 import BeautifulSoup

url = 'https://data.seoul.go.kr/dataList/OA-2734/S/1/datasetView.do'
response = requests.get(url, timeout=10) # timeout 값은 초 단위로 설정됩니다.
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'tbl_data tbl_g type01'})
rows = table.find_all('tr')

for row in rows:
    columns = row.find_all('td')
    if len(columns) < 5:
        continue
    print(f"{columns[0].text.strip()} / {columns[2].text.strip()} / {columns[4].text.strip()}")
