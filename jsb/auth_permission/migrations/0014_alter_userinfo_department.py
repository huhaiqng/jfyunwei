# Generated by Django 3.2 on 2021-04-15 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_permission', '0013_alter_userinfo_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth_permission.department', verbose_name='部门'),
        ),
    ]
