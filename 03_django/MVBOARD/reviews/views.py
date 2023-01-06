from django.shortcuts import render
from reviews.models import Review

# Create your views here.

def main_page(request):
    context = {'main': '안녕!'}
    return render(request, 'reviews/main_page.html', context)


def board(request):
    res = request.POST
    review = Review()
    review.author = res['author']
    review.title = res['title']
    review.content = res['content']
    review.movie = res['movie']
    review.save()
    
    ## Create (생성)

    # 데이터베이스 작성하는 방법
    # 1.
    '''
    review = Review()
    review.title = '첫번째 글'
    review.content = '와 내가 처음이야'
    review.author = '신주용'
    review.save()
    '''

    context = {'board':'게시판!'}
    return render(request, 'reviews/board.html', context)