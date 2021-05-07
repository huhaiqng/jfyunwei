from django.contrib import admin
from project.models import Project, Url, Env
from guardian.admin import GuardedModelAdmin


class ProjectUrlAdmin(GuardedModelAdmin):
    list_display = ('name', 'url', 'project', 'env')


admin.site.register(Project)
admin.site.register(Env)
admin.site.register(Url, ProjectUrlAdmin)
