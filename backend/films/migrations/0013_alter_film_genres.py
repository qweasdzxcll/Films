# Generated by Django 5.1.6 on 2025-02-09 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0012_film_genres_alter_category_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='genres',
            field=models.CharField(choices=[('Мультфильм', 'Мультфильм'), ('Фильм', 'Фильм'), ('Сериал', 'Сериал'), ('Мультсериал', 'Мультсериал'), ('Аниме', 'Аниме')], max_length=128, verbose_name='Жанр'),
        ),
    ]
