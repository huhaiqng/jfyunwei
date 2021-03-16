from django.apps import AppConfig
from django.core.management import call_command


class ProjectConfig(AppConfig):
    name = 'project'
    verbose_name = '项目'
    verbose_name_plural = verbose_name

    # def ready(self):
    #     call_command('runapscheduler')
