from django.contrib import admin

# Register your models here.
from .models import Patient, Appointment, Ward, MedicalStaff

admin.site.register(MedicalStaff)
admin.site.register(Appointment)
admin.site.register(Ward)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('registration_number', 'last_name', 'first_name')
    search_fields = ['registration_number']


admin.site.register(Patient, PatientAdmin)
