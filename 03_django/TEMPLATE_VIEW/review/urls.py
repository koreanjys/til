from django.urls import path
from . import views

# 변수명 반드시 app_name 고정
# .html에서 링크주소 적을때 'review:이동할이름' 을 적는다.
app_name = 'review'  # 이름이 겹치지 않도록 app_name값을 준다.

# URL 구성 맨 앞에 'review/' 는 이미 master url 에서 검사가 끝남.
urlpatterns = [
    # 패턴 '(review/)index/' 가 *요청으로 들어온다면*, 함수실행.
    # 요청으로 들어온다는 뜻은 나한테 파일이 있다는게 아니고
    # 클라이언트가 url주소 끝에 ~/index/ 가 온다는 뜻임!
    path('index/', views.index, name='index'),
    path('hello/', views.hello, name='hello')
]

# review/hello/ => view hello 함수실행 => hello.html을 응답(렌더)