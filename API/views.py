from API.serializers import OrderSerializer, ProductSerializer, CountSerializer
from .models import Order, Product
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def price_list(request, date_start, date_end):
    try:
        order = Order.objects.filter(Date__gt = date_start, Date__lt = date_end).annotate(
            month=TruncMonth('Date')).values('month').annotate(value=Sum('Products')).values('month', 'value')
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountSerializer(order, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def count_list(request, date_start, date_end):
    try:
        order = Order.objects.filter(Date__gt = date_start, Date__lt = date_end).annotate(
            month=TruncMonth('Date')).values('month').annotate(value=Count('Products')).values('month', 'value')
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountSerializer(order, many=True)
        return Response(serializer.data)


   