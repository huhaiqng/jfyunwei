# Generated by Django 3.2 on 2021-05-06 06:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_host_cloud_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
    ]