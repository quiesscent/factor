from django.shortcuts import render,redirect
from . models import Farmer, Task, Worker


# Create your views here.
def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')




def index(request):
    return render(request,'index.html')


def workersPage(request):
    workers=Worker.objects.all()
    return render(request,'workers-page.html',{'workers':workers})


def createWorkersPage(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        role=request.POST['role']
        email=request.POST['email']
        worktype=request.POST['worktype']
        status=request.POST['status'].lower()
        image=request.FILES['image']
        
        worker=Worker(name=name, phone=phone, role=role, email=email, worktype=worktype,status=status,image=image)
        worker.save()
        return redirect('/workersPage/')
    
    return render(request,'create-workers.html')

def createTasksPage(request):
    if request.method=="POST":
        name=request.POST['name']
        role=request.POST['role']
        heading=request.POST['heading']
        description=request.POST['description']
        days=request.POST['days']
        
        task=Task(name=name,role=role,heading=heading,description=description,days=days)
        task.save()
        return redirect('/tasksPage/')    
               
    return render(request,'create-tasks.html')


def tasksPage(request):
    tasks=Task.objects.all()
    return render(request,'tasks-page.html',{'tasks': tasks})

def editTask(request, id):
    return render(request, 'edit-task.html')

    