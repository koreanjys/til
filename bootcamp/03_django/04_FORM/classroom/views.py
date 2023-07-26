from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from .models import Student
from .forms import StudentForm

'''
    GET    /classroom/create/  => 작성할 HTML
    POST   /classroom/create/  => 데이터 받아서 저장
''' 
# 아래 view 함수는 ~~ HTTP method 만 받겠다!
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # 데이터 받아서 저장
        form = StudentForm(request.POST)
        if form.is_valid():  # form 은 is_valid 실패하면, HTML에 에러메세지가 들어감
            student = form.save()
            return redirect('classroom:detail', student.pk)
    elif request.method == 'GET':
        # HTML 던져 주기
        form = StudentForm()

    context = {'form': form, }
    return render(request, 'classroom/form.html', context)


# DB에 영향이 있다(CUD) => danger  => POST
# DB에 영향이 없으면(R) => safe    => GET

@require_safe
def index(request):
    students = Student.objects.order_by('-gpa')
    context = {'students': students,}
    return render(request, 'classroom/index.html', context)


@require_safe
def detail(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    context = {'student': student, }
    return render(request, 'classroom/detail.html', context)


@require_http_methods(['GET', 'POST'])
def update(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('classroom:detail', student.pk)
    else:  # GET 방식일 때,
        form = StudentForm(instance=student)
    
    context = { 'form': form, }
    return render(request, 'classroom/form.html', context)




@require_POST
def delete(request, student_pk):
    student = get_object_or_404(Student, pk=student_pk)
    student.delete()
    return redirect('classroom:index')