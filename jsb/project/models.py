from django.db import models
from django.utils import timezone


# 主机
class Host(models.Model):
    OS_CHOICES = [('CentOS 7', 'CentOS 7'), ('Windows Server 2012', 'Windows Server 20212')]
    CUP_CHOICES = [(4, 4), (8, 8), (16, 16), (32, 32)]
    MEMORY_CHOICES = [('4G', '4G'), ('8G', '8G'), ('16G', '16G'), ('32G', '32G')]
    DISK_CHOICES = [('4G', '40G'), ('100G', '100G'), ('200G', '200G')]
    CLOUD_CHOICE = [('阿里云', '阿里云'), ('华为云', '华为云')]
    CLOUD_USER_CHOICE = [('gainhon666', 'gainhon666'), ('lingfannao', 'lingfannao'),
                         ('胡振春221240096', '胡振春221240096'), ('水贝珠宝商业运营管理', '水贝珠宝商业运营管理'),
                         ('zhangtian2018', 'zhangtian2018')]
    ENV_CHOICES = [('测试环境', '测试环境'), ('测试环境A', '测试环境A'), ('测试环境B', '测试环境B'),
                   ('生产环境', '生产环境')]

    name = models.CharField('显示名称', max_length=200)
    hostname = models.CharField('主机名', max_length=200, blank=True)
    inside_ip = models.GenericIPAddressField('内网 IP')
    outside_ip = models.GenericIPAddressField('外网 IP', default='0.0.0.0')
    inside_port = models.IntegerField('内网端口号', default=22)
    outside_port = models.IntegerField('外网端口号', default=52113)
    os = models.CharField('系统', max_length=200, choices=OS_CHOICES)
    cpu = models.IntegerField('CPU 核数', default=4, choices=CUP_CHOICES)
    memory = models.CharField('内存大小', max_length=10, default='8G', choices=MEMORY_CHOICES)
    disk = models.CharField('硬盘大小', max_length=10, default='80G', choices=DISK_CHOICES)
    cloud = models.CharField('云平台', max_length=200, choices=CLOUD_CHOICE)
    cloud_user = models.CharField('云账号', max_length=200, choices=CLOUD_USER_CHOICE)
    env = models.CharField('环境', max_length=200, default='test', choices=ENV_CHOICES)
    user = models.CharField('用户', max_length=200, default='root')
    password = models.CharField('密码', max_length=200, default='123456')
    created = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        ordering = ['env', 'inside_ip']
        unique_together = ['inside_ip', 'cloud_user']
        verbose_name = '主机'
        verbose_name_plural = '主机'

    def __str__(self):
        return self.name


# MySQL 实例
class MySQLInstance(models.Model):
    inside_addr = models.CharField('内网地址', max_length=200, unique=True)
    outside_addr = models.CharField('外网地址', max_length=200, blank=True)
    role = models.CharField('角色', max_length=200)
    data_dir = models.CharField('数据库路径', max_length=200, blank=True)
    version = models.CharField('版本号', max_length=200)
    manager = models.CharField('管理员', max_length=200)
    password = models.CharField('密码', max_length=200)
    method = models.CharField('部署方式', max_length=200, default='normal')
    origin = models.CharField('来源', max_length=200, default='自建')
    cluster = models.CharField('集群', max_length=200, blank=True)
    created = models.DateTimeField('创建时间', default=timezone.now)
