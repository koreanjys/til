# scrapy

## scrapy-playwright

requests, bs4, selenium 만으로 많은 웹 사이트를 크롤링을 하려면 너무 많은 코드를 작성하고 전처리 등등 신경써야할게 많다.

특히 현재 진행중인 requests 기반 크롤링은 javascript 실행 문제라던지, 렌더링 문제들이 있고, 각 웹 페이지마다 처리해야 할 사항이 많다. 약 19개 url 중에 원하는 양식대로 크롤링 해온 수가 3개 밖에 되지 않았다. 그래서 웹 크롤링 프레임워크인 scrapy 필요성을 크게 꼈다.

