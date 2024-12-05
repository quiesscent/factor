from django.db import models
from authentication .models import CustomUser



# Create your models here.
class Farmer(models.Model):
    name=models.CharField( max_length=100)
    email=models.EmailField()
    username=models.CharField(max_length=100)
    password=models.CharField( max_length=50)
    phone=models.IntegerField()
    profession = models.CharField(max_length=100, null=True)
    image=models.ImageField( upload_to='images/')
    


class Task(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField( max_length=100)
    heading=models.CharField(max_length=100)
    description=models.CharField( max_length=100)
    days=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    

class Worker(models.Model):
       name=models.CharField(max_length=100)
       email=models.EmailField()
       phone=models.IntegerField()
       worktype=models.CharField( max_length=100)
       role=models.CharField( max_length=100)
       status=models.CharField( max_length=100)
       image=models.ImageField(upload_to='workerimages/')
       
       
       def __str__(self):
           return self.name
       
class Contact(models.Model):
    name=models.CharField( max_length=100)
    email=models.EmailField()
    role=models.CharField( max_length=100)
    workId=models.IntegerField()
    subject=models.CharField( max_length=100)
    message=models.CharField( max_length=100)
    image=models.ImageField( upload_to='contactimages/')
    
    def __str__(self):
        return self.name
    
    
class SupervisorProfile(models.Model):
        name=models.CharField( max_length=100)
        email=models.EmailField( max_length=100)
        role=models.CharField( max_length=100)
        phone=models.IntegerField()
        image=models.ImageField(upload_to='profileimages/')
        
        
        
        
class WorkerProfile(models.Model):
        name=models.CharField( max_length=100)
        email=models.EmailField( max_length=100)
        role=models.CharField( max_length=100)
        phone=models.IntegerField()
        image=models.ImageField(upload_to='profileimages/')
    

class AdminProfile(models.Model):
        name=models.CharField( max_length=100)
        email=models.EmailField( max_length=100)
        role=models.CharField( max_length=100)
        phone=models.IntegerField()
        image=models.ImageField(upload_to='profileimages/')

class SupervisorCreateworker(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    worktype=models.CharField( max_length=100)
    role=models.CharField( max_length=100)
    status=models.CharField( max_length=100)
    group=models.CharField( max_length=50)
    image=models.ImageField(upload_to='workerimages/')


def __str__(self):
    return self.name


class SupervisorCreatetask(models.Model):
    name=models.CharField(max_length=100)
    role=models.CharField( max_length=100)
    heading=models.CharField(max_length=100)
    description=models.CharField( max_length=100)
    days=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    