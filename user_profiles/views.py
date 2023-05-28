from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from bookings.models import Reservation, GameTime, Room
from datetime import datetime, date, timedelta
from django.utils import timezone
from django.contrib import messages



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

    context = {'reservations': reservations, 'current_date': current_date}

    return render(request, template, context)

def BookingEditSelection(request):
    template = 'reservation.edit.html'
    res_id = request.POST.get('res_id')
    new_date = request.POST.get('new_date')
    booked_res = Reservation.objects.filter(id=res_id)
    reservations = Reservation.objects.all()
    times = GameTime.objects.all()
    rooms = Room.objects.all()
    date = timezone.now().date()
    tomorrow = date + timedelta(days=2)
    today = tomorrow.strftime("%Y-%m-%d")

    context = {'reservations': reservations, 'booked_res': booked_res, 'times': times, 'rooms': rooms, 'today': today,'new_date': new_date}
    return render(request, template, context) 


def BookingEditConfirmation(request):
    template = 'reservation_edit_post.html'
    res_id = request.POST.get('res_id')
    old_booking = Reservation.objects.filter(id=res_id)
    new_time = request.POST.get('time')
    new_date = request.POST.get('picked_date')
    new_room = request.POST.get('room')

    context = {
        'res_id': res_id, 'old_booking': old_booking, 'new_time': new_time, 'new_date': new_date, 'new_room': new_room
    }

    return render(request, template, context)

def BookingUpdate(request):
    res_id = request.POST.get('res_id')
    new_time = request.POST.get('new_time')
    new_date = request.POST.get('new_date')
    new_room = request.POST.get('new_room')
    room = Room.objects.get(room_name=new_room)
    time = GameTime.objects.get(game_slot=new_time)

    reservation = Reservation.objects.get(id=res_id)
    reservation.date = new_date
    reservation.time_slot = time
    reservation.room_choice = room

    messages.success(request, 'Form submitted successfully!')
    reservation.save(update_fields=['date', 'time_slot','room_choice'])

    return redirect('account_overview')

def DeleteBooking(request):
    res_id = request.POST.get('res_id')
    res = Reservation.objects.filter(id=res_id)
    res.delete()

    return redirect('account_bookings')

def AccountUpdateView(request):
    template = 'account_page_edit.html'
    user_id = request.user.id
    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email

    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'user_id': user_id
    }

    return render(request, template, context)

def AccountUpdatePosting(request):
    user_id = int(request.POST.get('user_id'))
    new_first_name = request.POST.get('new_first_name')
    new_last_name = request.POST.get('new_last_name')
    new_email = request.POST.get('new_email')
    new_username = request.POST.get('new_username')

    update = User.objects.get(id=user_id)
    update.username = new_username
    update.first_name = new_first_name
    update.last_name = new_last_name
    update.email = new_email
    update.save(update_fields=['username', 'first_name','last_name', 'email'])

    messages.success(request, 'Form submitted successfully!')

    return redirect('account_overview')

def DeleteAccount(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        reservations = Reservation.objects.filter(user_id=user_id)
        reservations.delete()
        user.delete()
        messages.success(request, 'Account Deleted!')
        return redirect('home')
    else:
        return redirect('home')