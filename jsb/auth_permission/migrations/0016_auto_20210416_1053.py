# Generated by Django 3.2 on 2021-04-16 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0015_auto_20210415_1417'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
