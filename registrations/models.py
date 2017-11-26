from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=0)
    email = models.CharField(max_length=200)

    def __str__(self):
        return  '{first} {last}'.format(first=self.first_name, last=self.last_name)

class Patient(Person):
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

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    apt_date = models.DateTimeField('appointment date')
    location = models.CharField(max_length=200)
    in_doctor_id = models.IntegerField(default=0)

    def __str__(self):
        return 'Appointment for {patient} with Doctor ID: {doctor} at {date}.'.format(patient=str(self.patient), doctor=str(self.in_doctor_id), date=str(self.apt_date))
