from .models import Form, Question
from django.contrib.auth.admin import User
from django import forms
from django.db import models


#class FormsForm(forms.Form):
    # FORM_STATUS = (
    #     ('AC', 'active'),
    #     ('DA', 'deactivated'),
    #
    # )
    # form_heading = models.CharField(max_length=50)
    # form_link = models.TextField()
    # form_status = models.CharField(choices=FORM_STATUS, max_length=10)


class NameForm(forms.Form):
    FORM_STATUS = (
        ('AC', 'active'),
        ('DA', 'deactivated'),

    )
    form_heading = forms.CharField(max_length=50)
 #   form_link = forms.CharField()
    form_status = forms.ChoiceField(choices=FORM_STATUS)