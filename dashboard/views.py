from django.shortcuts import render, redirect, reverse
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


#Spot views

@login_required
def myspots(request):
    """List of Spots"""
 
    myspots= Spot.objects.filter(spot_by=request.user)
    return render(request,
                  'dashboard/my_spots.html',{'myspots': myspots})

#Trails views
@login_required
def mytrails(request):
    """List of Trails"""
  
    mytrails = Trail.objects.filter(trail_by=request.user)
    return render(request,
                  'dashboard/my_trails.html',{'mytrails': mytrails})

            


                               
