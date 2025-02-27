from django.contrib import admin
from .models import MenuItem, ReservationItem

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(ReservationItem)