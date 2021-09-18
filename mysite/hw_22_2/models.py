from django.db import models


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    master = models.CharField(max_length=255, verbose_name='Хозяин')
    age = models.CharField(max_length=255, verbose_name='Возраст')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')
