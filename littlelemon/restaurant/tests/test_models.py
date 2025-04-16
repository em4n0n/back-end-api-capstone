from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=10, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 10.0)
        self.assertEqual(item.inventory, 100)