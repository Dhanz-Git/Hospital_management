from django.db import models
# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    def __str__(self):
        return self.name
class Patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    address=models.TextField()
    def __str__(self):
        return self.name
class Appointments(models.Model):
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    Appointment_fees = models.DecimalField(max_digits=100,decimal_places=2)
    #def __str__(self):
        #return 'hi'
class Billing(models.Model):
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Consulting_Time = models.TimeField(null=True,blank=True)
    Consulting_Date = models.DateField(null=True,blank=True)
    Medcine_name = models.CharField(max_length=100)
    Medicine_Amount = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.medicine