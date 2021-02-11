from django import forms

from .models import Location, Spot, Trail


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'address', 'public', 'lon', 'lat',)

class SpotForm(forms.ModelForm):
    class Meta:
        model = Spot
        fields =('spot_location', 'spot_name', 'spot_on_trail', 'spot_public','spot_lon','spot_lat',)
        

class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = ('trail_location', 'trail_name','trail_public','trail_lon','trail_lat',)
        
