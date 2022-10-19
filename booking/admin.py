from django.contrib import admin
from .models import Room
from .models import Booking, Restaurant

# Register your models here.
class Info(admin.ModelAdmin):
    list_display=['number','category','Capacity','price','active']
    list_display_links=['number']
    list_editable=['category','Capacity','price','active']
    search_fields=['number']
    list_filter=['category','price']
    
class details(admin.ModelAdmin):
    list_display=['user','room','check_in','check_out']


admin.site.register(Restaurant)
admin.site.register(Room,Info)
admin.site.register(Booking,details)

admin.site.site_header='Mandarin Oriental'
admin.site.site_title='Mandarin Oriental'