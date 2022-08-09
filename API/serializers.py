from .models import Order, Product
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'Date', 'Products']
        depth = 1 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'Title', 'Price']

class StatSerializer(serializers.ModelSerializer):
    value = serializers.DecimalField(max_digits=6, decimal_places=2, required = True)
    month = serializers.DateField(required = True)

    class Meta:
        model = Order
        fields = ['month', 'value']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['month'] = instance["month"].strftime('%Y %b')
        return representation