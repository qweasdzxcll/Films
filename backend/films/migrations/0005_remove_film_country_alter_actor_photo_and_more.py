# Generated by Django 5.1.6 on 2025-02-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_alter_film_preview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='country',
        ),
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.ImageField(upload_to='photo/%Y/%n/%d'),
        ),
        migrations.RemoveField(
            model_name='film',
            name='actor',
        ),
        migrations.AddField(
            model_name='film',
            name='actor',
            field=models.ManyToManyField(to='films.actor'),
        ),
    ]
