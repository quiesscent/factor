from django.db import models

# Create your models here.
class Farmers(models.Model):
    name=models.CharField( max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField( max_length=50)
    phone=models.IntegerField()
    profession = models.CharField(max_length=100, null=True)
    image=models.ImageField( upload_to='images/')
    


class Tasks(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField( max_length=100)
    heading=models.CharField(max_length=100)
    description=models.CharField( max_length=100)
    days=models.IntegerField()
    

class Workers(models.Model):
       name=models.CharField(max_length=100)
       email=models.EmailField()
       phone=models.IntegerField()
       workertype=models.CharField( max_length=100)
       role=models.CharField( max_length=100)
       status=models.CharField( max_length=100)
       image=models.ImageField(upload_to='workerimages/')
         
 
  