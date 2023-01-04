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
6. 앱폴더 안에 urls.py를 만들어서 나머지 경로를 지정하고 views.py에 함수를 만들고 연결한다.
7. 마스터앱 폴더안에 templates를 만들어서 base.html을 만들어 베이스를 만든다. {%%}를 이용. extends도 잘 적고.
8. vscode extend에서 django를 다운로드 받고
9. vscode settings 에서 인클루드랭귀지?를 잘 넣는다.
10. 음 그리고 앱폴더안의 templates폴더에 .html을 작성해서 잘 꾸며서 실행해보자.
11. 그리고 django를 vscode 익스텐드에서 잘 설치하였으면, html안에서 파이썬 문법을 {%}를 이용해서 사용할수 있게 된다. 