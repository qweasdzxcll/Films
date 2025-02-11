from django.db import models
from users.models import User

class Actor(models.Model):
    firstname = models.CharField(
        max_length=128
    )

    lastname = models.CharField(
        max_length=128
    )

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Film(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=128
    )

    preview = models.ImageField(
        verbose_name='Превью',
        upload_to='preview/%Y/%m/%d'
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )

    date = models.DateField(
        verbose_name='Дата выпуска',
        auto_now_add=True
    )

    actors = models.ManyToManyField(
        Actor,
        verbose_name='Актеры',
        related_name='actors'
    )

    genres = models.CharField(
        verbose_name='Жанр',
        max_length=128,
        choices=(
            ('Мультфильм', 'Мультфильм'),
            ('Фильм', 'Фильм'),
            ('Сериал', 'Сериал'),
            ('Мультсериал', 'Мультсериал'),
            ('Аниме', 'Аниме')
        )
    )

    rating = models.DecimalField(
        verbose_name='Рейтинг',
        max_digits=2,
        decimal_places=0
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )
    message = models.TextField(
        verbose_name='Сообщение',
        blank=True,
        null=True
    )
    film = models.ForeignKey(
        Film,
        verbose_name='Фильм',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.film