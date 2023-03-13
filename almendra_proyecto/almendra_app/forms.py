from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings

class pasteleria_form (forms.ModelForm):

    

    class Meta:
        model = pasteleria_model 
        fields = '__all__'
        widgets = {'informacion':forms.Textarea(
            attrs = {'class':'form__informacion','placeholder':'informacion'}
        )}


class salados_form(forms.ModelForm):

    class Meta:
        model = pasteleria_model
        fields = '__all__'


class bebidas_form(forms.ModelForm):

    class Meta:
        model = bebidas_model
        fields = '__all__'
        widgets = {'informacion':forms.Textarea(
            attrs = {'class':'form__informacion','placeholder':'informacion'}
        )}
    


class cafes_form(forms.ModelForm):

    class Meta:
        model = cafes_model
        fields = '__all__'
        widgets = {'informacion':forms.Textarea(
            attrs = {'class':'form__informacion','placeholder':'informacion'}
        )}
    


class brunch_form(forms.ModelForm):

    class Meta:
        model = brunch_model
        fields = '__all__'
        widgets = {'informacion':forms.Textarea(
            attrs = {'class':'form__informacion','placeholder':'informacion'}
        )}
    

       

class populares_form(forms.ModelForm):

    class Meta:
        model = populares_model
        fields = '__all__'
        widgets = {'informacion':forms.Textarea(
            attrs = {'class':'form__informacion','placeholder':'informacion'}
        )}
    