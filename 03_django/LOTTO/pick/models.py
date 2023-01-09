from django.db import models

# Create your models here.


class pick(models.Model):
    author = models.CharField(max_length=50)
    nums = models.CharField(max_length=50)
    pick_date = models.DateField(auto_now_add=True)