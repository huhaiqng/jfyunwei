# Generated by Django 3.2 on 2021-07-07 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0024_project_deploy_obj'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='alias',
            field=models.CharField(blank=True, max_length=200, verbose_name='简称'),
        ),
    ]
