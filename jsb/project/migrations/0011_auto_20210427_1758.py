# Generated by Django 3.2 on 2021-04-27 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_account'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='account',
            old_name='use',
            new_name='name',
        ),
    ]
