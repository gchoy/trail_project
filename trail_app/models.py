from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    public = models.BooleanField()
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Spot(models.Model):
    spot_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    spot_name = models.CharField(max_length=250)
    spot_public = models.BooleanField()
    spot_lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    spot_lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    spot_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.spot_name



class Trail(models.Model):
    trail_location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    trail_name = models.CharField(max_length=250)
    trail_spots = models.ManyToManyField(Spot, blank=True)
    trail_public = models.BooleanField()
    trail_lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    trail_lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    trail_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.trail_name

    """def trail_spot_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(lst.join(','))"""



        
class Trail_Group(models.Model):
    tg_name=models.CharField(max_length=250)
    tg_trail = models.ForeignKey(Trail, on_delete=models.CASCADE, blank=True, null=True)
    tg_start = models.OneToOneField(Location, unique=True,on_delete=models.CASCADE, blank=True, null=True,related_name='tg_start')
    
    tg_start_lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    tg_start_lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    tg_end = models.OneToOneField(Location, unique=True,on_delete=models.CASCADE, blank=True, null=True,related_name='tg_end')
    
    tg_end_lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    tg_end_lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    tg_public = models.BooleanField() 
    tg_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.tg_name
