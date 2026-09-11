from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe de ser mayor a 0 .")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser negativo.")
        return value
    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del producto debe tener al menos 3 caracteres.")
        return value
