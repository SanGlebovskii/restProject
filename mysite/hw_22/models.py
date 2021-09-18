from django.db import models


# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=255, verbose_name='Марка')
    model = models.CharField(max_length=255, verbose_name='Модель')
    year = models.CharField(max_length=255, verbose_name='Год выпуска')
    price = models.FloatField(verbose_name='Цена')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')
