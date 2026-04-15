from django.contrib import admin
from .models import Residence, Room, Student, Reservation

admin.site.register(Residence)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Reservation)