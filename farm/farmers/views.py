from django.shortcuts import render
from . models import Farmers
from . serializers import FarmersSerializer
from rest_framework import viewsets

# Create your views here.
def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')




def index(request):
    return render(request,'index.html')

def tasksPage(request):
    return render(request,'tasks-page.html')

def workersPage(request):
    return render(request,'workers-page.html')

class FarmersView(viewsets.ModelViewSet):
    queryset=Farmers.objects.all()
    serializer_class= FarmersSerializer
    