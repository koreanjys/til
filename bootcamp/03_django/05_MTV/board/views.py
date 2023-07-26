from django.shortcuts import render, redirect
from .models import Posting


def new_posting(request):
    return render(request, 'board/new_posting.html')


def create_posting(request):
    posting = Posting()
    posting.subject = request.POST['subject']
    posting.description = request.POST['description']
    posting.save()
    return redirect('board:posting_detail', posting.pk)


def posting_list(request):
    # 기본 => id 오름차순
    # postings = Posting.objects.all()
    # id 내림차순 (python)
    # postings = Posting.objects.all()[::-1]
    
    # id(pk) 내림차순 (DB)
    postings = Posting.objects.order_by('-pk')
    context = {'postings': postings}
    return render(request, 'board/posting_list.html', context)


def posting_detail(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context = {'posting': posting}
    return render(request, 'board/posting_detail.html', context)


def edit_posting(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context = {'posting': posting,}
    return render(request, 'board/edit_posting.html', context)


def update_posting(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    posting.subject = request.POST['subject']
    posting.description = request.POST['description']
    posting.save()
    return redirect('board:posting_detail', posting.pk)



def delete_posting(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    posting.delete()
    return redirect('board:posting_list')