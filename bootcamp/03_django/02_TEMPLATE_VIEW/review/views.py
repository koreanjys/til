# review/views.py

from django.shortcuts import render

def index(request):
    # 응답은 결국 => HTML render
    # render(1. request | 2. HTML 이름 | 3. 넘길 데이터)
    return render(request, 'review/index.html')

def hello(request):

    return render(request, 'review/hello.html')


'https://www.acmicpc.net/problem/1861'
'https://www.acmicpc.net/problem/1860'
'https://www.acmicpc.net/problem/1862'
'https://www.acmicpc.net/problem/1859'