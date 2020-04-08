from django.contrib import admin
from .models import International,Domestic,Airport,Pilot,Crew,Flight,Passenger

admin.site.register(Airport)
admin.site.register(Passenger)
admin.site.register(Pilot)
admin.site.register(Crew)
admin.site.register(Flight)
admin.site.register(Domestic)
admin.site.register(International)




