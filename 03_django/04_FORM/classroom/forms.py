from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=10)
    major = forms.CharField(min_length=2, max_length=20)
    gpa = forms.FloatField(min_value=0.0, max_value=4.5)
    age = forms.IntegerField(min_value=10, max_value=100)

    class Meta:  # 이 클래스의 메타 데이터 저장용 
        model = Student
        # fields = ('name', 'major', 'gpa', 'age', )
        fields = '__all__'