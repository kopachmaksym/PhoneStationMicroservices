from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'bills', BillViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('unpaid_bills/', unpaid_bills, name='unpaid_bills'),
]
