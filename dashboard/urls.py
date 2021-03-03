from django.urls import path, include

from .views import dashboard, mylocations, myspots, mytrails

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('mylocations', mylocations, name='mylocations'),
    path('myspots', myspots, name='myspots'),
    path('mytrails', mytrails, name='mytrails'),
    path('myaccount/', include('userprofile.urls')),
    path('', include('trail_app.urls')),
     
]
