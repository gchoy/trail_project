from django.urls import path, include

from .views import dashboard

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('myaccount/', include('userprofile.urls')),
    path('', include('trail_app.urls')),
     
]
