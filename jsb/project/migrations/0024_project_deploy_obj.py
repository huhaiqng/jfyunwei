# Generated by Django 3.2 on 2021-07-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0023_env_alias'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deploy_obj',
            field=models.CharField(blank=True, max_length=200, verbose_name='部署对象'),
        ),
    ]
