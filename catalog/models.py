from django.db import models
from django.utils import timezone
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    price = models.FloatField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    update_at = models.DateTimeField(default=timezone.now, verbose_name='Дата последнего изменения')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Создан пользователем", **NULLABLE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}{self.price}'


class Version(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукт', related_name='version')
    number_version = models.IntegerField(default=1, verbose_name='Номер версии')
    name_version = models.CharField(max_length=250, verbose_name='Имя версии')
    version_flag = models.BooleanField(default=False, verbose_name='Признак версии')

    class Meta:
        verbose_name = 'Весрия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.name_version}'
