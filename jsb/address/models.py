from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from auth_permission.models import UserInfo
from project.models import Host


class Address(models.Model):
    # """
    # usual address
    # 常用地址存放表
    # """
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', max_length=20)
    url = models.CharField('地址', max_length=255)
    img = models.CharField('图片', max_length=255, null=True, help_text='例如: /images/abc.jpg')
    order = models.IntegerField('排序', default=100)

    class Meta:
        ordering = ['order']
        verbose_name = '首页地址'
        verbose_name_plural = '首页地址'

    def __str__(self):
        return self.name


# 项目
class Project(models.Model):
    name = models.CharField('名称', max_length=200, unique=True)
    hosts = models.ManyToManyField(Host, verbose_name='主机', blank=True)
    deploy_dir = models.CharField('部署路径', max_length=200, blank=True)
    log_dir = models.CharField('日志路径', max_length=200, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name


# 环境
class Env(models.Model):
    name = models.CharField('环境', max_length=200)

    class Meta:
        verbose_name = '环境'
        verbose_name_plural = '环境'

    def __str__(self):
        return self.name


# 地址
class ProjectUrl(models.Model):
    name = models.CharField('名称', max_length=200)
    project = models.ForeignKey(Project, verbose_name='项目', on_delete=models.PROTECT, related_name='urls')
    env = models.ForeignKey(Env, verbose_name='环境', on_delete=models.PROTECT)
    url = models.URLField('地址', max_length=200, unique=True)

    class Meta:
        ordering = ['project', 'name', 'env']
        verbose_name = '地址大全'
        verbose_name_plural = '地址大全'

    def __str__(self):
        return self.url

