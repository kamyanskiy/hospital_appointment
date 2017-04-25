from django.contrib import admin

# Register your models here.
from .models import Doctor, Appointment


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession')


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_phone',
                    'doctor', 'date', 'time', 'subject')
    list_filter = ['time', 'doctor', 'date']


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)