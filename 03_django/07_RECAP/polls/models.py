# polls/models.py
from django.db import models
from django.conf import settings

class Question(models.Model):
    title = models.CharField(max_length=200)
    # 알아서 db 컬럼은 user_id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Reply(models.Model):
    content = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    # db 컬럼은 user_id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # db 컬럼은 question_id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)