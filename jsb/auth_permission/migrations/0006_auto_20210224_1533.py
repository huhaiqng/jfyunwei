# Generated by Django 2.2.11 on 2021-02-24 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0005_auto_20210224_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth_permission.Department', verbose_name='部门'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth_permission.Position', verbose_name='职位'),
            preserve_default=False,
        ),
    ]
