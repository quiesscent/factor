from django.shortcuts import render
from . models import Farmers, Tasks


# Create your views here.
def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')




def index(request):
    return render(request,'index.html')


def workersPage(request):
    return render(request,'workers-page.html')


def createWorkersPage(request):
    return render(request,'create-workers.html')

def createTasksPage(request):
    if request.method=="POST":
        name=request.POST['name']
        role=request.POST['role']
        heading=request.POST['heading']
        description=request.POST['description']
        days=request.POST['days']
        
        task=Tasks(name=name,role=role,heading=heading,description=description,days=days)
        task.save()
        return redirect('tasksPage/')    
               
    return render(request,'create-tasks.html')


def tasksPage(request):
    tasks=Tasks.objects.all()
    return render(request,'tasks-page.html',{'tasks': tasks})

    