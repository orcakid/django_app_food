from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', unique=True)
    password = models.CharField(verbose_name="password", max_length=150)
    first_name = models.CharField(verbose_name='first name', max_length=150)
    last_name = models.CharField(verbose_name='last name', max_length=150)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    def __str__(self):
        return self.username