from django import forms

from .models import Location, Spot, Trail


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'address', 'public', 'lon', 'lat',)

class SpotForm(forms.ModelForm):
    pass

class TrailForm(forms.ModelForm):
    pass
