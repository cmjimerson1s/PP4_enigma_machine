from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from bookings.models import Room


class RoomListView(generic.ListView):
    model = Room
    queryset = Room.objects.all()
    template_name = "rooms/room_list.html"


class RoomListViewDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Room.objects.all()
        detail = get_object_or_404(queryset, slug=slug)
        template = "rooms/room_list_detail.html"
        context = {
            "detail": detail,
        }
        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        template = "rooms/room_list_detail.html"
        return render(request, template)
