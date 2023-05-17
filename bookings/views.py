from django.shortcuts import render
from .models import Reservation
from django.utils import timezone
from django.views import generic, View
import ast



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
        picked_date = request.POST.get('picked_date')
        room = request.POST.get('room')
        time = request.POST.get('time')

        # Check if the item is already in the cart
        cart = request.session.get('cart', [])
        for item in cart:
            if item['picked_date'] == picked_date and item['room'] == room and item['time'] == time:
                # If the item already exists in the cart, do not add it again
                break
        else:
            # If the item does not exist in the cart, add it to the cart
            item = {'picked_date': picked_date, 'room': room, 'time': time}
            cart.append(item)
            request.session['cart'] = cart


        if 'delete-all' in request.POST:
            # Remove all items from the cart
            request.session.pop('cart', None)
        elif 'delete-item' in request.POST:
            # Get the key, value, and specific_date of the item to remove
            selected = request.POST.get('delete-item')
            picked_date, room, time = selected.split("|")
            # Find the item in the cart and remove it
            for item in request.session.get('cart', []):
                if item['picked_date'] == picked_date and item['room'] == room and item['time'] == time:
                    request.session['cart'].remove(item)
                    request.session.modified = True
                    break

        date = timezone.now().date()
        today = date.strftime("%Y-%m-%d")
        times = ['12:00', '14:00', '16:00','18:00']
        rooms = ['Horror', 'Pirate']
        queryset = Reservation.objects.all()
        cart = [item for item in request.session.get('cart', []) if item.get('picked_date') and item.get('time') and item.get('room')]
       
        context = {
            'today': today,
            'times': times,
            'rooms': rooms,
            'queryset': queryset,
            'cart': cart,
        }

        return render(request, template, context)

def CartView(request):
    data = request.GET.get('cart')
    cart = CartTransform(data)
    template = 'res_booking_page.html'

    return render(request, template, {'data': cart})

def CartTransform(data):
    string = data.replace('[', '').replace(']', '').replace('"', '')
    game_data = ast.literal_eval(string)
    if isinstance(game_data, dict):
    # if dataset is a dictionary, convert it to a tuple
        dataset = (game_data,)
    else:
        dataset = game_data

    return dataset
