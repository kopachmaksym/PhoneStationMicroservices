from rest_framework import viewsets, status
from .models import Bill
from .serializers import BillSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

@api_view(['GET'])
def unpaid_bills(request):
    if request.user.is_staff:
        unpaid_bills = Bill.objects.filter(is_paid=False)
        serializer = BillSerializer(unpaid_bills, many=True)
        return Response(serializer.data)
    else:
        return Response(status=403)

