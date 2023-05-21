from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path('account_overview', views.AccountOverview, name='account_overview'),
    path('account_bookings', views.AccountReservations, name='account_bookings'),
    path('account_booking_edit', views.BookingEditSelection, name='account_booking_edit'),
    path('account_booking_edit_confirm', views.BookingEditConfirmation, name='account_booking_edit_confirm'),
    path('account_booking_edit_post', views.BookingUpdate, name='account_booking_edit_post'),
    path('account_update_view', views.AccountUpdateView, name='account_update_view'),
    path('account_update_post', views.AccountUpdatePosting, name='account_update_post'),
    path('delete_account', views.DeleteAccount, name='delete_account'),

]