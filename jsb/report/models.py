from django.db import models
from django.utils import timezone
from auth_permission.models import UserInfo


# 日报
class Daily(models.Model):
    owner = models.ForeignKey(UserInfo, on_delete=models.PROTECT, verbose_name='用户')
    task = models.TextField('任务')
    rate = models.FloatField('进度')
    time = models.FloatField('耗时')
    created_at = models.DateTimeField('创建时间', default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '日报'
        verbose_name_plural = '日报'

    def __str__(self):
        return self.task
