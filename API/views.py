from API.serializers import OrderSerializer
from rest_framework import viewsets, permissions
from .models import Order

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]