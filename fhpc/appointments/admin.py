from django.contrib import admin
from .models import Appointments
# Register your models here.
class AppointmentsAdmin(admin.ModelAdmin):
    model = Appointments
    list_display = (
        'customer',
        'pet',
        'start_time',
        'end_time',
        'location',
        'notes'
    )
admin.site.register(Appointments, AppointmentsAdmin)