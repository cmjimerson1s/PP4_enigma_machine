from django.test import TestCase
from .models import Reservation
from . import views
from django.urls import reverse



class BlogPostListViewTest(TestCase):

    def setUp(self):
        self.reservation = Reservation.objects.create(
            customer_name = 'Test Test',
            customer_email = 'test@gmail.com',
            customer_phone = '+123456789123',
            price = 500,
            date = '2023-01-01',
            time_slot = '14:00',
            room_choice = 'Horror',
            comment = 'Test',
            user_id =  55,
        )

    def test_Reservation_List_View(self):
        response = self.client.get(reverse('reservation'))
        self.assertEqual(response.status_code, 200)

