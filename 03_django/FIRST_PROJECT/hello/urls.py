from django.urls import path, include
from . import views
urlpatterns = [
    path('world/', views.hello_world), 
]
