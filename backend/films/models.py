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
        upload_to='preview/%Y/%m/%d',
        null=True,
        blank=True
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

    genre = models.IntegerField(
        verbose_name='Жанр',
        choices=(
            (1, 'Мультфильм'),
            (2, 'Фильм'),
            (3, 'Сериал'),
            (4, 'Мультсериал'),
            (5, 'Аниме')
        )
    )

    average_rating = models.FloatField(
        verbose_name='Рейтинг',
        default=0.0
    )

    def update_average_rating(self):
        ratings = self.rating_set.all()
        if ratings.exists():
            self.average_rating = sum(rating.rating for rating in ratings) / ratings.count()
        else:
            self.average_rating = 0.0
        self.save()

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
    
class Rating(models.Model):
    film = models.ForeignKey(
        Film,
        verbose_name='Фильм',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    rating = models.IntegerField(
        verbose_name='Рейтинг',
        choices=(
            [(i ,i) for i in range(11)]
        )
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.film:
            self.film.update_average_rating()