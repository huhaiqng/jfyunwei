# Generated by Django 3.2 on 2021-04-20 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210323_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='password',
            field=models.CharField(default='123456', max_length=200, verbose_name='密码'),
        ),
        migrations.AddField(
            model_name='host',
            name='user',
            field=models.CharField(default='root', max_length=200, verbose_name='用户'),
        ),
    ]
