from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class prediction_Of_crime_type(models.Model):


    FID= models.CharField(max_length=300)
    url= models.CharField(max_length=30000)
    length_url= models.CharField(max_length=300)
    length_hostname= models.CharField(max_length=300)
    Source_IP= models.CharField(max_length=300)
    Source_Port= models.CharField(max_length=300)
    Destination_IP= models.CharField(max_length=300)
    Destination_Port= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



