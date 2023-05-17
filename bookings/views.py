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
        context['cart'] = []

        return context


    
class ReservationChoice(View):
    template = 'res_choice.html'


    def post(self, request):
        template = 'res_choice.html'
        specific_date = request.POST.get('picked_date')
        key = request.POST.get('room')
        value = request.POST.get('time')

        # Check if the item is already in the cart
        cart = request.session.get('cart', [])
        for item in cart:
            if item['key'] == key and item['value'] == value and item['specific_date'] == specific_date:
                # If the item already exists in the cart, do not add it again
                break
        else:
            # If the item does not exist in the cart, add it to the cart
            item = {'key': key, 'value': value, 'specific_date': specific_date}
            cart.append(item)
            request.session['cart'] = cart


        if 'delete-all' in request.POST:
            # Remove all items from the cart
            request.session.pop('cart', None)
        elif 'delete-item' in request.POST:
            # Get the key, value, and specific_date of the item to remove
            selected = request.POST.get('delete-item')
            key, value, specific_date = selected.split("|")
            # Find the item in the cart and remove it
            for item in request.session.get('cart', []):
                if item['key'] == key and item['value'] == value and item['specific_date'] == specific_date:
                    request.session['cart'].remove(item)
                    request.session.modified = True

                    break
        # Get the updated items to display on the page, including the user's cart


        date = timezone.now().date()
        today = date.strftime("%Y-%m-%d")
        times = ['12:00', '14:00', '16:00','18:00']
        rooms = ['Horror', 'Pirate']
        queryset = Reservation.objects.all()
        cart = [item for item in request.session.get('cart', []) if item.get('key') and item.get('value') and item.get('specific_date')]
       
        context = {
            'today': today,
            'times': times,
            'rooms': rooms,
            'queryset': queryset,
            'cart': cart,
        }

        return render(request, template, context)
