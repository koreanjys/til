from django.db import models

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    def __str__(self):
        return f'#{self.pk}: {self.title}'
        

class Student(models.Model):
    name = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    lectures = models.ManyToManyField(
        Lecture,                      # m:n 관계의 상대 모델
        related_name='students',      # 상대 모델(Lecture)이 나(Student)를 부를 때 이름
        through='school.Enrollment',  # 커스텀 중개모델 이름(str)
        through_fields=('student', 'lecture')  # M:N을 맺는 FK들 명시
    )
    def __str__(self):
        return f'#{self.pk}: {self.name}'


# Join Table에 추가 데이터가 있다면, 클래스 생성
class Enrollment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    semester = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.student} => {self.lecture}'