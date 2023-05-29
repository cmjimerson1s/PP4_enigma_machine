from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path("reservation", views.ReservationView, name="reservation"),
    path(
        "reservation_choice",
        views.ReservationChoice.as_view(),
        name="reservation_choice",
    ),
    path("booking_form", views.CartView, name="booking_form"),
    path("posted", views.update_database, name="posted"),
    path("confirmed", views.ConfirmView, name="confirmed"),
    path("", views.home, name="home"),
]
