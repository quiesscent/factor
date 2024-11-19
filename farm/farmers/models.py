from django.db import models

# Create your models here.
class Farmers (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    username=models.CharField( max_length=50)
    password=models.CharField( max_length=50)
    
    

    

   

   