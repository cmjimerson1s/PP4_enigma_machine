from django.contrib import admin
from .models import Reservation, GameTime, Room


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "date", "room_choice", "time_slot")
    search_fields = ("customer_name", "customer_email")
    list_filter = ("room_choice", "date")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("room_name",)}


admin.site.register(GameTime)
