from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('board', views.board, name='board'),
]
