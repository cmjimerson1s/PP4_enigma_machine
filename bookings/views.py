from django.shortcuts import render, redirect
from .models import Reservation, GameTime, Room
from .forms import ReservationForm
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
        context['times'] = GameTime.objects.all()
        context['rooms'] = Room.objects.all()
        context['cart'] = []

        return context


    
class ReservationChoice(View):

    def post(self, request):
        template = 'res_choice.html'
        specific_date = request.POST.get('picked_date')
        key = request.POST.get('room')
        value = request.POST.get('time')
        new_date = request.POST.get('new_date')

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
        times = GameTime.objects.all()
        rooms = Room.objects.all()
        queryset = Reservation.objects.all()
        cart = [item for item in request.session.get('cart', []) if item.get('key') and item.get('value') and item.get('specific_date')]
       
        context = {
            'new_date': new_date,
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
    form = ReservationForm()
    template = 'res_booking_page.html'

    return render(request, template, {'data': cart, 'form': form})

def update_database(request):
    data = request.GET.get('data')
    dataset = CartTransform(data)
    if request.method == 'POST':
        for item in dataset:
            form = ReservationForm(request.POST)
            if form.is_valid():
                date = item['specific_date']
                room_name = item['key']
                time_slot = item['value']
                price = request.POST.get('price')
                user_id = request.POST.get('user_id')
                room = Room.objects.get(room_name=room_name)
                time = GameTime.objects.get(game_slot=time_slot)

                instance = form.save(commit=False)
                instance.date = date
                instance.room_choice = room
                instance.time_slot = time
                instance.price = price
                instance.user_id = user_id
                instance.save()

            else:
                form = ReservationForm()
                context = {'form': form, 'data': data}
                return render(request, 'reservations.html', context)

        if 'cart' in request.session:
            del request.session['cart']

        return redirect('reservation')





def CartTransform(data):
    string = data.replace('[', '').replace(']', '').replace('"', '')
    game_data = ast.literal_eval(string)
    if isinstance(game_data, dict):
    # if dataset is a dictionary, convert it to a tuple
        dataset = (game_data,)
    else:
        dataset = game_data

    return dataset
