### `payload`
```
payload = {'name': 'value'}
```
해당 홈페이지 html에 동적으로 접근하기 위해서 선택한 name='name'의 값을 할당해주고, post로 받아올 수 있다.

```
import requests
from bs4 import BeautifulSoup


# 검색어를 입력할 URL
url = "http://www.spavalley.co.kr/naturepark/event/parkevent.asp"

# 검색어 입력 데이터
payload = {
    "sword": "동물탐험대"
}

# POST 요청을 통해 검색어를 입력하고 결과를 가져옴
response = requests.post(url, data=payload)

html = BeautifulSoup(response.text, 'lxml')

tag = '#content > ul > li > span > a'
print(html.select(tag)[0])
```

### `sword`
```
payload = {'sword': '검색키워드'}
```
입력 시 해당 url의 검색어를 동적으로 입력한게 되는지 정적인지는 아직 확인 필요하나,
동적으로 url 변경 없이 검색어 입력 결과를 html로 받아올 수 있다.