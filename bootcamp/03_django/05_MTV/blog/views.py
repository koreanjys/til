# blog/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# 글 목록 화면 (Read)
def index(request):
    # 글 목록 조회
    # db > article > 모든 레코드 조회
    articles = Article.objects.all()  # QuerySet(List)
    context = { 'articles': articles, }
    return render(request, 'blog/index.html', context)


# 글 상세 화면 (Read)
def detail(request, article_pk):
    # db > articles > 특정 레코드 조회    
    article = get_object_or_404(Article, pk=article_pk)
    context = { 'article': article, }
    return render(request, 'blog/detail.html', context)


# 글 쓰기 화면 or 저장 or 반려
def create(request):
    # 만약 POST 방식으로 요청이 왔다면
    if request.method == 'POST':
        # 박스에 넣고
        article_form = ArticleForm(request.POST)
        # 검사하고
        if article_form.is_valid():
            # 괜춘하니 save => redirect
            article = article_form.save()
            return redirect('blog:detail', article.pk)
    
    # 만약 GET 방식으로 요청이 왔다면       
    elif request.method == 'GET':
        # 빈 박스를
        article_form = ArticleForm()

    # 1. POST 방식인데 안괜찮으면, 반려당한 article_form
    # 2. GET 방식이면 빈 article_form
    context = {'article_form': article_form, }
    return render(request, 'blog/form_new.html', context)



# 글 수정 화면
def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = { 'article': article, }
    return render(request, 'blog/edit.html', context)

# 글 DB에 실제 수정
def update(request, article_pk):
    # 기존의 article 객체 조회(레코드 검색)
    article = get_object_or_404(Article, pk=article_pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    # 저장하고 detail 로 redirect 하자!
    return redirect('blog:detail', article.pk)



# 글 삭제 ?? (Delete)
def delete(request, article_pk):
    if request.method == 'POST':
        # 1. 고른다.
        article = get_object_or_404(Article, pk=article_pk)
        # 2. 지운다.
        article.delete()
    return redirect('blog:index')
