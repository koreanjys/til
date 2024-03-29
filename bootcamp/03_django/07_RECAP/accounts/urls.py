# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # accounts/signup/
    path('signup/', views.signup, name='signup'),
    # accounts/login/
    path('login/', views.login, name='login'),
    # accounts/logout/
    path('logout/', views.logout, name='logout'),
    # accounts/neo/
    path('<username>/', views.profile, name='profile'),
    # accounts/neo/follow/
    path('<username>/follow/', views.follow, name='follow'),
]
