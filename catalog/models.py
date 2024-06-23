from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='описание', **NULLABLE)
    price = models.FloatField(verbose_name='цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата заполнения')
    update_at = models.DateTimeField(default=timezone.now, verbose_name='Дата изменения')
    manufactured_at = models.DateTimeField(default=timezone.now, verbose_name='Дата производства продукта')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}{self.price}'
