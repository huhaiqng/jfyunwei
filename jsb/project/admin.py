from django.contrib import admin
from project.models import Project, Url, Env, BuildHost, ProjectModule
from guardian.admin import GuardedModelAdmin


class ProjectAdmin(GuardedModelAdmin):
    list_display = ('name', 'alias', 'deploy_obj', 'user', 'deploy_dir', 'log_dir', 'used')


class ProjectModuleAdmin(GuardedModelAdmin):
    list_display = ('project', 'module', 'pkg_name', 'pkg_type', 'port', 'deploy_dir', 'logfile')


class BuildHostAdmin(GuardedModelAdmin):
    list_display = ('project', 'host', 'env', 'user')


class ProjectUrlAdmin(GuardedModelAdmin):
    list_display = ('project', 'name', 'env', 'url', 'popular')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Env)
admin.site.register(Url, ProjectUrlAdmin)
admin.site.register(BuildHost, BuildHostAdmin)
admin.site.register(ProjectModule, ProjectModuleAdmin)
