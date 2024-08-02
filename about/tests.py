from django.test import TestCase
from .models import ContactQuery
from datetime import datetime
from django.utils import timezone


class ContactQueryModelTest(TestCase):
    def setUp(self):
        self.contact = ContactQuery.objects.create(
            name='John Doe',
            email='john.doe@example.com',
            phone_number='+1234567890'
        )

    def test_contact_query_creation(self):
        """Test that a ContactQuery object is created correctly."""
        contact = ContactQuery.objects.get(id=self.contact.id)
        self.assertEqual(contact.name, 'John Doe')
        self.assertEqual(contact.email, 'john.doe@example.com')
        self.assertEqual(contact.phone_number, '+1234567890')

    def test_string_representation(self):
        """Test the string representation of the ContactQuery object."""
        expected_str = 'John Doe - john.doe@example.com'
        self.assertEqual(str(self.contact), expected_str)

    def test_creation_time(self):
        """Test that the created_at field is set to the current time upon creation."""
        contact = ContactQuery.objects.get(id=self.contact.id)
        self.assertIsInstance(contact.created_at, datetime)
        now = timezone.now()
        self.assertAlmostEqual(
            contact.created_at,
            now,
            delta=timezone.timedelta(seconds=5)
        )
