from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path('account_overview', views.AccountOverview, name='account_overview'),
    path('account_bookings', views.AccountReservations, name='account_bookings'),
    path('account_bokking_edit', views.BookingEditSelection, name='account_booking_edit')

]