# Generated by Django 2.2.11 on 2021-02-24 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth_permission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='L1Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
                ('title', models.CharField(max_length=255, verbose_name='显示名称')),
                ('path', models.CharField(help_text='需要 /，例如: /resource', max_length=255, unique=True, verbose_name='URI')),
                ('redirect', models.CharField(help_text='访问一级菜单跳转到子节点 URI，例如: /resource/host', max_length=255, verbose_name='定向')),
                ('icon', models.CharField(default='tree', max_length=255, verbose_name='菜单图标')),
                ('order', models.IntegerField(default=10, help_text='菜单排序，小的排前面', verbose_name='排序')),
            ],
            options={
                'verbose_name': '一级菜单',
                'verbose_name_plural': '一级菜单',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='L2Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='显示名称')),
                ('path', models.CharField(help_text='不需要 /，例如: user', max_length=255, unique=True, verbose_name='URI')),
                ('component', models.CharField(help_text='相对于 /views 的路径, 例如: /resource/host', max_length=255, verbose_name='部件')),
                ('order', models.IntegerField(default=10, help_text='菜单排序，小的排前面', verbose_name='排序')),
                ('is_model', models.BooleanField(default=True, verbose_name='是否对应模型')),
                ('name', models.ForeignKey(blank=True, help_text='绑定模型', limit_choices_to={'app_label': 'app'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType', verbose_name='模型')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='auth_permission.L1Menu', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '二级菜单',
                'verbose_name_plural': '二级菜单',
                'ordering': ['order'],
            },
        ),
    ]
