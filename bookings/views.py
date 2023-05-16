from django.shortcuts import render
from .models import Reservation
from django.utils import timezone
from django.views import generic, View


class ReservationView(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.all()
    template_name = 'reservations.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = timezone.now().date()
        context['today'] = date.strftime("%Y-%m-%d")
        context['times'] = ['12:00', '14:00', '16:00','18:00']
        context['rooms'] = ['Horror', 'Pirate']

        return context

class ReservationChoice(View):
    def post(self, request):
        time = request.POST.get('time')
        date = request.POST.get('date')
        room = request.POST.get('room')
        template = 'res_choice.html'

        context = {
            'date': date,
            'time': time,
            'room': room,
        }

        return render(request, template, context)