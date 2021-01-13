from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    Address_Line_1 = models.CharField(max_length=150)
    Address_Line_2 = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50)