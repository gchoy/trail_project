from django.contrib import admin

from .models import Userprofile

class UserprofileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Userprofile, UserprofileAdmin)
