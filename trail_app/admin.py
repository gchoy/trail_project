from django.contrib import admin

from .models import Location, Spot, Trail

class LocationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Location, LocationAdmin)

class SpotAdmin(admin.ModelAdmin):
    pass
admin.site.register(Spot, SpotAdmin)

class TrailAdmin(admin.ModelAdmin):
    pass
admin.site.register(Trail, TrailAdmin)
