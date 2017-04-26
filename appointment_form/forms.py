from django.forms import ModelForm

from datetimewidget.widgets import DateWidget

from .models import Appointment


class AppointmentForm(ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': DateWidget(
                attrs={'placeholder': "Select appointment date...",
                       'required': ""},
                usel10n=True,
                bootstrap_version=3)
        }
