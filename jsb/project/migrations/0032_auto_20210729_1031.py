# Generated by Django 3.2 on 2021-07-29 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_auto_20210708_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='host',
            options={'ordering': ['cloud_user', 'hostname', 'env', 'inside_ip'], 'verbose_name': '主机', 'verbose_name_plural': '主机'},
        ),
        migrations.AddField(
            model_name='project',
            name='used',
            field=models.BooleanField(default=True, verbose_name='使用中'),
        ),
    ]
