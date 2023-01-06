from django.db import models

# Create your models here.
# 만든 class 에 models.Model 을 상속 받아야 함
class Article(models.Model):
    # id 는 자동으로 만들어 짐
    # CharField(길이제한 숫자) => 짧은 str
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    # TextField => 긴 str
    content = models.TextField()

# 1. models.py 작성 및 수정
# 2. python manage.py makemigrations <app_name>
# 3. python manage.py migrate board

