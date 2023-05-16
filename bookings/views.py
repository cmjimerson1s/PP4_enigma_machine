from django.shortcuts import render
from .models import Reservation
from django.views import generic, View


class ReservationView(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name = 'reservations.html'

