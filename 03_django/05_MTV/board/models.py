from django.db import models


class Posting(models.Model):
    subject = models.CharField(max_length=200)
    description = models.TextField()