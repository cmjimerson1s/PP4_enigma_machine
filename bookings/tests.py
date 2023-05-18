from django.test import TestCase, RequestFactory
from datetime import date
from .models import Reservation
from django.utils import timezone
from .views import ReservationView, ReservationChoice, CartTransform, CartView, update_database
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware


class ReservationListViewTest(TestCase):

    def setUp(self):
        self.reservation = Reservation.objects.create(
            customer_name='Test Test',
            customer_email='test@gmail.com',
            customer_phone='+123456789123',
            price=500,
            date='2000-01-01',
            time_slot='14:00',
            room_choice='Horror',
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
        # Create a sample Reservation instance
        reservation = Reservation.objects.create(
            customer_name='Test Test',
            customer_email='test@gmail.com',
            customer_phone='+123456789123',
            price=500,
            date='2000-01-01',
            time_slot='14:00',
            room_choice='Horror',
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


class UpdateDatabaseTestCase(TestCase):
    
    def test_update_database(self):
        # Mock the request object
        raw_data = "[{'name': 'John Doe','email': 'john@example.com','phone': '+121234567890','price': '100','comment': 'Test comment','specific_date' : '2000-01-01', 'key' : 'Horror','value' : '14:00','user_id': '1'}]"
        data = CartTransform(raw_data)

        url = reverse('posted')  
        url += f'?data={data}'

        post_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '+121234567890',
            'price': '100',
            'comment': 'Test comment',
            'specific_date': date(2000, 1, 1),  # Convert to datetime.date object
            'key': 'Horror',
            'value': '14:00',
            'user_id': '1',
        }
        
        session = self.client.session
        session['cart'] = [{'key': 'Horror', 'value': '14:00', 'specific_date': '2000-01-01'}]
        session.save()

        # Call the view function
        response = self.client.post(url, data=post_data)

        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        data = CartTransform(raw_data)

        # Assert that the data is saved to the database
        instances = Reservation.objects.all()
        self.assertEqual(instances.count(), 1)
        instance = instances.first()
        self.assertEqual(instance.customer_name, 'John Doe')
        self.assertEqual(instance.customer_email, 'john@example.com')
        self.assertEqual(instance.phone_number, '+121234567890')
        self.assertEqual(instance.price, 100)
        self.assertEqual(instance.date, date(2000, 1, 1))
        self.assertEqual(instance.room_choice, 'Horror')
        self.assertEqual(instance.time_slot, '14:00')
        self.assertEqual(instance.comment, 'Test comment')
        self.assertEqual(instance.user_id, 1)
        session = self.client.session
        self.assertNotIn('cart', session)


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