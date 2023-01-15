from django import forms
from django.forms import ModelForm, DateTimeInput, DateTimeField
from functions.models import Farm
from functools import partial
from .models import *

class InputFarmForm(ModelForm):

    class Meta:
        model = Farm
        fields = ['farm_name', 'longitude', 'latitude']


class CheckFarmForm(forms.Form):

    # date = forms.DateField(
    #     required=True,
    #     input_formats = ['%Y-%m-%d'],
    #     widget = forms.DateInput(
    #         attrs={
    #             'type': 'date',
    #             'class': 'form-control'},
    #         format='%Y-%m-%d')
    # )
    date = forms.ChoiceField(choices = [])
    farm = forms.ChoiceField(choices = [])

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CheckFarmForm, self).__init__(*args, **kwargs)
        get_farm = FarmDetails.objects.filter(user=self.request.user.username)[:1].get()
        self.fields['farm'].choices = [(get_farm.farm_name,get_farm.farm_name)]
        self.fields['date'].choices = [(x.date.strftime('%Y-%m-%d'), x.date) for x in FarmDetails.objects.filter(user=self.request.user.username)]

