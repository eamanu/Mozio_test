from rest_framework import generics
from .models import Providers
from .serializers import ProvidersSeriealizer


class CreateView(generics.ListCreateAPIView):
    """Thhis class define the create behaviour"""
    queryset = Providers.objects.all()
    serializer_class = ProvidersSeriealizer

    def perfom_create(self, serializer):
        """Save the POST data"""
        serializer.save()
