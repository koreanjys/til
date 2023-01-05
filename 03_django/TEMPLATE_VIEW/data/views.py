from django.shortcuts import render

# Create your views here.

# data/views.py

def index(request):
    
    # render 불러올때 모든 templates 폴더 안에서 불러오기 때문에
    # 각 앱들의 templates 폴더 안에 새로운 폴더를 만들어서 넣어줘야
    # 구분이 된다.
    return render(request, 'data/index.html')


def hello(request, name):  # name 매개변수가 온 이유는 urls.py에 path('hello/<name>)'을 지정 해 줬기 때문이다.
    
    # context 딕셔너리 만들어주고, 그 안에 매개변수로 받은 name을 만들어준다. 그렇게 하면 /hello/asdfadf 이렇게 hello/ 뒤에 뭐가 와도 그 값을 .html 파일에서 {{name}} 으로 감싸주면 반환한다.
    context = {
        'name': name,
    }
    return render(request, 'data/hello.html', context)


def user_input(request):
    
    return render(request, 'data/user_input.html')


def user_output(request):
    c = int(request.POST['cel'])
    f = c * 1.8 + 32

    context = {
        'f': f,
        'username': request.POST['username'],
        'password': request.POST['password'],
    }
    return render(request, 'data/user_output.html', context)