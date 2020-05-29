from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=250)
    location_address = models.CharField(max_length=250)
    public = models.BooleanField()
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Spot(models.Model):
    spot_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    spot_name = models.CharField(max_length=250)
    spot_public = models.BooleanField()
    spot_lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    spot_lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    spot_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.spot_name

class Trail(models.Model):
    trail_spot = models.ManyToManyField(Spot)
    trail_name = models.CharField(max_length=250)
    trail_public = models.BooleanField()
    trail_lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    trail_lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    trail_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.trail_name
