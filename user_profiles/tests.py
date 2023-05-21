from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from bookings.models import Reservation, Room, GameTime
from datetime import datetime, date
from .views import AccountOverview, AccountReservations
from django.contrib.messages import get_messages



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
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create reservations for the user
        self.reservation1 = Reservation.objects.create(user_id=self.user.id, date=date(2023, 5, 1), price=100)

    def test_account_reservations_authenticated(self):
        # Log in the user
        self.client.force_login(self.user)

        # Send a GET request to the view
        response = self.client.get(reverse('account_bookings'))

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'account_bookings.html')

        # Assert that the reservations are passed to the template context
        reservations = response.context['reservations']
        self.assertEqual(len(reservations), 1)
        self.assertIn(self.reservation1, reservations)

        # Assert that the current date and time are passed to the template context
        current_date = response.context['current_date']
        self.assertEqual(current_date, date.today())


class BookingEditSelectionTestCase(TestCase):

    def setUp(self):
        # Create test data
        self.reservation = Reservation.objects.create(id=1, date=date(2023, 5, 1), price=100)
        self.time = GameTime.objects.create()
        self.room = Room.objects.create()
        self.url = reverse('account_booking_edit')
    
    def test_booking_edit_selection(self):
        # Send a POST request to the view
        data = {
            'res_id': self.reservation.id,
            'new_date': '2023-05-30',
        }
        response = self.client.post(self.url, data=data)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'reservation.edit.html')

        # Assert the context data
        self.assertEqual(response.context['reservations'].count(), 1)
        self.assertEqual(list(response.context['booked_res']), [self.reservation])
        self.assertEqual(response.context['times'].count(), 1)
        self.assertEqual(response.context['rooms'].count(), 1)
        self.assertEqual(response.context['new_date'], '2023-05-30')


class BookingEditConfirmationTestCase(TestCase):
    def test_booking_edit_confirmation(self):
        # Create test data
        room = Room.objects.create(room_name='Room 2')
        time = GameTime.objects.create(game_slot='18:00')
        reservation = Reservation.objects.create(id=1, date='2000-01-01', room_choice=room, time_slot=time, price=100)

        # Send a POST request to the view
        data = {
            'res_id': 1,
            'time': '18:00',
            'picked_date': '2023-06-15',
            'room': 'Room 2',
        }
        url = reverse('account_booking_edit_confirm')
        response = self.client.post(url, data=data)

        # Assert that the response has a 200 status code (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the rendered template
        self.assertTemplateUsed(response, 'reservation_edit_post.html')

        # Assert the context data
        self.assertEqual(response.context['new_time'], '18:00')
        self.assertEqual(response.context['new_date'], '2023-06-15')
        self.assertEqual(response.context['new_room'], 'Room 2')
        self.assertQuerysetEqual(response.context['old_booking'], [repr(reservation)])

class BookingUpdateTestCase(TestCase):

    def setUp(self):
        # Create test data
        self.room = Room.objects.create(room_name='Room 2')
        self.time = GameTime.objects.create(game_slot='18:00')
        self.reservation = Reservation.objects.create(id=1, date='2000-01-01', room_choice=self.room, time_slot=self.time, price=100)
        self.url = reverse('account_booking_edit_post')


    def test_booking_update(self):
        # Send a POST request to the view
        data = {
            'res_id': self.reservation.id,
            'new_time': '18:00',
            'new_date': '2023-06-15',
            'new_room': 'Room 2',
        }
        response = self.client.post(self.url, data=data)



        # Assert the updated reservation values
        updated_reservation = Reservation.objects.get(id=self.reservation.id)
        self.assertEqual(updated_reservation.date.strftime('%Y-%m-%d'), '2023-06-15')
        self.assertEqual(updated_reservation.time_slot, GameTime.objects.get(game_slot='18:00'))
        self.assertEqual(updated_reservation.room_choice, Room.objects.get(room_name='Room 2'))

        # Assert success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Form submitted successfully!')
