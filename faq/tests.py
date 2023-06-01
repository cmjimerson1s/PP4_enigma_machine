from django.test import TestCase, Client
from django.urls import reverse
from .views import FaqList
from .models import Faq


# Views


class FaqListViewTest(TestCase):
    def test_faq_list_view(self):
        # Test that the page renders
        response = self.client.get(reverse("faq"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("faq/faq.html")


# Models


class FaqModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question = "How do I know this is working?"
        cls.answer = "Because I have automated tests!"

    def test_faq_model_valid(self):
        # Create a Faq instance with valid data

        new_faq = Faq.objects.create(
            question=self.question, answer=self.answer
        )

        self.assertEqual(new_faq.question, self.question)
        self.assertEqual(new_faq.answer, self.answer)

    def test_faq_model_magic_string(self):
        # Test the magic string function for the class

        new_faq = Faq.objects.create(
            question=self.question, answer=self.answer
        )
        string_representation = str(new_faq)

        self.assertEqual(string_representation, self.question)
