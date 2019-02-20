from rest_framework import serializers
from .models import Providers


class ProvidersSeriealizer(serializers.ModelSerializer):
    """Serializer to map the model into JSON format"""
    class Meta:
        """Meta class to map serializer fields with the model fields"""
        model = Providers
        fields = ('name', 'email', 'phone', 'language', 'currency')
        read_only_fields = ('name', 'email', 'phone', 'language', 'currency')
