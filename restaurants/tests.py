from django.test import TestCase
from .models import Restaurant

# Create your tests here.

class RestaurantModelTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name='Pizza Haven',
            address='Main Street Maynooth Co.Kildare',
            description='The best pizza in all of Ireland',
            max_tables=10
        )

    def test_restaurant_creation(self):
        """Test that a Restaurant object is created correctly."""
        restaurant = Restaurant.objects.get(id=self.restaurant.id)
        self.assertEqual(restaurant.name, 'Pizza Haven')
        self.assertEqual(restaurant.address, 'Main Street Maynooth Co.Kildare')
        self.assertEqual(restaurant.description, 'The best pizza in all of Ireland')
        self.assertEqual(restaurant.max_tables, 10)

    def test_string_representation(self):
        """Test the string representation of the Restaurant object."""
        self.assertEqual(str(self.restaurant), 'Pizza Haven')

