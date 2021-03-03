from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import LocationForm, SpotForm, TrailForm 
from .models import Location, Spot, Trail

import datetime

#Frontpage view
def frontpage(request):
    return render (request, 'frontpage.html')



#Location views
@login_required
def locations_list(request):
    """List of Locations"""
 
    locations = list(Location.objects.filter(public='True'))

    return render(request,
                  'trail_app/locations_list.html',{'locations': locations})

@login_required
def location_detail(request, id):
    """Location Detail"""
    location = get_object_or_404(Location, id=id)
    spots_on_location = Spot.objects.filter(spot_location=id).filter(spot_public='True')
    trails_on_location = Trail.objects.filter(trail_location=id).filter(trail_public='True')
     
    return render(
          request,
          'trail_app/location_detail.html', 
          {'location': location, 'spots_on_location': spots_on_location, 'trails_on_location': trails_on_location})
    



@login_required
def location_new(request):
    """Adding a new Location. Users are able to add a new location once signed in"""

    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            name = form.data['name']
            address = form.data['address']
            lat = form.data['lat']
            lon = form.data['lon']
            user =  request.user
            new_location = Location()
            new_location.name = name
            new_location.address = address

            if 'public' in form.data and form.data['public'] == 'on':
                new_location.public = True
            else:
                new_location.public = False

            new_location.lat = lat
            new_location.lon = lon
            new_location.date = datetime.datetime.now()
            new_location.created_by = user
            new_location.save()
 
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


@login_required
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

@login_required
def spots_list(request):
    """List of Spots"""
 
    spots = list(Spot.objects.filter(spot_public='True'))

    return render(request,
                  'trail_app/spots_list.html',{'spots': spots})
@login_required
def spot_detail(request, id):
    """Spot Detail"""

    spot = get_object_or_404(Spot, id=id)
    trails = spot.trail_set.filter(trail_public='True')
    
    return render(request, 'trail_app/spot_detail.html', {'spot': spot, 'trails':trails})


@login_required
def spot_new(request):
    """Adding a new Spot. Users are able to add a new spot once signed in"""

    if request.method == "POST":
        form = SpotForm(request.POST)
        
        if form.is_valid():
            spot_location = form.cleaned_data['spot_location']
            spot_name = form.cleaned_data['spot_name']
            spot_lat = form.data['spot_lat']
            spot_lon = form.data['spot_lon']
            user =  request.user
            new_spot = Spot()
            new_spot.spot_location = spot_location 
            new_spot.spot_name = spot_name

            if 'public' in form.data and form.data['spot_public'] == 'on':
                new_spot.spot_public = True
            else:
                new_spot.spot_public = False

            new_spot.spot_lat = spot_lat
            new_spot.spot_lon = spot_lon
            new_spot.spot_date = datetime.datetime.now()
            new_spot.spot_by = user
            new_spot.save()

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

@login_required
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
@login_required
def trails_list(request):
    """List of Trails"""
  
    trails = list(Trail.objects.filter(trail_public='True'))

    return render(request,
                  'trail_app/trails_list.html',{'trails': trails})
@login_required
def trail_detail(request, id):
    """Trail Detail"""

    trail = get_object_or_404(Trail, id=id)
    spots = trail.trail_spots.filter(spot_public='True')
    
    return render(request, 'trail_app/trail_detail.html', {'trail': trail, 'spots':spots})


@login_required
def trail_new(request):
    """Adding a new Trail. Users are able to create trails once signed in"""
    
    if request.method == "POST":
        form = TrailForm(request.POST)
        if form.is_valid():
            trail = form.save(commit=False)
            trail.location = form.cleaned_data['trail_location']
            trail.name = form.cleaned_data['trail_name']
            trail.spots = form.data['trail_spots']
            trail.lat = form.data['trail_lat']
            trail.lon = form.data['trail_lon']
            user =  request.user

            if 'public' in form.data and form.data['trail_public'] == 'on':
                trail.public = True
            else:
                trail.public = False

            trail.trail_date = datetime.datetime.now()
            trail.trail_by = request.user
            trail.save()
            return redirect(reverse('trail_detail', args=(trail.id,)))
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


@login_required
def trail_edit(request, id):
    trail = get_object_or_404(Trail, id=id)
    if request.method == "POST":
        form = TrailForm(request.POST, instance=trail)
        if form.is_valid():
            trail = form.save(commit=False)
            trail.spots = form.data['trail_spots']
            trail.location = form.data['trail_location']
            trail.name = form.data['trail_name']

            if 'trail_public' in form.data and form.data['trail_public'] == 'on':
                trail.public = True
            else:
                trail.public = False

            trail.lat = form.data['trail_lat']
            trail.lon = form.data['trail_lon']
            trail.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('trail_edit', args=(trail.id,)))
    else:
        form = TrailForm(instance=trail)
    return render(request, 'trail_app/trail_edit.html', {'trail': trail, 'form': form})



