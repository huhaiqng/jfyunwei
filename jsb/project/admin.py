from django.contrib import admin
from project.models import Project, Url, Env, BuildHost
from guardian.admin import GuardedModelAdmin


class ProjectAdmin(GuardedModelAdmin):
    list_display = ('name', 'alias', 'deploy_obj', 'user', 'deploy_dir', 'log_dir')


class BuildHostAdmin(GuardedModelAdmin):
    list_display = ('project', 'host', 'env', 'user')


class ProjectUrlAdmin(GuardedModelAdmin):
    list_display = ('project', 'name', 'env', 'url')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Env)
admin.site.register(Url, ProjectUrlAdmin)
admin.site.register(BuildHost, BuildHostAdmin)
