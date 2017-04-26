from django import forms
from django.forms import ModelForm, SelectDateWidget

from .models import Appointment


class AppointmentForm(ModelForm):
    date = forms.DateField(widget=SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day")))

    class Meta:
        model = Appointment
        fields = '__all__'
