from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from bookings.models import Reservation, Room, GameTime
from datetime import datetime, date
from .views import (
    AccountOverview,
    AccountReservations,
    DeleteBooking,
    DeleteAccount,
)
from django.contrib.messages import get_messages


class AccountOverviewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="testuser", password="testpass"
        )
        cls.url = reverse("account_overview")

    def test_account_overview_authenticated(self):
        # Authenticated user should be able to view their account overview

        # Log in the user
        self.client.login(username="testuser", password="testpass")

        # Send a GET request to the view
        response = self.client.get(self.url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, "user_profiles/account_page.html")

        # Assert that the context contains the expected data
        self.assertEqual(response.context["username"], "testuser")
        self.assertEqual(response.context["first_name"], "")
        self.assertEqual(response.context["last_name"], "")
        self.assertEqual(response.context["user_id"], self.user.id)
        self.assertEqual(response.context["email"], "")

    def test_account_overview_unauthenticated(self):
        # Unauthenticated user should be redirected to login before coming back

        # Send a GET request to the view without logging in
        response = self.client.get(self.url)

        # Assert that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Assert that the user is redirected to the login page
        self.assertRedirects(
            response, "/accounts/login/?next=/user_profiles/account_overview"
        )


class AccountReservationsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_account_reservations_empty(self):
        # User with no reservations should be able to view their
        # reservations list

        # Log in the user
        self.client.force_login(self.user)

        # Send a GET request to the view
        response = self.client.get(reverse("account_bookings"))

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(
            response, "user_profiles/account_bookings.html"
        )

        # Assert that the empty reservations QuerySet is
        # passed to the template context
        reservations = response.context["reservations"]
        self.assertEqual(len(reservations), 0)

        # Assert that the current date and time are
        # passed to the template context
        current_date = response.context["current_date"]
        self.assertEqual(current_date, date.today())

    def test_account_reservations_single(self):
        # User with a single reservation should be able to view their
        # reservations list

        # Create one reservation for the user
        reservation1 = Reservation.objects.create(
            user_id=self.user.id, date=date(2023, 5, 1), price=100
        )

        # Log in the user
        self.client.force_login(self.user)

        # Send a GET request to the view
        response = self.client.get(reverse("account_bookings"))

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(
            response, "user_profiles/account_bookings.html"
        )

        # Assert that the reservations are passed to the template context
        reservations = response.context["reservations"]
        self.assertEqual(len(reservations), 1)
        self.assertIn(reservation1, reservations)

        # Assert that the current date and time are
        # passed to the template context
        current_date = response.context["current_date"]
        self.assertEqual(current_date, date.today())

    def test_account_reservations_multiple(self):
        # User with multiple reservations should be able to view their
        # reservations list

        # Create one reservation for the user
        reservation1 = Reservation.objects.create(
            user_id=self.user.id, date=date(2023, 5, 1), price=100
        )
        reservation2 = Reservation.objects.create(
            user_id=self.user.id, date=date(2023, 5, 2), price=200
        )

        # Log in the user
        self.client.force_login(self.user)

        # Send a GET request to the view
        response = self.client.get(reverse("account_bookings"))

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(
            response, "user_profiles/account_bookings.html"
        )

        # Assert that the reservations are passed to the template context
        reservations = response.context["reservations"]
        self.assertEqual(len(reservations), 2)
        self.assertIn(reservation1, reservations)
        self.assertIn(reservation2, reservations)

        # Assert that the current date and time are
        # passed to the template context
        current_date = response.context["current_date"]
        self.assertEqual(current_date, date.today())


class BookingEditSelectionTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data
        cls.reservation = Reservation.objects.create(
            id=1, date=date(2023, 5, 1), price=100
        )
        cls.time = GameTime.objects.create()
        cls.room = Room.objects.create()
        cls.url = reverse("account_booking_edit")

    def test_booking_edit_selection(self):
        # Send a POST request to the view
        data = {
            "res_id": self.reservation.id,
            "new_date": "2023-05-30",
        }
        response = self.client.post(self.url, data=data)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(
            response, "user_profiles/reservation.edit.html"
        )

        # Assert the context data
        self.assertEqual(response.context["reservations"].count(), 1)
        self.assertEqual(
            list(response.context["booked_res"]), [self.reservation]
        )
        self.assertEqual(response.context["times"].count(), 1)
        self.assertEqual(response.context["rooms"].count(), 1)
        self.assertEqual(response.context["new_date"], "2023-05-30")


class BookingEditConfirmationTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data
        return

    def test_booking_edit_confirmation(self):
        # Create test data
        room = Room.objects.create(room_name="Room 2")
        time = GameTime.objects.create(game_slot="18:00")
        reservation = Reservation.objects.create(
            id=1,
            date="2000-01-01",
            room_choice=room,
            time_slot=time,
            price=100,
        )

        # Send a POST request to the view
        data = {
            "res_id": 1,
            "time": "18:00",
            "picked_date": "2023-06-15",
            "room": "Room 2",
        }
        url = reverse("account_booking_edit_confirm")
        response = self.client.post(url, data=data)

        # Assert that the response has a 200 status code (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the rendered template
        self.assertTemplateUsed(
            response, "user_profiles/reservation_edit_post.html"
        )

        # Assert the context data
        self.assertEqual(response.context["new_time"], "18:00")
        self.assertEqual(response.context["new_date"], "2023-06-15")
        self.assertEqual(response.context["new_room"], "Room 2")
        self.assertQuerysetEqual(
            response.context["old_booking"], [repr(reservation)]
        )


class BookingUpdateTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data
        cls.room = Room.objects.create(room_name="Room 2")
        cls.time = GameTime.objects.create(game_slot="18:00")
        cls.reservation = Reservation.objects.create(
            id=1,
            date="2000-01-01",
            room_choice=cls.room,
            time_slot=cls.time,
            price=100,
        )
        cls.url = reverse("account_booking_edit_post")

    def test_booking_update(self):
        # Send a POST request to the view
        data = {
            "res_id": self.reservation.id,
            "new_time": "18:00",
            "new_date": "2023-06-15",
            "new_room": "Room 2",
        }
        response = self.client.post(self.url, data=data)

        # Assert the updated reservation values
        updated_reservation = Reservation.objects.get(id=self.reservation.id)
        self.assertEqual(
            updated_reservation.date.strftime("%Y-%m-%d"), "2023-06-15"
        )
        self.assertEqual(
            updated_reservation.time_slot,
            GameTime.objects.get(game_slot="18:00"),
        )
        self.assertEqual(
            updated_reservation.room_choice,
            Room.objects.get(room_name="Room 2"),
        )

        # Assert success message is displayed
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Reservation updated successfully!")


class DeleteBookingTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test reservation
        cls.reservation = Reservation.objects.create(
            id=1, price=100, date="2000-01-01"
        )

    def test_delete_booking(self):
        # Send a POST request to the view with the reservation ID
        response = self.client.post(
            reverse("delete_booking"), {"res_id": self.reservation.id}
        )

        # Assert that the response redirects to the account_bookings page
        self.assertRedirects(response, reverse("account_bookings"))

        # Assert that the reservation is deleted
        self.assertFalse(
            Reservation.objects.filter(id=self.reservation.id).exists()
        )


class AccountUpdateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        cls.url = reverse("account_update_view")

    def test_account_update_view(self):
        # Log in the user
        self.client.login(username="testuser", password="testpassword")

        # Send a GET request to the view
        response = self.client.get(self.url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(
            response, "user_profiles/account_page_edit.html"
        )

        # Assert that the context contains the user information
        self.assertEqual(response.context["username"], "testuser")
        self.assertEqual(response.context["first_name"], "")
        self.assertEqual(response.context["last_name"], "")
        self.assertEqual(response.context["email"], "")


class AccountUpdatePostingTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        cls.url = reverse("account_update_post")

    def test_account_update_posting(self):
        # Log in the user
        self.client.login(username="testuser", password="testpassword")

        # Send a POST request to the view with updated user information
        data = {
            "user_id": self.user.id,
            "new_username": "newusername",
            "new_first_name": "John",
            "new_last_name": "Doe",
            "new_email": "newemail@example.com",
        }
        response = self.client.post(self.url, data=data)

        # Assert that the response redirects to the account overview page
        self.assertRedirects(response, "/user_profiles/account_overview")

        # Assert that the user information is updated
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "newusername")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "newemail@example.com")

        # Assert success message is displayed
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Form submitted successfully!")


class DeleteAccountTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create a test reservation associated with the user
        cls.reservation = Reservation.objects.create(
            user_id=cls.user.id, price=100, date="2000-01-01"
        )

    def test_delete_account(self):
        # Log in the user
        client = Client()
        client.login(username="testuser", password="testpassword")

        # Send a POST request to the view
        response = client.post(reverse("delete_account"))

        # Check the response status code and redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

        # Check that the user and reservations are deleted
        self.assertFalse(User.objects.filter(id=self.user.id).exists())
        self.assertFalse(
            Reservation.objects.filter(user_id=self.user.id).exists()
        )

        # Check the success message
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Account Deleted!")

    def test_delete_account_not_authenticated(self):
        # Create a new client
        client = Client()

        # Send a POST request to the view
        response = client.post(reverse("delete_account"))

        # Check the response status code and redirect
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

        # Check that the user is not deleted
        self.assertTrue(User.objects.filter(id=self.user.id).exists())
