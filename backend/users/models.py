from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=18,
        unique=True
    )

    is_status = models.PositiveSmallIntegerField(
        verbose_name='Статус',
        default=0,
        choices=(
            (0, 'Пользователь'),
            (1, 'Администратор')
        )
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.phone
            super().save(*args, **kwargs)