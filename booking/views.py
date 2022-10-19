from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,FormView,View,DeleteView
from .models import Room,Booking
from .forms import AvailabilityForm
from django.contrib.auth.models import User
from booking.booking_functions.availability import check_availability
# Create your views here

def RoomListView(request):
    return render (request,'room_list_view.html')

class BookingList(ListView):
    model=Booking



class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)


        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.Rooms_catog).get(room.category, None)
            context = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist !!')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')


def home(request):
    rooms = Room.objects.all()

    return render(request , 'home.html' , {'rooms' : rooms})


def roomview(request):
    return render(request, 'room_detail_view.html')

def restaurant(request):
    return render(request, 'Login/index.html')

