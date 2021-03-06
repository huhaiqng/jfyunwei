# Generated by Django 3.2 on 2021-04-27 09:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_mysqlinstance_inside_addr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=255, unique=True, verbose_name='名称')),
                ('username', models.CharField(max_length=200, verbose_name='用户名')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('addr', models.CharField(blank=True, max_length=200, null=True, verbose_name='地址')),
                ('remark', models.CharField(blank=True, max_length=255, verbose_name='备注')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'ordering': ['use'],
            },
        ),
    ]
