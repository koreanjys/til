# Master urls.py
from django.contrib import admin
from django.urls import path, include

def to_main(request):
    from django.shortcuts import redirect
    return redirect('polls:question_index')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('polls/', include('polls.urls')),
    path('', to_main),
]
