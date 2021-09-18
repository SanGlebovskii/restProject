from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    quantity = models.CharField(max_length=255, verbose_name='Количество')
    comment = models.CharField(max_length=255, verbose_name='Комментарий')
