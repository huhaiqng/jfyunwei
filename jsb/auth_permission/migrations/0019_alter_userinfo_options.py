# Generated by Django 3.2 on 2021-07-29 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0018_userinfo_hosted_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]
