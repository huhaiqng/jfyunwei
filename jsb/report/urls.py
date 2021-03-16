from django.urls import path, include
from report.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'daily', DailyViewSet)
router.register(r'getReportDaily', GetDailyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
