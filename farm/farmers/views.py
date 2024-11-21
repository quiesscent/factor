from django.shortcuts import render
from . models import Farmers


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


def createWorkersPage(request):
    return render(request,'create-workers.html')




    