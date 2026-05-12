from django.contrib import admin
from .models import Doctor,Patient,Appointments,Billing


# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointments)
admin.site.register(Billing)