from django.shortcuts import render, redirect
from .models import Article

# 글 목록 화면 (Read)
def index(request):
    
    # 글 목록 조회
    # db article 관련된 모든 레코드 전체를 조회
    articles = Article.objects.all()  # QuerySet(List)
    context = {
        'articles': articles,
    }
    return render(request, 'blog/index.html', context)


# 글 상세 화면 (Read)
def detail(request, article_pk):  # urls.py 에 <article_pk> 라고 적어서 이렇게 매개변수 두번째 값으로 받음
    # db > articles > 특정 레코드 조회
    pk = request.GET.get('no')
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'blog/detail.html', context)

'''
RESTful 하게 URL 짜는법

1. Resource 를 표현
2. 명사형
3. 확실히 구분
4. (동사는 빼라)
'''
# 글 쓰기 화면 (Create)
def new(request):

    return render(request, 'blog/new.html')


# 글 실제 저장
def create(request):
    # 새로운 article 객체 생성(레코드 추가)
    article = Article()
    article.title =  request.POST['new_title']
    article.content = request.POST['new_content']
    article.save()
    # /blog/ 로 재요청을 시킴
    return redirect('blog:detail', article.pk)
    # return redirect('blog/{article.pk}/')


# 글 수정 화면 (Update)
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {'article': article,}
    return render(request, 'blog/edit.html', context)


# 글 DB에 실제 수정
def update(request, article_pk):
    # 기존의 article 객체 조회(레코드 검색)
    article = Article.objects.get(pk=article_pk)
    article.title =  request.POST['edit_title']
    article.content = request.POST['edit_content']
    article.save()
    # /blog/ 로 재요청을 시킴
    return redirect('blog:detail', article.pk)
    # return redirect('blog/{article.pk}/')


# 글 삭제 ?? (Delete)
def delete(request, article_pk):
    if request.method == 'POST':
        # 특정 게시글을 지운다.
        # 1. 고른다.
        article = Article.objects.get(pk=article_pk)
        # 2. 지운다.
        article.delete()
    return redirect('blog:index')


# 번외: GET 과 POST 구분은 DB에 영향을 주면 POST, 그 외엔 GET