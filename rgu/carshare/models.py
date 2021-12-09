from django.db import models
from django.db import IntegrityError, models, router, transaction

# Create your models here.

class Newuser(models.Model):
    FName=models.CharField(max_length=150)
    LName=models.CharField(max_length=150 ,default='')
    Residence=models.CharField(max_length=150, default='')
    Email=models.CharField(max_length=150)
    Pwd=models.CharField(max_length=150)
    RPwd=models.CharField(max_length=150 ,default='')
    Title=models.CharField(max_length=1)

class Payment(models.Model):
    CName=models.CharField(max_length=150)
    CNum=models.IntegerField()
    Expm=models.IntegerField()
    Expy=models.IntegerField()
    CVV=models.IntegerField()
    Tbill=models.IntegerField()

class Driver(models.Model):
    Firstname=models.CharField(max_length=150)
    Lastname=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Pass=models.CharField(max_length=150)
    Repass=models.CharField(max_length=150)
    Residence=models.CharField(max_length=150, default='')



   





