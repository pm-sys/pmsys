from django.contrib import admin

# Register your models here.
from .models import Patient, Ward, MedicalStaff, Prescription

admin.site.register(MedicalStaff)
admin.site.register(Ward)
admin.site.register(Prescription)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_number', 'last_name', 'first_name')
    search_fields = ['patient_number']


admin.site.register(Patient, PatientAdmin)
