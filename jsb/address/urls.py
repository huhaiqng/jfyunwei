from django.urls import path, include
from address.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'address', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
