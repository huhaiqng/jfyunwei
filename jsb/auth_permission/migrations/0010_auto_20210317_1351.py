# Generated by Django 2.2.11 on 2021-03-17 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0009_auto_20210317_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='l2menu',
            name='path',
            field=models.CharField(help_text='不需要 /，例如: user', max_length=255, verbose_name='URI'),
        ),
    ]