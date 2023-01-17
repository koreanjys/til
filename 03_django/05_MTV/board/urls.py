from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    ## C
    # board/new/
    path('new/', views.new_posting, name='new_posting'),
    # board/create/
    path('create/', views.create_posting, name='create_posting'),
    
    ## R
    # board/
    path('', views.posting_list, name='posting_list'),
    # board/1/
    path('<int:posting_pk>/', views.posting_detail, name='posting_detail'),

    ## U
    # board/1/edit/
    path('<int:posting_pk>/edit/', views.edit_posting, name='edit_posting'), 
    # board/1/update/
    path('<int:posting_pk>/update/', views.update_posting, name='update_posting'),

    ## D
    # board/1/delete/
    path('<int:posting_pk>/delete/', views.delete_posting, name='delete_posting'),
]
