from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import ContentType


# 部门
class Department(models.Model):
    name = models.CharField(max_length=11, unique=True)

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门'

    def __str__(self):
        return self.name


# 职位
class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = '职位'

    def __str__(self):
        return self.name


# 用户
class UserInfo(AbstractUser):
    phone = models.CharField('手机号码', max_length=11, unique=True)
    department = models.ForeignKey(Department, verbose_name="部门", on_delete=models.PROTECT)
    position = models.ForeignKey(Position, verbose_name='职位', on_delete=models.PROTECT)

    def __str__(self):
        return self.username


# 一级菜单
class L1Menu(models.Model):
    name = models.CharField('名称', max_length=255, unique=True)
    title = models.CharField('显示名称', max_length=255)
    path = models.CharField('URI', max_length=255, unique=True, help_text='需要 /，例如: /resource')
    redirect = models.CharField('定向', max_length=255, help_text='访问一级菜单跳转到子节点 URI，例如: /resource/host')
    icon = models.CharField('菜单图标', max_length=255, default='tree')
    order = models.IntegerField('排序', default=10, help_text='菜单排序，小的排前面')

    class Meta:
        verbose_name = '一级菜单'
        verbose_name_plural = '一级菜单'
        ordering = ['order']

    def __str__(self):
        return self.title


# 二级菜单
class L2Menu(models.Model):
    parent = models.ForeignKey(L1Menu, on_delete=models.PROTECT, verbose_name='父菜单', related_name='children')
    title = models.CharField('显示名称', max_length=255)
    name = models.ForeignKey(
        ContentType, verbose_name='模型',
        on_delete=models.PROTECT,
        limit_choices_to={'app_label__in': ['report']},
        blank=True, null=True,
        help_text='绑定模型'
    )
    path = models.CharField('URI', max_length=255, help_text='不需要 /，例如: user')
    component = models.CharField('部件', max_length=255, help_text='相对于 /views 的路径, 例如: /resource/host')
    order = models.IntegerField('排序', default=10, help_text='菜单排序，小的排前面')
    is_model = models.BooleanField('是否对应模型', default=True)

    class Meta:
        verbose_name = '二级菜单'
        verbose_name_plural = '二级菜单'
        ordering = ['order']

    def __str__(self):
        return self.title
