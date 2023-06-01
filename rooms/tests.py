from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from bookings.models import Room
from .views import RoomListViewDetail


# RoomListView covered by related tests


class RoomListViewDetailTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Room.objects.create(
            room_name="TestRoom room_name",
            slug="TestRoom",
            short_room_description="TestRoom short_description",
            room_description="TestRoom room_description",
        )

    def test_room_list_view_detail_unauthenticated(self):
        # Unauthenticated user should be able to view the room detail

        testRoom = Room.objects.get(slug__exact="TestRoom")
        response = self.client.get(
            reverse("rooms_detail", args=[testRoom.slug])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "rooms/room_list_detail.html")
        self.assertContains(response, testRoom.room_name)
