from django.db import models
from .host import Host


# 项目
class Project(models.Model):
    name = models.CharField('名称', max_length=200, unique=True)
    hosts = models.ManyToManyField(Host, verbose_name='主机', blank=True, related_name='project')
    deploy_dir = models.CharField('部署路径', max_length=200, blank=True)
    log_dir = models.CharField('日志路径', max_length=200, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name
