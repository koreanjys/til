from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('new/', views.new, name='new'),
    # blog/create/
    path('create/', views.create, name='create'),

    
    #blog/
    path('', views.index, name='index'),
    # blog/1/
    path('<int:article_pk>/', views.detail, name='detail'),
    # 여기서 pk 는 id 와 비슷한 값이고, 고유 값을 의미
    # 만약 정수로 쓸거면 <int:article_pk> 로 적으면 된다.

    # blog/1/edit/
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    # blog/1/update/
    path('<int:article_pk>/update/', views.update, name='update'),

    # blog/1/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]
