# Generated by Django 3.2.3 on 2021-06-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0011_auto_20210609_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(max_length=100, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='binding',
            field=models.CharField(max_length=100, verbose_name='Переплет'),
        ),
        migrations.AlterField(
            model_name='book',
            name='size',
            field=models.CharField(max_length=100, verbose_name='Формат'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title_book',
            field=models.CharField(max_length=200, verbose_name='Название книги'),
        ),
    ]
