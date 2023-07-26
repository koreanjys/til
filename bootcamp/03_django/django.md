# **django 를 시작하다**
## 2023-01-04
### django 초기 실행모습
새해 장고프로젝트를 시작하다.

1. 장고 다운로드 받음
2. pip install django
3. django-admin => django로 할수있는 일을 볼수있는 명령어
4. django-admin startproject first_project 명령어로 첫 프로젝트를 열다.
5. first_project 폴더 안에서 python manage.py를 보면 쓸수있는 명령어를 볼수있다.
6. python manage.py startapp hello 명령어로 새로운 first_project라는 회사?(마스터앱)안에 hello라는 부서(앱)를 개설하다.
7. MTV모델을 이용하여 장고를 해보자

- View(컨트롤타워) Model(DB) Tamplate(html)

8. python manage.py runserver 로 서버를 시작

### views.py
```
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def hihihi(request):
    numbers = list(range(1, 46))
    return HttpResponse(numbers)
```
views.py 안에 내용
함수 hihihi를 만든것이다.

### urls.py
```
from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wow/', views.hihihi),
]
```
urls.py 안에 path('wow/', views.hihihi) 를 추가했다.

### settings

마스터앱(처음 만든 startproject 안에 폴더)에 있는 settings.py를 잘 이용해야한다.

만약 app을 하나 만들었다면
```
python manage.py startapp app_name
```

settings.py 안에 `INSTALLED_APPS` 라는 이름의 

리스트가 있는데 여기에 'app_name'을 적어 줘야 한다.

만든 app을 삭제하려면 간단하다. 폴더를 삭제해주고

settings에 적어놓은 앱이름을 삭제한다.


### django html 그리고 python

여러가지를 복합적으로 이용해서 흐름을 익혀봤고,

CSS는 적용해보고 싶었지만 아직 잘 모르겠다.

### 오늘 배운 내용을 이용해 순서대로 서버를 열어본다면

1. pip install django
2. django-admin startproject project_name
3. python manage.py startapp app_name
4. settings 안에 인스톨앱 리스트에 app_name을 적어준다.
5. 마스터앱의 urls.py 에 경로 지정 (include)를 쓰면 좋음
6. 앱폴더 안에 urls.py를 만들어서 나머지 경로를 지정하고 views.py에 함수를 만들고 연결한다. views.py에 함수를 만들때 예시
   ```
from django.shortcuts import render
from django.http.response import HttpResponse

import random

def hello_world(request):
    # 응답으로 HTML을 렌더링 하겠다.
    # django => 무조건 HTML 파일은 폴더명 templates/ 에서 찾는다.
    return render(request, 'hello_world.html')


def lunch(request):
    menus = [
        '짜장', '보쌈',
        '삼겹살', '치킨',
        '샐러드', '굶기',
    ]
    menu = random.choice(menus)
    context = {
        'menu': menu,
    }
    return render(request, 'lunch.html', context)

def lotto(request):
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()

    context = {
        'numbers': numbers,
        'is_jackpot': True,
    }
    return render(request, 'lotto.html', context)
    ```

7. 마스터앱 폴더안에 templates를 만들어서 base.html을 만들어 베이스를 만든다. {%%}를 이용. 자식 html 첫부분에 {% extends 'base.html' %}도 잘 적고. 
8. 마스터앱 폴더안에 settings에서 베이스html경로지정도 적어주자. => 'DIRS': [ BASE_DIR / 'templates', ],
9.  vscode extend에서 django를 다운로드 받고
10. vscode settings 에서 인클루드랭귀지?를 잘 넣는다.
11. 음 그리고 앱폴더안의 templates폴더에 .html을 작성해서 잘 꾸며서 실행해보자.
12. 그리고 django를 vscode 익스텐드에서 잘 설치하였으면, html안에서 파이썬 문법을 {%}를 이용해서 사용할수 있게 된다. 


## 2023-01-05

### 오늘의 핵심 내용 요약

1. 어제와 동일한 URL => View => Template
2. 앞으로 urls.py 에서 app_name = 'APP_NAME' 과 path('', views.func, name='PATTERN_NAME') 설정하기
3. 템플릿에서 {% url 'APP_NAME:PATTERN_NAME' %} 으로 링크 생성 가능
4. App 마다 html 파일 이름이 겹칠경우 django에서 제대로 인식하지 못함
 
    >app/ > templates/ > app/ > html 파일들 방식으로 구분

5. 사용자 입력을 받아보자
    >Variable Routing
    
        1. url pattern 에서 'hello/<str:name>/' 식으로 원하는 부분 변수화 가능
        2. 해당 URL과 매칭된 View 함수에서 def hello(reqeust, name): 으로 값 접근 가능
    >Form & Input

        1. 총 두가지 요청으로 구성됨! 입력창 받는 요청 / 데이터 제출하는 요청
        2. <form action="URL" method="GET / POST"> 메서드는 선택가능
        3. GET 은 입력내용이 URL에 다 나옴
        4. POST 는 나오지 않지만 {% csrf_token %} 을 필요로 함
        5. View 함수의 기본 인자 request 에서 넘어온 입력 데이터 접근가능
        6. GET 요청의 데이터는 request.GET['key']
        7. POST 요청의 데이터는 request.POST['key'] 로 접근