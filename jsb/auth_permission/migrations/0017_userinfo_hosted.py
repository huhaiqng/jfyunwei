# Generated by Django 3.2 on 2021-07-12 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0016_auto_20210416_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='hosted',
            field=models.BooleanField(default=False, verbose_name='主持早会'),
        ),
    ]
