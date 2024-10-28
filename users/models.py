from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите номер телефона"
    )
    avatar = models.ImageField(
        upload_to="users/",
        **NULLABLE,
        verbose_name="Аватар",
        help_text="Загрузите фото профиля"
    )
    country = models.CharField(
        verbose_name="Страна", **NULLABLE, help_text="Введите страну"
    )
    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
