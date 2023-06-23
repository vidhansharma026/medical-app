from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    mobile = models.BigIntegerField(unique=True, validators=[RegexValidator("^[0-9]{10}$")])
    password = models.CharField(max_length=255)  

class Doctor(models.Model):
    dname = models.CharField(max_length=20)
    specialist = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    image = models.ImageField(upload_to='doctor_img')

    def __str__(self):
        return self.dname

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallary_img')

class Appointment(models.Model):
    pname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField(validators=[RegexValidator("^[0-9]{10}$")])
    date = models.DateField()
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    department = models.ForeignKey(Doctor,on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.pname
    
class Msgs(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=20)
    msgs = models.TextField()

    def __str__(self):
        return self.subject
    
class Subscribe(models.Model):
    email = models.EmailField(max_length=30)
    def __str__(self):
        return self.email