from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CanteenEmployee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,default='')
    job = models.CharField(max_length=50)
    loginId = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
  
    def __str__(self):
        return self.first_name

class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100,default='',unique=True)
    username = models.CharField(max_length=10,unique=True,primary_key=True)
    password = models.CharField(max_length=15,unique=True)

    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.first_name +" "+self.last_name