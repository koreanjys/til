from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.decorators.http import (require_http_methods,
                                            require_safe, require_POST)

from django.contrib.auth.decorators import login_required

from .models import Question, Reply
from .forms import QuestionForm, ReplyForm


@login_required
@require_http_methods(['GET', 'POST'])
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            # 이 question 객체의 user 항목은(작성자는) 요청을 보낸 사용자다.
            question.user = request.user
            question.save()
            return redirect('polls:question_detail', question.pk)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'polls/question_form.html', context)


@require_safe
def question_index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/question_index.html', context)


@require_safe
def question_detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    form = ReplyForm()
    
    # N개의 reply들이 모두 request.user가 vote 했는지 여부
    
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'polls/question_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    # 요청 보낸 사용자가 질문 작성자가 아니라면,
    if request.user != question.user:
        return HttpResponseForbidden('권한이 없습니다.')

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return redirect('polls:question_detail', question.pk)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, }
    return render(request, 'polls/question_form.html', context)


@login_required
@require_POST
def delete_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    # 요청 보낸 사용자가 질문 작성자가 아니라면,
    if request.user != question.user:
        return HttpResponseForbidden('권한이 없습니다.')
    question.delete()
    return redirect('polls:question_index')


@login_required
@require_POST
def create_reply(request, question_pk):  # 댓글 저장만 담당
    question = get_object_or_404(Question, pk=question_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.question = question
        reply.user = request.user
        reply.save()
    return redirect('polls:question_detail', question.pk)


@login_required
@require_POST
def vote_reply(request, question_pk, reply_pk):  #/polls/1/replies/2/vote/
    question = get_object_or_404(Question, pk=question_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    user = request.user
    
    # 답변 작성자는 투표 못함
    if request.user == reply.user:
        return HttpResponseForbidden('자추는 금지')

    # is_voted = reply.vote_users.filter(pk=user.pk).exists()
    
    if reply.is_voted(user):
        reply.vote_users.remove(user)
    else:
        reply.vote_users.add(user)
            
    return redirect('polls:question_detail', question.pk)


@login_required
@require_POST
def delete_reply(request, question_pk, reply_pk):
    question = get_object_or_404(Question, pk=question_pk)
    reply = get_object_or_404(Reply, pk=reply_pk)
    # 댓글 작성자와 삭제버튼 누른사람이 같을 때만 삭제
    if reply.user != request.user:
        return HttpResponseForbidden('권한이 없습니다.')
        
    reply.delete()
    return redirect('polls:question_detail', question.pk)