from django.contrib import admin

# Register your models here.
from .models import Patient, Appointment, Ward, MedicalStaff

admin.site.register(Patient)
admin.site.register(MedicalStaff)
admin.site.register(Appointment)
admin.site.register(Ward)

