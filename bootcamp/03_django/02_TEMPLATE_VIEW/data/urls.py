# data/urls.py
from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    # data/
    path('', views.index, name='index'),
    
    # data/hello/<name>/ => Variable Routing
    path('hello/<str:name>/', views.hello, name='hello'),

    # data/user_input/
    path('user_input/', views.user_input, name='user_input'),    
    # data/user_output/
    path('user_output/', views.user_output, name='user_output'),
]
