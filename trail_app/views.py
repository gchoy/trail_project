from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import LocationForm, SpotForm, TrailForm 
from .models import Location, Spot, Trail


def locations_list(request):
    """List of Locations"""
 
    locations = list(Location.objects.all())

    return render(request,
                  'trail_app/locations_list.html',{'locations': locations})

def location_detail(request, id):
    """Location Detail"""
    
    location = get_object_or_404(Location, id=id)
    return render(request, 'trail_app/location_detail.html', {'location': location})



def add_location(request, Location):
    """Adding a new Location. Users are able to add a new location once signed in"""
    
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('location_detail'))
        else:
            return render(
                request,
                'trail_app/add_location.html',
                {'form': form})
                
    else:
        form = LocationForm() 
        return render(request,
                      'locations/add_location.html',
                      {'form': form})



