# hello / urls.py

from django.urls import path
from . import views

urlpatterns = [
    # FULL URL
    # hello/world/ => views.py / hello_world
    path('world/', views.hello_world),
    # hello/lunch/ => views.lunch
    path('lunch/', views.lunch),
    # hello/lotto/ => views.lotto
    path('lotto/', views.lotto),
]