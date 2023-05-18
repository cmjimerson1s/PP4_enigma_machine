from django.shortcuts import render
from .models import Reservation
from django.http import HttpResponse
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

def CartView(request):
    data = request.GET.get('cart')
    cart = CartTransform(data)
    template = 'res_booking_page.html'

    return render(request, template, {'data': cart})

def update_database(request):
    data = request.GET.get('data')
    dataset = CartTransform(data)
    if request.method == 'POST':
        for item in dataset:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            price = request.POST.get('price')
            date = item['specific_date']
            room = item['key']
            time = item['value']
            comment = request.POST.get('comment')
            user_id = request.POST.get('user_id')
            

            # Create a new instance of the Reservation model and set its attributes
            instance = Reservation()
            instance.customer_name = name
            instance.customer_email = email
            instance.phone_number = phone
            instance.price = price
            instance.date = date
            instance.room_choice = room
            instance.time_slot = time
            instance.comment = comment
            instance.user_id = user_id
            instance.save()
    if 'cart' in request.session:
        del request.session['cart']
    return HttpResponse('Data saved successfully.')






def CartTransform(data):
    string = data.replace('[', '').replace(']', '').replace('"', '')
    game_data = ast.literal_eval(string)
    if isinstance(game_data, dict):
    # if dataset is a dictionary, convert it to a tuple
        dataset = (game_data,)
    else:
        dataset = game_data

    return dataset
