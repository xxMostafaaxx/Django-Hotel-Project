from django.urls import path,reverse
from .views import RoomListView,BookingList,RoomDetailView,home
from . import views

app_name='booking.apps.BookingConfig'

urlpatterns = [
    path('',home,name='home'),
    path('roomlist',views.RoomListView, name='RoomList'),
    path('booking_list/',views.BookingList,name='BookingList'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('home/', views.home, name = 'room_list'),
    path('room_detail_view/', views.roomview, name='booking')
    
]
 