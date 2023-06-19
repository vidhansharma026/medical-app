from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Login(models.Model):
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)

class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20, unique=True)
    mobile = models.BigIntegerField(unique=True, validators=[RegexValidator("^[0-9]{10}$")])
    password = models.CharField(max_length=20)  

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    specialist = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    image = models.ImageField(upload_to='doctor_img')

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallary_img')

class Appointment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    date = models.DateField()
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    information = models.TextField()

    def __str__(self):
        return self.name