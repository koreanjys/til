from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    # classroom/create/
    path('create/', views.create, name='create'),
    # classroom/
    path('', views.index, name='index'),
    # classroom/1/
    path('<int:student_pk>/', views.detail, name='detail'),
    # classroom/1/update/
    path('<int:student_pk>/update/', views.update, name='update'),
    # classroom/1/delete/
    path('<int:student_pk>/delete/', views.delete, name='delete'),
]
