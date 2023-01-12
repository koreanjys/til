from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    content = models.CharField(max_length=200)
    # foreign key 쓰면 필드명에 _id 붙이지 않기.
    # migrate 하면 자동으로 뒤에 _id 붙음.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)