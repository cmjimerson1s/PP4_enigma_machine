from . import views
from django.views import View
from django.urls import path

urlpatterns = [
    path('rooms', views.RoomListView.as_view(), name='rooms'),
    path('<slug:slug>', views.RoomListViewDetail.as_view(), name='rooms_detail')

]