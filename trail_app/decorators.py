from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages
from .models import Location, Spot, Trail

def user_is_location_author(function):
    def wrap(request, *args, **kwargs):
        location = Location.objects.get(pk=kwargs['id'])
        
        
        if location.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            messages.info(request, "You cannot edit or delete another user's location")
            return redirect('dashboard')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap






def user_is_spot_author(function):
    def wrap(request, *args, **kwargs):
        
        spot = Spot.objects.get(pk=kwargs['id'])
        
        
        if spot.spot_by == request.user:
            return function(request, *args, **kwargs)
        else:
            messages.info(request, "You cannot edit or delete another user's spot")
            return redirect('dashboard')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def user_is_trail_author(function):
    def wrap(request, *args, **kwargs):
        
        trail = Trail.objects.get(pk=kwargs['id'])
        
        if trail.trail_by == request.user:
            return function(request, *args, **kwargs)
        else:
            messages.info(request, "You cannot edit or delete another user's trail")
            return redirect('dashboard')
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

