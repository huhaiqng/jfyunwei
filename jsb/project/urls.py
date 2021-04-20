from django.urls import path, include
from .views import GetGaingon666Domain, GetGaingon666DomainRecord, GetLingfannaoDomain, GetLingfannaoDomainRecord, \
    TaskResultViewSet, HostViewSet, EnvViewSet, MySQLInstanceViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'taskresult', TaskResultViewSet)
router.register(r'getEnv', EnvViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'mysqlInstance', MySQLInstanceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('getGaingon666Domain/', GetGaingon666Domain.as_view()),
    path('getGaingon666DomainRecord/', GetGaingon666DomainRecord.as_view()),
    path('getLingfannaoDomain/', GetLingfannaoDomain.as_view()),
    path('getLingfannaoDomainRecord/', GetLingfannaoDomainRecord.as_view()),
]
