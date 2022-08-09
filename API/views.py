from API.serializers import OrderSerializer, ProductSerializer, StatSerializer
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
def stats_list(request, metric, date_start, date_end):
    try:
        if metric == "price":
            order = Order.objects.filter(Date__gt = date_start, Date__lt = date_end).annotate(
                month=TruncMonth('Date')).values('month').annotate(value=Sum('Products__Price')).values('month', 'value')
        elif metric == "count":
            order = Order.objects.filter(Date__gt = date_start, Date__lt = date_end).annotate(
                month=TruncMonth('Date')).values('month').annotate(value=Count('Products')).values('month', 'value')
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StatSerializer(order, many=True)
        return Response(serializer.data)
