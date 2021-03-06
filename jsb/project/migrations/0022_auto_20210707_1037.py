# Generated by Django 3.2 on 2021-07-07 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0021_alter_config_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='url',
            options={'ordering': ['project', 'env', 'name'], 'verbose_name': '地址大全', 'verbose_name_plural': '地址大全'},
        ),
        migrations.AlterField(
            model_name='env',
            name='name',
            field=models.CharField(max_length=200, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='project',
            name='hosts',
            field=models.ManyToManyField(blank=True, related_name='project', to='project.Host', verbose_name='主机'),
        ),
    ]
