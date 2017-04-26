from django.shortcuts import render

from .forms import AppointmentForm
from .models import Appointment, WORKHOURS_CHOICES


def index(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            doctor = form_data['doctor']
            if doctor.appointment_set.filter(date=form_data['date'],
                                             time=form_data['time']):
                busy_hours = []
                for appointment in doctor.appointment_set.filter(
                        date=form_data['date']):
                    busy_hours.append(appointment.time)
                current_schedule = []
                for k, v in WORKHOURS_CHOICES:
                    if k in busy_hours:
                        current_schedule.append((v, 'busy'))
                    else:
                        current_schedule.append((v, 'free'))
                return render(request,
                              'appointment_form/busy_list.html',
                              {'doctor': doctor,
                               'current_schedule': current_schedule,
                               'date': form_data['date']
                               })
            appointment = Appointment.objects.create(**form_data)
            return render(request, 'appointment_form/thanks.html',
                          {'appointment': appointment})
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form/appointment_form.html',
                  {'form': form})
