from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("La contraseña debe tener al menos 6 caracteres.")
        return value

    def validate_profile(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("El perfil debe tener al menos 4 caracteres.")
        return value
    
