# Generated by Django 5.1.6 on 2025-02-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_alter_film_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='preview',
            field=models.ImageField(upload_to='preview/%Y/%n/%d'),
        ),
    ]
