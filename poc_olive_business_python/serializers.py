from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=512)
    price = serializers.FloatField()
    active = serializers.BooleanField(default=True)

    class Meta:
        model = Product
        fields = ('__all__')