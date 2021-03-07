from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from trail_app.models import Location, Spot, Trail


def dashboard(request):
    
    return render(request, 'dashboard/dashboard.html',{'hello': 'hello world'})


#Location views
@login_required
def mylocations(request):
    """List of Locations"""
    
    mylocations = Location.objects.filter(created_by=request.user)
    return render(request,
                  'dashboard/my_locations.html',{'mylocations': mylocations})

@login_required
def mylocation_detail(request, id):
    """Location Detail"""
    mylocation = get_object_or_404(Location, id=id)
    myspots_on_location = Spot.objects.filter(spot_location=id).filter(spot_by=request.user)
    mytrails_on_location = Trail.objects.filter(trail_location=id).filter(trail_by=request.user)
     
    return render(request, 'dashboard/mylocation_detail.html', {'mylocation': mylocation, 'myspots_on_location': myspots_on_location, 'mytrails_on_location': mytrails_on_location})
    


#Spot views

@login_required
def myspots(request):
    """List of Spots"""
 
    myspots= Spot.objects.filter(spot_by=request.user)
    return render(request,
                  'dashboard/my_spots.html',{'myspots': myspots})

@login_required
def myspot_detail(request, id):
    """Spot Detail"""

    myspot = get_object_or_404(Spot, id=id)
    mytrails = myspot.trail_set.filter(trail_by=request.user)
    
    return render(request, 'dashboard/myspot_detail.html', {'myspot': myspot, 'mytrails':mytrails})

#Trails views
@login_required
def mytrails(request):
    """List of Trails"""
  
    mytrails = Trail.objects.filter(trail_by=request.user)
    return render(request,
                  'dashboard/my_trails.html',{'mytrails': mytrails})

@login_required
def mytrail_detail(request, id):
    """Trail Detail"""

    mytrail = get_object_or_404(Trail, id=id)
    myspots = mytrail.trail_spots.all()
    #myspots = mytrail.trail_spots.filter(spot_by=request.user)
    return render(request, 'dashboard/mytrail_detail.html', {'mytrail': mytrail, 'myspots': myspots})


            


                               
