"""jsb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.core.management import call_command


# 执行定时任务
# call_command('runapscheduler')
urlpatterns = [
    path('api/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('admin/', admin.site.urls),
    re_path(r'^api/', include(('report.urls', 'report'))),
    re_path(r'^api/', include(('address.urls', 'address'))),
    re_path(r'^api/', include(('auth_permission.urls', 'auth_permission'))),
]
