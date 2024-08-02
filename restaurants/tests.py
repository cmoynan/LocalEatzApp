from django.test import TestCase
from .models import Restaurant, Booking
from django.contrib.auth.models import User
from datetime import date, time

# Create your tests here.


class RestaurantModelTest(TestCase):
    def setUp(self):
        """
        Set up the test environment by creating a Restaurant instance.
        This method is called before each test method runs.
        """
        self.restaurant = Restaurant.objects.create(
            name='Pizza Haven',
            address='Main Street Maynooth Co.Kildare',
            description='The best pizza in all of Ireland',
            max_tables=10
        )

    def test_restaurant_creation(self):
        """
        Test that a Restaurant object is created correctly.
        Retrieves the Restaurant object and checks its attributes.
        """
        restaurant = Restaurant.objects.get(id=self.restaurant.id)
        self.assertEqual(restaurant.name, 'Pizza Haven')
        self.assertEqual(restaurant.address, 'Main Street Maynooth Co.Kildare')
        self.assertEqual(
         restaurant.description,
         'The best pizza in all of Ireland'
        )

        self.assertEqual(restaurant.max_tables, 10)

    def test_string_representation(self):
        """
        Test the string representation of the Restaurant object.
        Ensures that the string representation matches the expected value.
        """
        self.assertEqual(str(self.restaurant), 'Pizza Haven')


class BookingModelTest(TestCase):
    def setUp(self):
        """
        Set up the test environment by creating a User, a Restaurant,
        and a Booking instance. This method
        is called before each test method runs.
        """
        # Create a user for testing
        self.user = User.objects.create_user(
         username='testuser',
         password='12345'
        )

        # Create a restaurant for testing
        self.restaurant = Restaurant.objects.create(
            name='Test Restaurant',
            address='123 Test St',
            description='A place for testing',
            max_tables=10
        )
        # Create a booking for testing
        self.booking = Booking.objects.create(
            user=self.user,
            restaurant=self.restaurant,
            name='John Doe',
            date=date(2024, 8, 1),
            time=time(19, 0),
            party_size=4
        )

    def test_booking_creation(self):
        """
        Test that a Booking object is created correctly.
        Retrieves the Booking object and checks its attributes.
        """
        booking = Booking.objects.get(id=self.booking.id)
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.restaurant, self.restaurant)
        self.assertEqual(booking.name, 'John Doe')
        self.assertEqual(booking.date, date(2024, 8, 1))
        self.assertEqual(booking.time, time(19, 0))
        self.assertEqual(booking.party_size, 4)

    def test_string_representation(self):
        """
        Test the string representation of the Booking object.
        Ensures that the string representation matches the expected format.
        """
        expected_str = (
         f"Booking for {self.booking.name} at {self.booking.restaurant.name} "
         f"on {self.booking.date} at {self.booking.time}"
        )

        self.assertEqual(str(self.booking), expected_str)
