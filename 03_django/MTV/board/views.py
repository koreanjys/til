from django.shortcuts import render, redirect
from .models import Posting

# Create your views here.

def index(request):
    postings = Posting.objects.order_by('-pk')
    context = {
        'postings': postings
    }
    return render(request, 'board/index.html', context)

def new(request):
    return render(request, 'board/new.html')

def create(request):
    posting = Posting()
    posting.subject = request.POST['new_subject']
    posting.description = request.POST['new_description']
    posting.save()
    return redirect('board:detail', posting.pk)

def detail(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context = {
        'posting': posting,
    }
    return render(request, 'board/detail.html', context)

# 삭제
def delete(request, posting_pk):
    if request.method == 'POST':
        posting = Posting.objects.get(pk=posting_pk)
        posting.delete()
    return redirect('board:index')

# 수정
def edit(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context = { 'posting': posting, }
    return render(request, 'board/edit.html', context)

def update(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    posting.subject = request.POST['subject']
    posting.description = request.POST['description']
    posting.save()
    # 저장하고 detail 로 redirect 하자!
    return redirect('board:detail', posting.pk)