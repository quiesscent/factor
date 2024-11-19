from django.db import models

# Create your models here.
class Farmers(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField()
    username=models.CharField(max_length=50)
    password=models.CharField( max_length=50)
    phone=models.IntegerField()
    image=models.ImageField( upload_to='images/')