# accounts/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomUserCreationForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    # login 한 사용자라면,
    if request.user.is_authenticated:
        return HttpResponseBadRequest('이미 로그인 하였습니다.')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('polls:question_index')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form, }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    # login 한 사용자라면,
    if request.user.is_authenticated:
        return HttpResponseBadRequest('이미 로그인 하였습니다.')

    if request.method == 'POST':
        # 수많은 form 중에 얘만 1번 인자 request
        form = AuthenticationForm(request, request.POST)
        # 사용자가 입력한 username / password 가 맞다면,
        if form.is_valid():
            # AuthenticationForm => User create 가 아님. 다른 메서들 제공
            user = form.get_user()
            # 로그인 시키기(쿠키 세팅)
            auth_login(request, user)
            return redirect('polls:question_index')
    else:
        form = AuthenticationForm()
    context = {'form': form, }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('polls:question_index')