from django.db import models


# Create your models here.
class Guitar(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Марка')
    year = models.CharField(max_length=255, verbose_name='Год выпуска')
    price = models.FloatField(verbose_name='Цена')
    amount = models.CharField(max_length=255, verbose_name='Количество')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')
