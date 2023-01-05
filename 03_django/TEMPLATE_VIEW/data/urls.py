# data/urls.py

from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    # data/
    path('', views.index, name='index'),

    # data/hello/<name>/ => Variable Routing
    # <name> 이라는 고정된 입력. hello/ 뒤에 뭐가 와도 받겠다는 뜻.
    path('hello/<name>', views.hello, name='hello'),
    # hello/neo/ => 안녕 neo,
    # hello/andy/ => 안녕 andy,



    # data/user_input/
    path('user_input/', views.user_input, name='user_input'),

    # data/user_output/
    path('user_output/', views.user_output, name='user_output'),
]
