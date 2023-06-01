from django.test import TestCase
from .models import ContactUs
from .forms import ContactUsForm
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.sessions.middleware import SessionMiddleware
from .views import ContactUsForm, ContactUsPost
from django.contrib.auth.models import User


# Models


class ContactUsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        ContactUs.objects.create(
            inquiry_name="John",
            inquiry_email="john@example.com",
            phone_number="1234567890",
            inquiry_message="Test message",
            created_date="2023-01-01",
        )

    def test_inquiry_name_label(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        field_label = inquiry._meta.get_field("inquiry_name").verbose_name
        self.assertEqual(field_label, "inquiry name")

    def test_created_date_label(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        field_label = inquiry._meta.get_field("created_date").verbose_name
        self.assertEqual(field_label, "created date")

    def test_phone_number_max_length(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        max_length = inquiry._meta.get_field("phone_number").max_length
        self.assertEqual(max_length, 14)

    def test_magic_string(self):
        inquiry = ContactUs.objects.get(inquiry_id=1)
        string_representation = str(inquiry)

        self.assertEqual(
            string_representation,
            "{0} Inquiry Date: {1}".format(
                inquiry.inquiry_name, inquiry.created_date
            ),
        )


# Views


class ContactUsViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("contact_us")

    def test_get_contact_us(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertIsInstance(response.context["form"], ContactUsForm)


class ContactUsPostViewTestCase(TestCase):
    def test_post_valid_form(self):
        form_data = {
            "inquiry_name": "John Doe",
            "inquiry_email": "johndoe@example.com",
            "phone_number": "1234567890",
            "inquiry_message": "Test message",
        }
        response = self.client.post(reverse("contact_us_post"), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Message has been sent")

    def test_post_invalid_form(self):
        form_data = {
            "inquiry_name": "John Doe",
            "inquiry_email": "johndoe@example.com",
            "phone_number": "1234567890",
            # Missing inquiry_message field
        }
        response = self.client.post(reverse("contact_us_post"), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Error: Please try again")

    def test_get_form(self):
        # Test the method called after a failed form submission

        url = reverse("contact_us_post")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")
        self.assertIsInstance(response.context["form"], ContactUsForm)

# Forms


class ContactFormTestCase(TestCase):
    def test_form_init(self):
        form = ContactUsForm()

        # Assert that the form fields have the expected attributes
        self.assertEqual(
            form.fields["inquiry_name"].widget.attrs["class"], "form-control"
        )
        self.assertEqual(
            form.fields["inquiry_name"].widget.attrs["placeholder"],
            "Name",
        )

        self.assertEqual(
            form.fields["inquiry_email"].widget.attrs["class"], "form-control"
        )
        self.assertEqual(
            form.fields["inquiry_email"].widget.attrs["placeholder"],
            "Email",
        )

        self.assertEqual(
            form.fields["phone_number"].widget.attrs["class"], "form-control"
        )
        self.assertEqual(
            form.fields["phone_number"].widget.attrs["placeholder"],
            "Enter Your Phone Number",
        )

        self.assertEqual(
            form.fields["inquiry_message"].widget.attrs["class"],
            "form-control",
        )
        self.assertEqual(
            form.fields["inquiry_message"].widget.attrs["rows"], 6
        )
        self.assertEqual(
            form.fields["inquiry_message"].widget.attrs["placeholder"],
            "What is your Question?",
        )

    def test_form_clean_empty(self):
        # Test when all fields are empty
        form = ContactUsForm(data={})
        form.is_valid()  # Trigger the clean method

        self.assertFalse(form.is_valid())

        # Assert that the expected errors are added
        self.assertEqual(
            form.errors["inquiry_name"], ["This field is required."]
        )
        self.assertEqual(
            form.errors["inquiry_email"], ["This field is required."]
        )
        self.assertEqual(
            form.errors["phone_number"], ["This field is required."]
        )
        self.assertEqual(
            form.errors["inquiry_message"], ["This field is required."]
        )

    def test_form_clean_invalid_inquiry_name(self):
        # Test when a name is too long

        data = {
            "inquiry_name": """John Doe John Doe John Doe John Doe
            John Doe John Doe John Doe John Doe John""",
            "inquiry_email": "johndoe@example.com",
            "phone_number": "1234567890",
            "inquiry_message": "Hello, this is my message.",
        }
        form = ContactUsForm(data=data)

        self.assertFalse(form.is_valid())  # Trigger the clean method

        # Assert that the expected errors are added
        inquiry_name_error = (
            "Ensure this value has at most"
            " 75 characters (it has {0}).".format(len(data["inquiry_name"]))
        )
        self.assertEqual(
            form.errors["inquiry_name"],
            [inquiry_name_error],
        )

    def test_form_clean_all(self):
        # Test when all fields are filled
        data = {
            "inquiry_name": "John Doe",
            "inquiry_email": "johndoe@example.com",
            "phone_number": "1234567890",
            "inquiry_message": "Hello, this is my message.",
        }
        form = ContactUsForm(data=data)
        self.assertTrue(form.is_valid())  # Trigger the clean method

        # Assert that no errors are present
        self.assertFalse(form.errors)
