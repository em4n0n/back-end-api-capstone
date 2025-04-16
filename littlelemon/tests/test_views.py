from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.item1 = MenuItem.objects.create(name="Pasta", price=10.99, description="Creamy Alfredo pasta")
        self.item2 = MenuItem.objects.create(name="Pizza", price=12.99, description="Wood-fired Margherita pizza")
        self.item3 = MenuItem.objects.create(name="Salad", price=8.50, description="Fresh garden salad")

    def test_getall(self):
        response = self.client.get('/menu/')
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)