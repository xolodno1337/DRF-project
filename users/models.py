from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Укажите почту')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', help_text='Укажите номер телефона',
                                    **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='Город', help_text='Укажите город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Изображение', help_text='Загрузите аватар',
                               **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
