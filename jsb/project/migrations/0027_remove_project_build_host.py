# Generated by Django 3.2 on 2021-07-07 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0026_project_build_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='build_host',
        ),
    ]
