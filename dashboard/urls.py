from django.urls import path, include

from .views import dashboard #, mylocations, myspots, mytrails, mylocation_detail, myspot_detail, mytrail_detail
urlpatterns = [
    path('',dashboard, name='dashboard'),
    #path('mylocations', mylocations, name='mylocations'),
    #path('mylocations/<int:id>/', mylocation_detail, name='mylocation_detail'),
    #path('myspots', myspots, name='myspots'),
    #path('myspots/<int:id>/', myspot_detail, name='myspot_detail'),
    #path('mytrails', mytrails, name='mytrails'),
    #path('mytrails/<int:id>/', mytrail_detail, name='mytrail_detail'),
    path('myaccount/', include('userprofile.urls')),
    path('', include('trail_app.urls')),
     
]
