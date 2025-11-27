from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    dateregistered = models.DateTimeField()
    dob = models.DateField()
    medicalHistory = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)

    def __str__(self):
        return self.fullname
    
class MedicalHistory(models.Model):
    patientname = models.CharField(max_length=50)
    doctor = models.CharField()
    diagnosis = models.TextField()
    visitdate = models.DateField()

    def __str__(self):
        return self.patientname

class Appointment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    department = models.CharField(max_length=20)
    doctors = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
