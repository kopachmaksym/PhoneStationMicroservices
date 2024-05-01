from rest_framework import viewsets, status
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer