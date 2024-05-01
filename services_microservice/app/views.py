from rest_framework import viewsets, status
from .models import Service
from .serializers import ServiceSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
