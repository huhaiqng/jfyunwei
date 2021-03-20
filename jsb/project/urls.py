from django.urls import path
from .views import GetGaingon666Domain, GetGaingon666DomainRecord, GetLingfannaoDomain, GetLingfannaoDomainRecord

urlpatterns = [
    path('getGaingon666Domain/', GetGaingon666Domain.as_view()),
    path('getGaingon666DomainRecord/', GetGaingon666DomainRecord.as_view()),
    path('getLingfannaoDomain/', GetLingfannaoDomain.as_view()),
    path('getLingfannaoDomainRecord/', GetLingfannaoDomainRecord.as_view()),
]
