# Generated by Django 2.2.11 on 2021-02-24 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0004_auto_20210224_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='auth_permission.Department', verbose_name='部门'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='auth_permission.Position', verbose_name='职位'),
        ),
    ]
