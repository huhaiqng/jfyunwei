# Generated by Django 3.2 on 2021-04-15 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0014_alter_userinfo_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='department',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='position',
        ),
    ]
