# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # blog/create/
    path('create/', views.create, name='create'),

    # blog/
    path('', views.index, name='index'),
    # blog/1/
    path('<int:article_pk>/', views.detail, name='detail'),
    
    # blog/1/edit/
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    # blog/1/update/
    path('<int:article_pk>/update/', views.update, name='update'),

    # blog/1/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]

'''
URL
1. Resource 를 표현
2. 명사형
3. 확실히 구분
4. (동사는 빼라)

'''
