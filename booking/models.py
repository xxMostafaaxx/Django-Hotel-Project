from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
class Room(models.Model):
    Rooms_catog=(
        ('Triple','Triple Room'),
        ('Non-Conditioned 2','Non-Conditioned'),
        ('Non-Conditioned 3','Non-Conditioned '),
        ('Deluxe','Deluxe Rooom'),
        ('Single','Single Room'),
        ('Double','Double Room '),
    )
    #user = models.OneToOneField(User , verbose_name=("user"), on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=Rooms_catog)
    Beds = models.IntegerField(blank=True, null=True)
    Capacity = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/%y/%m/%d', blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.category

    class Meta:
        verbose_name = ("Room")
        verbose_name_plural = ("Rooms")

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    
    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in}  to {self.check_out}'
    
    # def get_cancel_booking_url(self):

