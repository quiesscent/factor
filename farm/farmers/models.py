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
    


class Tasks(models.model):
    name=models.CharField(max_length=100)
    role=models.EmailField()
    heading=models.CharField(max_length=100)
    description=models.CharField( max_length=100)
    days=models.IntegerField()