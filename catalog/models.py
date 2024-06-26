from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name')
    description = models.TextField(verbose_name='description', **NULLABLE)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name')
    description = models.TextField(verbose_name='description', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='description', **NULLABLE)
    price = models.FloatField(verbose_name='price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Date of creation')
    update_at = models.DateTimeField(default=timezone.now, verbose_name='Date of Update')
    #manufactured_at = models.DateTimeField(default=timezone.now, verbose_name='Дата производства продукта')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name}{self.price}'
