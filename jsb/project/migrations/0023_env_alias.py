# Generated by Django 3.2 on 2021-07-07 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_auto_20210707_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='env',
            name='alias',
            field=models.CharField(blank=True, max_length=200, verbose_name='简称'),
        ),
    ]
