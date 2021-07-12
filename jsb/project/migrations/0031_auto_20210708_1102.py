# Generated by Django 3.2 on 2021-07-08 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0030_buildhost_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.CharField(default='www', max_length=200, verbose_name='管理用户'),
        ),
        migrations.AlterField(
            model_name='buildhost',
            name='user',
            field=models.CharField(default='www', max_length=200, verbose_name='打包用户'),
        ),
    ]