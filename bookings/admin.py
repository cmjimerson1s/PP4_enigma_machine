from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'date', 'room_choice', 'time_slot')
    search_fields = ('customer_name', 'customer_email')
    list_filter = ('room_choice', 'date')