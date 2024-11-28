from django.shortcuts import render,redirect
from . models import Farmer, Task, Worker


# Create your views here.
def login(request):
    return render(request,'login/login.html')


def register(request):
    return render(request,'login/register.html')




def index(request):
    tasks=Task.objects.all()
    workers=Worker.objects.all()
    
    context={
        'tasks': tasks,
        'workers':workers
    }
    return render(request,'admin/index.html',context)


def workersPage(request):
    workers=Worker.objects.all()
    return render(request,'admin/workers-page.html',{'workers':workers})


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
    
    return render(request,'admin/create-workers.html')

def editWorker(request, id):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        role=request.POST['role']
        email=request.POST['email']
        worktype=request.POST['worktype']
        status=request.POST['status'].lower()
        image=request.FILES['image']
        
        
        workers=Worker.objects.get(id=id)
        
        workers.name = name
        workers.phone = phone
        workers.role = role
        workers.email = email
        workers.worktype = worktype
        workers.status = status
        workers.image = image
        
        workers.save()
        return redirect('/workersPage/')
    
    workers=Worker.objects.get(id=id)
    return render(request, 'admin/edit-worker.html',{'workers': workers})

def deleteWorker(request, id):
    workers=Worker.objects.get(id=id)
    workers.delete()
    return redirect('/workersPage/')

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
               
    return render(request,'admin/create-tasks.html')




def tasksPage(request):
    tasks=Task.objects.all()
    return render(request,'admin/tasks-page.html',{'tasks': tasks})

def editTask(request, id):
    if request.method=="POST":
        name = request.POST['name']
        role = request.POST['role']
        heading = request.POST['heading']
        description = request.POST['description']
        days = request.POST['days']

        tasks=Task.objects.get(id = id)

        tasks.name = name
        tasks.role = role
        tasks.heading = heading
        tasks.description = description
        tasks.days = days

        tasks.save()
        return redirect('/tasksPage/')
        
    tasks=Task.objects.get(id = id)
    return render(request, 'admin/edit-task.html',{'tasks': tasks})

def deleteTask(request, id):
    tasks=Task.objects.get(id=id)
    tasks.delete()
    
    return redirect('/tasksPage/')

    
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        role=request.POST['role']
        workId=request.POST['workId']
        subject=request.POST['subject']
        message=request.POST['message']
        image=request.POST['image']
        
        contact=Contact(name=name, email=email, role=role, workId=workId, subject=subject, message=message, image=image)
        contact.save()
    return render(request,'contact.html')