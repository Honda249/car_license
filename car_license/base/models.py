from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CarDetails (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    make  = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    chassis = models.CharField(max_length=50, unique=True)
    eng_num = models.CharField(max_length=50, unique=True)
    year  = models.IntegerField()
    
class Reservation (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarDetails, on_delete=models.CASCADE)
    date = models.DateTimeField()


class UserInfo (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    national_id = models.CharField(max_length=50, unique=True)
    number = models.IntegerField(unique=True)
    address = models.CharField(unique=True, max_length=50)
