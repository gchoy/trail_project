from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from .forms import LocationForm, SpotForm, TrailForm 
from .models import Location, Spot, Trail

#Location views

def locations_list(request):
    """List of Locations"""
 
    locations = list(Location.objects.all())

    return render(request,
                  'trail_app/locations_list.html',{'locations': locations})

def location_detail(request, id):
    """Location Detail"""

    location = get_object_or_404(Location, id=id)
    return render(request, 'trail_app/location_detail.html', {'location': location})



def location_new(request):
    """Adding a new Location. Users are able to add a new location once signed in"""

    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            new_location = form.save()
            return redirect(reverse('location_detail', args=(new_location.id,)))
        else:
            return render(
                request,
                'trail_app/location_new.html',
                {'form': form})

    else:
        form = LocationForm() 
        return render(request,
                      'trail_app/location_new.html',
                      {'form': form})



def location_edit(request, id):
    location = get_object_or_404(Location, id=id)
    if request.method == "POST":
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            location = form.save(commit=False)
            location.address = form.data['address']
            if 'public' in form.data and form.data['public'] == 'on':
                location.public = True
            else:
                location.public = False

            location.lat = form.data['lat']
            location.lon = form.data['lon']
            location.save()
            return HttpResponseRedirect(reverse('location_edit', args=(location.id,)))
    else:
        form = LocationForm(instance=location)
    return render(request, 'trail_app/location_edit.html', {'location': location, 'form': form})


#Spot views

def spots_list(request):
    """List of Spots"""
 
    spots = list(Spot.objects.all())

    return render(request,
                  'trail_app/spots_list.html',{'spots': spots})

def spot_detail(request, id):
    """Spot Detail"""

    spot = get_object_or_404(Spot, id=id)
    return render(request, 'trail_app/spot_detail.html', {'spot': spot})



def spot_new(request):
    """Adding a new Spot. Users are able to add a new spot once signed in"""

    if request.method == "POST":
        form = SpotForm(request.POST)
        if form.is_valid():
            new_spot = form.save()
            return redirect(reverse('spot_detail', args=(new_spot.id,)))
        else:
            return render(
                request,
                'trail_app/spot_new.html',
                {'form': form})

    else:
        form = SpotForm() 
        return render(request,
                      'trail_app/spot_new.html',
                      {'form': form})


def spot_edit(request, id):
    spot = get_object_or_404(Spot, id=id)
    if request.method == "POST":
        form = SpotForm(request.POST, instance=spot)
        if form.is_valid():
            spot = form.save(commit=False)
            spot.location = form.data['spot_location']
            spot.name = form.data['spot_name']
            if 'spot_public' in form.data and form.data['spot_public'] == 'on':
                spot.public = True
            else:
                spot.public = False

            spot.lat = form.data['spot_lat']
            spot.lon = form.data['spot_lon']
            spot.save()
            return HttpResponseRedirect(reverse('spot_edit', args=(spot.id,)))
    else:
        form = SpotForm(instance=spot)
    return render(request, 'trail_app/spot_edit.html', {'spot': spot, 'form': form})



#Trails views

def trails_list(request):
    """List of Trails"""
 
    trails = list(Trail.objects.all())

    return render(request,
                  'trail_app/trails_list.html',{'trails': trails})

def trail_detail(request, id):
    """Trail Detail"""

    trail = get_object_or_404(Trail, id=id)
    return render(request, 'trail_app/trail_detail.html', {'trail': trail})



def trail_new(request):
    """Adding a new Trail. Users are able to create trails once signed in"""

    if request.method == "POST":
        form = TrailForm(request.POST)
        if form.is_valid():
            new_trail = form.save()
            return redirect(reverse('trail_detail', args=(new_trail.id,)))
        else:
            return render(
                request,
                'trail_app/trail_new.html',
                {'form': form})

    else:
        form = TrailForm() 
        return render(request,
                      'trail_app/trail_new.html',
                      {'form': form})


#fields = ('trail_spot', 'trail_location', 'trail_name','trail_public','trail_lon','trail_lat',)

def trail_edit(request, id):
    trail = get_object_or_404(Trail, id=id)
    if request.method == "POST":
        form = TrailForm(request.POST, instance=trail)
        if form.is_valid():
            trail = form.save(commit=False)
            trail.spot = form.data['trail_spot']
            trail.location = form.data['trail_location']
            trail.name = form.data['trail_name']

            if 'trail_public' in form.data and form.data['trail_public'] == 'on':
                trail.public = True
            else:
                trail.public = False

            trail.lat = form.data['trail_lat']
            trail.lon = form.data['trail_lon']
            trail.save()
            return HttpResponseRedirect(reverse('trail_edit', args=(trail.id,)))
    else:
        form = TrailForm(instance=trail)
    return render(request, 'trail_app/trail_edit.html', {'trail': trail, 'form': form})



