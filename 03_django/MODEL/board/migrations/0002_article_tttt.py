# Generated by Django 3.2.16 on 2023-01-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tttt',
            field=models.IntegerField(default=0),
        ),
    ]
