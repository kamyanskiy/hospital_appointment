# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_form', '0007_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.IntegerField(choices=[(1, '9:00-10:00'), (2, '10:00-11:00'), (3, '11:00-12:00'), (4, '12:00-13:00'), (5, '13:00-14:00'), (6, '14:00-15:00'), (7, '16:00-17:00'), (8, '17:00-18:00')], default=1, max_length=1),
        ),
    ]
