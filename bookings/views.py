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
    template = 'res_choice.html'


    def post(self, request):
        template = 'res_choice.html'

        date = timezone.now().date()
        today = date.strftime("%Y-%m-%d")
        times = ['12:00', '14:00', '16:00','18:00']
        rooms = ['Horror', 'Pirate']
        queryset = Reservation.objects.all()
        picked_date = request.POST.get('picked_date')

        context = {
            'today': today,
            'times': times,
            'rooms': rooms,
            'queryset': queryset,
            'picked_date': picked_date,
        }

        return render(request, template, context)