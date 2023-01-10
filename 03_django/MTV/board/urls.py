from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:posting_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:posting_pk>/delete/', views.delete, name='delete'),
     # blog/1/edit/
    path('<int:posting_pk>/edit/', views.edit, name='edit'),
    # blog/1/update/
    path('<int:posting_pk>/update/', views.update, name='update'),
]
