# Generated by Django 3.2 on 2021-04-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0010_auto_20210317_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
