from django.contrib import admin
from .models import Address, Project, ProjectUrl, Env
from guardian.admin import GuardedModelAdmin


class ProjectUrlAdmin(GuardedModelAdmin):
    list_display = ('name', 'url', 'project', 'env')


class AddressAdmin(GuardedModelAdmin):
    list_display = ('name', 'url', 'order')


admin.site.register(Project)
admin.site.register(Env)
admin.site.register(ProjectUrl, ProjectUrlAdmin)
admin.site.register(Address, AddressAdmin)
