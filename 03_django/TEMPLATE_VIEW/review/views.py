# review/views.py

from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    # 응답(Response)는 결국 => HTML render
    # render(1. request | 2. HTML 이름 | 3(선택). 넘길 데이터)
    return render(request, 'review/index.html')


def hello(request):

    return render(request, 'review/hello.html')

