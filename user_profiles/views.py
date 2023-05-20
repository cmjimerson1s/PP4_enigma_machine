from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from bookings.models import Reservation, GameTime, Room
from datetime import datetime, date



@login_required
def AccountOverview(request):
    template = 'account_page.html'

    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    user_id = request.user.id
    email = request.user.email

    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'user_id': user_id,
        'email': email,
        
    }

    return render(request, template, context)

def AccountReservations(request):
    template = 'account_bookings.html'
    user_id = request.user.id

    reservations = Reservation.objects.filter(user_id=user_id)

    current_datetime = datetime.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    context = {'reservations': reservations, 'current_date': current_date, 'current_time': current_time}

    return render(request, template, context)