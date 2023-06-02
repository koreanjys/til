# `비동기 자바스크립트 렌더링을 위한 라이브러리 requests-html`

## `install`

```
pip install requests-html
```
- 여기서 주의할 것은 install 할때 -(bar) 와 import 할때 _(under bar)가 다르다는 것 

## `필요한 라이브러리들을 불러와야 한다.`

```
import nest_asyncio
from requests_html import AsyncHTMLSession
```

## `nest_asyncio 활성화`

- 여기서 nest_asyncio를 활성화 시켜 줘야 에러가 발생하지 않았다.
- 위에서 말한 에러는 이벤트 루프가 실행중이라 렌더링 못한다는 에러다.(jupyter notebook 기준)
- 아래는 nest_asyncio 활성화 코드
```
nest_asyncio.apply()
```
- 위 코드가 기본적으로 실행 되어 있어야 한다.

## `렌더링`

```
import nest_asyncio
from requests_html import AsyncHTMLSession

# nest_asyncio 활성화
nest_asyncio.apply()

# 비동기 세션 생성
asession = AsyncHTMLSession()
url = 'https://www.kintex.com/web/ko/event/list.do?searchType=&searchStartMon=202305&searchEndMon=202305&searchStartDt=&searchEndDt='
r = await asession.get(url)
```
- 위와 같이 비동기 세션을 생성한 후 .get(url)로 크롤링해왔다.
