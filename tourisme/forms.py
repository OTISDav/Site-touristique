from django import  forms

from .models import *

class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketBus
        fields = '__all__'

class HebergementForm(forms.ModelForm):
    class Meta:
        model = Hebergement
        fields = '__all__'

class SiteTouristiqueForm(forms.ModelForm):
    class Meta:
        model = Sitetour
        fields = '__all__'

class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = '__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

