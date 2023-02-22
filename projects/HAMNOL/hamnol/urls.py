from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from accounts.views import signup

urlpatterns = [

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('signup/', signup, name='signup'),

]
