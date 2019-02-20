from rest_framework import generics
from .models import Providers
from .serializers import ProvidersSeriealizer


class ListView(generics.ListAPIView):
    """This View define the list behaviour"""
    queryset = Providers.objects.all()
    serializer_class = ProvidersSeriealizer


class CreateView(generics.CreateAPIView):
    """This class define the create behaviour"""
    queryset = Providers.objects.all()
    serializer_class = ProvidersSeriealizer

    def perform_create(self, serializer):
        serializer.save()


class UpdateView(generics.ListAPIView):
    """Thhis class define the update behaviour"""
    queryset = Providers.objects.all()
    serializer_class = ProvidersSeriealizer

    def perform_update(self, serializer):
        serializer.save()


class DeleteView(generics.ListAPIView):
    """Thhis class define the Delete behaviour"""
    queryset = Providers.objects.all()
    serializer_class = ProvidersSeriealizer

    def perform_destroy(self, serializer):
        serializer.delete()
