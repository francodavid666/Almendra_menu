from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings

class pasteleria_form (forms.ModelForm):

    class Meta:
        model = pasteleria_model 
        fields = '__all__'


class salados_form(forms.ModelForm):

    class Meta:
        model = pasteleria_model
        fields = '__all__'


class bebidas_form(forms.ModelForm):

    class Meta:
        model = bebidas_model
        fields = '__all__'


class cafes_form(forms.ModelForm):

    class Meta:
        model = cafes_model
        fields = '__all__'


class brunch_form(forms.ModelForm):

    class Meta:
        model = brunch_model
        fields = '__all__'
       