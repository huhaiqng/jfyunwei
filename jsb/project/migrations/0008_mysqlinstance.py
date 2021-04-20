# Generated by Django 3.2 on 2021-04-20 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20210420_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySQLInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inside_addr', models.CharField(max_length=200, verbose_name='内网地址')),
                ('outside_addr', models.CharField(blank=True, max_length=200, verbose_name='外网地址')),
                ('role', models.CharField(max_length=200, verbose_name='角色')),
                ('data_dir', models.CharField(blank=True, max_length=200, verbose_name='数据库路径')),
                ('version', models.CharField(max_length=200, verbose_name='版本号')),
                ('manager', models.CharField(max_length=200, verbose_name='管理员')),
                ('password', models.CharField(max_length=200, verbose_name='密码')),
                ('method', models.CharField(default='normal', max_length=200, verbose_name='部署方式')),
                ('origin', models.CharField(default='自建', max_length=200, verbose_name='来源')),
                ('cluster', models.CharField(blank=True, max_length=200, verbose_name='集群')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
    ]
