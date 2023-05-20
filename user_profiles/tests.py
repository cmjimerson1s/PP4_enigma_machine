from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from bookings.models import Reservation, Room, GameTime
from datetime import datetime, date
from .views import AccountOverview, AccountReservations


class AccountOverviewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.url = reverse('account_overview')

    def test_account_overview_authenticated(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Send a GET request to the view
        response = self.client.get(self.url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'account_page.html')

        # Assert that the context contains the expected data
        self.assertEqual(response.context['username'], 'testuser')
        self.assertEqual(response.context['first_name'], '')
        self.assertEqual(response.context['last_name'], '')
        self.assertEqual(response.context['user_id'], self.user.id)
        self.assertEqual(response.context['email'], '')

    def test_account_overview_unauthenticated(self):
        # Send a GET request to the view without logging in
        response = self.client.get(self.url)

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected to the login page
        self.assertRedirects(response, '/accounts/login/?next=/user_profiles/account_overview')

    def test_account_overview_decorator(self):
        # Log in the user
        self.client.login(username='testuser', password='testpass')

        # Send a GET request to the view
        response = self.client.get(self.url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'account_page.html')

        # Assert that the context contains the expected data
        self.assertEqual(response.context['username'], 'testuser')
        self.assertEqual(response.context['first_name'], '')
        self.assertEqual(response.context['last_name'], '')
        self.assertEqual(response.context['user_id'], self.user.id)
        self.assertEqual(response.context['email'], '')


class AccountReservationsTestCase(TestCase):

    def setUp(self):
        room = Room.objects.create(room_name='Horror')
        time_slot = GameTime.objects.create(game_slot='12:00')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.reservation = Reservation.objects.create(
            user_id=self.user.id,
            room_choice=room,
            time_slot=time_slot,
            date=date.strftime('2000-01-01'),
            customer_name='Test Test',
            customer_email='test@gmail.com',
            customer_phone='+123456789123',
            price=500,
            comment='Test',
        )

        self.url = reverse('account_bookings')

    def test_account_reservations_authenticated(self):
        # Log in the user
        self.client.force_login(self.user)

        # Send a GET request to the view
        response = self.client.get(self.url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
 
        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'account_bookings.html')

        # Assert that the context contains the expected data
        self.assertEqual(len(response.context['entries']), 1)
        self.assertEqual(response.context['entries'][0].id, self.reservation.id)
        self.assertEqual(response.context['reservations'][0][0], self.reservation.date)
        self.assertEqual(response.context['reservations'][0][1], '14:00')
        self.assertEqual(response.context['reservations'][0][2], 'Room 1')
        self.assertEqual(response.context['reservations'][0][3], self.reservation.id)
        self.assertEqual(response.context['current_date'], date.today())

    def test_account_reservations_unauthenticated(self):
        # Send a GET request to the view without logging in
        response = self.client.get(self.url)

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 200)

        # Assert that the user is redirected to the login page
        self.assertRedirects(response, '/accounts/login/')