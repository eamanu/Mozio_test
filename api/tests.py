from django.test import TestCase
from .models import Providers
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class ModelTestCase(TestCase):
  """This TestCase define the test for Providers"""

  def setUp(self):
    """Define the setup test variables"""
    self.provider = Providers(name="Emmanuel Arias",
                              email="eamanu@eamanu.com",
                              phone="1234",
                              language="Spanish",
                              currency="ARS")

  def test_model_create(self):
    """Test that providers could be saved"""
    old = Providers.objects.count()
    self.provider.save()
    new = Providers.objects.count()
    self.assertNotEquals(old, new)


class ViewTestCase(TestCase):
  """TestCase for Views"""

  def setUp(self):
    """Define setup tests variables"""
    self.client = APIClient()
    self.provier_data = {'name': "Emmanuel", 'email': 'eamanu@eamanu.com',
                         'phone': "1234", 'language': 'Spanish',
                         'currency': "ARS"}
    self.response = self.client.post(
        reverse('create'),
        self.provider_data,
        format='json')

    def test_api_create_provider(self):
      """Test if the api create a provider"""
      self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
