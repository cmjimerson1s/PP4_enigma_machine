from django.test import TestCase
from .models import ContactUs
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.sessions.middleware import SessionMiddleware
from .views import ContactUsForm, ContactUsPost

class ContactUsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ContactUs.objects.create(
            inquiry_name='John', 
            inquiry_email='john@example.com', 
            phone_number='1234567890', 
            inquiry_message='Test message',
            created_date='2023-01-01',
        )

    def test_inquiry_name_label(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        field_label = inquiry._meta.get_field('inquiry_name').verbose_name
        self.assertEqual(field_label, 'inquiry name')

    def test_created_date_label(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        field_label = inquiry._meta.get_field('created_date').verbose_name
        self.assertEqual(field_label, 'created date')

    def test_phone_number_max_length(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        max_length = inquiry._meta.get_field('phone_number').max_length
        self.assertEqual(max_length, 14)

class ContactUsTestCase(TestCase):
    def setUp(self):
        self.url = reverse('contact_us')

    def test_get_contact_us(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertIsInstance(response.context['form'], ContactUsForm)



class ContactUsPostTestCase(TestCase):

    def test_post_valid_form(self):
        form_data = {
            'inquiry_name': 'John Doe',
            'inquiry_email': 'johndoe@example.com',
            'phone_number': '1234567890',
            'inquiry_message': 'Test message',
        }
        response = self.client.post(reverse('contact_us_post'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Message has been sent")


    def test_post_invalid_form(self):
        form_data = {
            'inquiry_name': 'John Doe',
            'inquiry_email': 'johndoe@example.com',
            'phone_number': '1234567890',
            # Missing inquiry_message field
        }
        response = self.client.post(reverse('contact_us_post'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Error: Please try again")

#Model form unit tests below
