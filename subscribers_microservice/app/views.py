from rest_framework import viewsets, status
from .models import Subscriber
from .serializers import SubscriberSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    @action(detail=True, methods=['post'], url_path='block_subscriber')
    def block_subscriber(self, request, pk=None):
        if not request.user.is_staff:
            return Response({'status': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)

        subscriber = self.get_object()
        subscriber.is_active = False
        subscriber.save()
        return Response({'status': 'subscriber blocked'})

