from django.test import TestCase, RequestFactory
from django.shortcuts import render
from datetime import date
from .models import Reservation, Room, GameTime
from .forms import ReservationForm
from django.http import HttpRequest
from django.utils import timezone
from .views import ReservationView, ReservationChoice, CartTransform, CartView, update_database
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string




class ReservationListViewTest(TestCase):

    def setUp(self):
        room = Room.objects.create(room_name='Horror')
        time_slot = GameTime.objects.create(game_slot='12:00')

        self.reservation = Reservation.objects.create(
            customer_name='Test Test',
            customer_email='test@gmail.com',
            customer_phone='+123456789123',
            price=500,
            date='2000-01-01',
            time_slot=time_slot,
            room_choice=room,
            comment='Test',
            user_id=55,
        )

    def test_Reservation_List_View(self):
        response = self.client.get(reverse('reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')
        self.assertContains(response, self.reservation.time_slot)
        self.assertContains(response, self.reservation.room_choice)
        context = response.context_data
        self.assertIn('today', context)
        expected_date = timezone.now().date().strftime("%Y-%m-%d")
        self.assertEqual(context['today'], expected_date)


class ReservationChoiceTestCase(TestCase):
    def test_post_method_adds_item_to_cart(self):
        room = Room.objects.create(room_name='Horror')
        time_slot = GameTime.objects.create(game_slot='12:00')
        # Create a sample Reservation instance
        reservation = Reservation.objects.create(
            customer_name='Test Test',
            customer_email='test@gmail.com',
            customer_phone='+123456789123',
            price=500,
            date='2000-01-01',
            time_slot=time_slot,
            room_choice=room,
            comment='Test',
            user_id=55,
        )

        # Set request data
        data = {
            'picked_date': '2023-05-17',
            'room': 'Horror',
            'time': '14:00',
        }

        # Add data to the session
        session = self.client.session
        session['cart'] = []
        session.save()

        # Call the post method
        response = self.client.post(reverse('reservation_choice'), data=data)

        # Assert that the item is added to the cart
        self.assertEqual(len(self.client.session.get('cart', [])), 1)

        # Assert that the added item matches the provided data
        cart_item = self.client.session['cart'][0]
        self.assertEqual(cart_item['specific_date'], '2023-05-17')
        self.assertEqual(cart_item['key'], 'Horror')
        self.assertEqual(cart_item['value'], '14:00')

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response template used
        self.assertTemplateUsed(response, 'res_choice.html')

        # Test item already in cart
        # Add an item to the cart
        existing_item = {'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'}
        session['cart'] = [existing_item]
        session.save()

        # Call the post method again with the same item data
        response = self.client.post(reverse('reservation_choice'), data=data)

        # Assert that the item is not added again
        self.assertEqual(len(self.client.session.get('cart', [])), 1)
        self.assertEqual(self.client.session['cart'][0], existing_item)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response template used
        self.assertTemplateUsed(response, 'res_choice.html')

        # Test delete-all action
        # Add some items to the cart
        session['cart'] = [{'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'},
                           {'key': 'Pirate', 'value': '16:00', 'specific_date': '2023-05-18'}]
        session.save()

        # Perform the delete-all action
        response = self.client.post(reverse('reservation_choice'), data={'delete-all': '1'})

        # Assert that the cart is emptied
        self.assertNotIn('cart', self.client.session)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response template used
        self.assertTemplateUsed(response, 'res_choice.html')

        # Test delete-item action
        # Add some items to the cart
        session['cart'] = [
            {'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'},
            {'key': 'Pirate', 'value': '16:00', 'specific_date': '2023-05-18'}
            ]

        session.save()

        # Perform the delete-item action
        delete_item_data = {'delete-item': 'Horror|14:00|2023-05-17'}
        response = self.client.post(reverse('reservation_choice'), data=delete_item_data)

        # Assert that the item is removed from the cart
        self.assertEqual(len(self.client.session.get('cart', [])), 2)
        self.assertEqual(self.client.session['cart'][0], {'key': 'Pirate', 'value': '16:00', 'specific_date': '2023-05-18'})

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the response template used
        self.assertTemplateUsed(response, 'res_choice.html')

class CartViewTestCase(TestCase):
    def test_cart_view(self):
        # Prepare the URL and data
        url = reverse('booking_form')
        data = {'cart': "[{'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'}]"}

        # Call the CartView function
        response = self.client.get(url, data)

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Assert the template used
        self.assertTemplateUsed(response, 'res_booking_page.html')

        # Assert the data passed to the template
        expected_data = CartTransform("[{'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'}]")
        self.assertEqual(response.context['data'], expected_data)


class ReservationViewTestCase(TestCase):
    def test_reservation_view(self):
        # Create related objects
        room = Room.objects.create(room_name='Horror')
        time_slot = GameTime.objects.create(game_slot='14:00')

        # Prepare test data
        raw_data = "[{'customer_name': 'John Doe','email': 'john@example.com','phone': '+121234567890','price': '100','comment': 'Test comment','specific_date' : '2000-01-01', 'key' : 'Horror','value' : '14:00','user_id': '1'}]"
        post_data = {
            'customer_name': 'John Doe',
            'customer_email': 'john@example.com',
            'customer_phone': '+12123456789',
            'price': 100,
            'comment': 'Test comment',
            'specific_date': '2000-01-01',
            'room_choice': room.id,
            'time_slot': time_slot.id,
            'user_id': 1,
        }

        data = CartTransform(raw_data)
        # Set up session data
        session = self.client.session
        session['cart'] = [{'key': 'Horror', 'value': '14:00', 'specific_date': '2000-01-01'}]
        session.save()

        # Call the view function
        url = reverse('posted')
        url += f'?data={data}'  # Adjust the URL name as needed
        response = self.client.post(url, data=post_data)

        # Assert that the response is a redirect
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/') 

        # Assert that the form is valid
        form = ReservationForm(data=post_data)
        self.assertTrue(form.is_valid())

        # Assert that the data is saved to the database
        instances = Reservation.objects.all()
        self.assertEqual(instances.count(), 1)
        instance = instances.first()
        self.assertEqual(instance.price, 100)
        self.assertEqual(instance.date.strftime('%Y-%m-%d'), '2000-01-01')
        self.assertEqual(instance.room_choice, room)
        self.assertEqual(instance.time_slot, time_slot)
        self.assertEqual(instance.user_id, 1)
        # Assert that the session data is cleared
        session = self.client.session
        self.assertNotIn('cart', session)
        

class ReservationViewElseBlockTestCase(TestCase):
    def test_else_block(self):
        # Set up session data
        session = self.client.session
        session['cart'] = [{'key': 'Horror', 'value': '14:00', 'specific_date': '2000-01-01'}]
        session.save()

        # Call the view function with a POST request and empty data
        post_data = {}
        raw_data = "['key','value','specific_date']"
        data = CartTransform(raw_data)
        url = reverse('posted')
        url += f'?data={data}'  
        response = self.client.post(url, data=post_data)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template is used
        self.assertTemplateUsed(response, 'reservations.html')

        # Assert that the form is in the context
        self.assertIsInstance(response.context['form'], ReservationForm)

class CartTransformTestCase(TestCase):

    def test_cart_transform_with_list(self):
        data = "[{'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'}]"
        expected_output = ({'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'},)

        result = CartTransform(data)

        self.assertEqual(result, expected_output)

    def test_cart_transform_with_dict(self):
        data = "{'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'}"
        expected_output = ({'key': 'Horror', 'value': '14:00', 'specific_date': '2023-05-17'},)

        result = CartTransform(data)

        self.assertEqual(result, expected_output)

    def test_cart_transform_with_other(self):
        data = "'Horror', '14:00', '2023-05-17'"
        expected_output = ('Horror', '14:00', '2023-05-17')

        result = CartTransform(data)

        self.assertEqual(result, expected_output)