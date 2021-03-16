from django.contrib import admin
from .models import Address, Project, ProjectUrl, Env
from guardian.admin import GuardedModelAdmin


class ProjectUrlAdmin(GuardedModelAdmin):
    list_display = ('name', 'url', 'project', 'env')


admin.site.register(Project)
admin.site.register(Env)
admin.site.register(ProjectUrl, ProjectUrlAdmin)
admin.site.register(Address)
