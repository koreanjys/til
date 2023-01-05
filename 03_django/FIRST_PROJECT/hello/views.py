from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def hello_world(requests):
    # 응답으로 HTML을 렌더링 하겠다.
    # django => 무조건 HTML 파일은 폴더명 templates/ 에서 찾는다.
    return render(request, 'hello_world.html')