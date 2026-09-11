from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre de la categoría debe tener al menos 3 caracteres.")
        return value
    def validate_description(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("La descripción de la categoría debe tener al menos 10 caracteres.")
        return value
    