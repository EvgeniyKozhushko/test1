# Generated by Django 3.2.3 on 2021-07-08 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customer_user_group'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
