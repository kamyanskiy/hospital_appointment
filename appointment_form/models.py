from django.db import models
from django.utils import timezone

WORKHOURS_CHOICES = (
    (1, "9:00-10:00"),
    (2, "10:00-11:00"),
    (3, "11:00-12:00"),
    (4, "12:00-13:00"),
    # (5, "13:00-14:00"), dinner
    (6, "14:00-15:00"),
    (7, "15:00-16:00"),
    (8, "16:00-17:00"),
    (9, "17:00-18:00"),
)


class Doctor(models.Model):
    name = models.CharField(max_length=256)
    profession = models.CharField(max_length=256)

    def __str__(self):
        return str(self.name)


class Appointment(models.Model):
    patient_name = models.CharField(max_length=256,
                                    help_text="Enter your full name here...",
                                    )
    patient_phone = models.CharField(max_length=32,
                                     help_text='Enter your phone number '
                                               'here...')
    subject = models.CharField(max_length=256,
                               help_text='Enter your subject here...')
    reason = models.TextField(max_length=1024,
                              help_text='Describe more details of your reason '
                                        'here...')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,
                               help_text="Select doctor...")
    time = models.IntegerField(choices=WORKHOURS_CHOICES, default=1)
    date = models.DateField(default=timezone.now(), editable=True)

    def __str__(self):
        return "{0} - {1} - {2}".format(self.patient_name,
                                        get_time_text(self.time),
                                        self.doctor)


def get_time_text(choice_num):
    for choice, text in WORKHOURS_CHOICES:
        if choice == choice_num:
            return text
