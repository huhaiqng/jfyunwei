from django.db import models


# 环境
class Env(models.Model):
    name = models.CharField('环境', max_length=200)

    class Meta:
        verbose_name = '环境'
        verbose_name_plural = '环境'

    def __str__(self):
        return self.name
