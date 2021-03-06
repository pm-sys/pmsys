from django.db import models

# Create your models here.
# The Person Class
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0)
    email = models.CharField(max_length=200)

    def __str__(self):
        return  '{first} {last}'.format(first=self.first_name, last=self.last_name)

# The MedicalStaff class is a subclass of the Person class
class MedicalStaff(Person):
    employee_number = models.IntegerField(default=11111)
    login_password = models.CharField(max_length=20)

# The Ward Class
class Ward(models.Model):
    ward_id = models.AutoField(primary_key=True)
    ward_name = models.CharField(max_length=200, default='defaultward')
    # ForeginKey specifies associations
    # Instances of MedicalStaff are assigned to a Ward
    medical_staff = models.ForeignKey(MedicalStaff, on_delete=models.CASCADE, null=True)
    total_room = models.IntegerField(default=0)
    total_bed = models.IntegerField(default=0)

    def __str__(self):
        return  '{wardName}'.format(wardName=self.ward_name)

class Patient(Person):

    patient_number = models.AutoField(primary_key=True)
    insurance_number = models.IntegerField(default=0)
    reg_date = models.DateTimeField('date registered')
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('I', 'Intersex'),
        ('DtA', 'Decline to Answer'),
    )
    martial_status = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('DtA', 'Decline to Answer'),
    )
    ext_doctor_id = models.IntegerField(default=0)
    rationale = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    # ForeginKey specifies associations
    # Patients belong to a Ward
    ward = models.ForeignKey(Ward, null=True)

class Prescription(models.Model):
    # ForeginKey specifies associations
    # Prescriptions are associated with patients
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug_number = models.IntegerField(default=0)
    drug_name = models.CharField(max_length=200)
    units_by_day = models.IntegerField(default=0)
    number_of_administration_per_day = models.IntegerField(default=0)
    time_of_units_administered = models.TimeField('Time of administration')
    number_of_units_administered = models.IntegerField(default=0)
    method_of_administration = models.CharField(max_length=200)
    start_date = models.DateTimeField('Start date')
    finish_date = models.DateTimeField('Finish date')

    def __str__(self):
        return 'Prescription for {patient}.'.format(patient=str(self.patient))
