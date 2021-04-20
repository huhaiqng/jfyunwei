# Generated by Django 3.2 on 2021-04-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20210420_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='disk',
            field=models.CharField(choices=[('4G', '40G'), ('100G', '100G'), ('200G', '200G')], default='80G', max_length=10, verbose_name='硬盘大小'),
        ),
        migrations.AlterField(
            model_name='host',
            name='inside_ip',
            field=models.GenericIPAddressField(unique=True, verbose_name='内网 IP'),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=200, verbose_name='显示名称'),
        ),
    ]
