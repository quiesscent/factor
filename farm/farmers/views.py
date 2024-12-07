from django.shortcuts import render,redirect
from . models import Farmer, Task, Worker, SupervisorCreatetask, SupervisorCreateworker,WorkerProfile,SupervisorProfile,MainProfile
from django.views.decorators.csrf import csrf_exempt
from authentication.models import CustomUser

#Admins Pages
# Create your views here.
def login(request):
    return render(request,'login/login.html')


def register(request):
    return render(request,'login/register.html')

@csrf_exempt
def index(request):
    tasks=Task.objects.all()
    workers=Worker.objects.all()
    supervisorworkers=SupervisorCreateworker.objects.all()
    supervisortasks=SupervisorCreatetask.objects.all()
    mainProfiles=MainProfile.objects.all()
    context={
        'tasks': tasks,
        'workers':workers,
        'supervisorworkers': supervisorworkers,
        'supervisortasks': supervisortasks,
        'mainProfiles': mainProfiles
    }
    return render(request,'main/index.html',context)


def workersPage(request):
    workers=Worker.objects.all()
    supervisorworkers=SupervisorCreateworker.objects.all()
    context={
        'workers':workers,
        'supervisorworkers':supervisorworkers
    }
    return render(request,'main/workers-page.html',context)


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
        create_user  = CustomUser.objects.create_user(username=name, email=email, user_type=role.lower(), password=email)
        create_user.save()
        worker.save()
        
        return redirect('/workersPage/')
    
    return render(request,'main/create-workers.html')

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
    return render(request, 'main/edit-worker.html',{'workers': workers})

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
               
    return render(request,'main/create-tasks.html')




def tasksPage(request):
    tasks=Task.objects.all()
    return render(request,'main/tasks-page.html',{'tasks': tasks})

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
    return render(request, 'main/edit-task.html',{'tasks': tasks})

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
    return render(request,'workers/contact.html')



#Workers pages
def workerHome(request):
    supervisorworker=SupervisorCreateworker.objects.all()
    supervisortask=SupervisorCreatetask.objects.all()
    workerProfiles=WorkerProfile.objects.all()
    context={
        'supervisorworker': supervisorworker,
        'supervisortask': supervisortask,
        'workerProfiles':workerProfiles
       
    }
    return render(request,'workers/worker-home.html',context)

def workerTask(request):
    tasks=Task.objects.all()
    return render(request,'workers/worker-task.html',{'tasks': tasks})

def workerWorkers(request):
    workers=Worker.objects.all()
    return render(request, 'workers/worker-workers.html',{'workers': workers})



def supervisorHome(request):
        supervisortask = SupervisorCreatetask.objects.all()
        supervisorworker = SupervisorCreateworker.objects.all()
        worker = Worker.objects.all()  
        supervisorProfiles=SupervisorProfile.objects.all()

        context = {
            'worker': worker,
            'supervisortask': supervisortask,
            'supervisorworker': supervisorworker,
            'supervisorProfiles':supervisorProfiles
            
        }
        return render(request, 'supervisor/home.html', context)



def supervisorCreateTaskPage(request):
    if request.method=="POST":
        name=request.POST['name']
        role=request.POST['role']
        heading=request.POST['heading']
        description=request.POST['description']
        days=request.POST['days']
      
        
        supervisortask=SupervisorCreatetask(name=name,role=role,heading=heading,description=description,days=days)
        supervisortask.save()
        return redirect('/supervisorTasksPage/')    
    
    return render(request,'supervisor/create-task.html')


def supervisorEditTaskPage(request,id):
    if request.method=="POST":
        name = request.POST['name']
        role = request.POST['role']
        heading = request.POST['heading']
        description = request.POST['description']
        days = request.POST['days']

        supervisortasks=SupervisorCreatetask.objects.get(id = id)

        supervisortasks.name = name
        supervisortasks.role = role
        supervisortasks.heading = heading
        supervisortasks.description = description
        supervisortasks.days = days

        supervisortasks.save()
        return redirect('/supervisorTasksPage/')
        
    supervisortasks=SupervisorCreatetask.objects.get(id = id)
    return render(request,'supervisor/edit-task.html')

def supervisorTaskDelete(request,id):
    supervisortasks=SupervisorCreatetask.objects.get(id = id)
    supervisortasks.delete()
    return redirect('/supervisorTaskPage/')

def supervisorTaskPage(request):
    supervisortask=SupervisorCreatetask.objects.all()
    return render(request, 'supervisor/task-page.html',{'supervisortask': supervisortask})



def supervisorCreateWorkerPage(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        role=request.POST['role']
        email=request.POST['email']
        worktype=request.POST['worktype']
        status=request.POST['status'].lower()
        image=request.FILES['image']
        group=request.POST['group']
        
        supervisorworker=SupervisorCreateworker(name=name, phone=phone, role=role, email=email, worktype=worktype,status=status,group=group,image=image)
        create_user  = CustomUser.objects.create_user(username=name, email=email, user_type=role.lower(), password=email)
        create_user.save()
        supervisorworker.save()
        
        return redirect('/supervisorWorkerPage/')
    return render(request, 'supervisor/create-worker.html')

def supervisorWorkerPage(request):
    supervisorworker=SupervisorCreateworker.objects.all()
    return render(request,'supervisor/worker.html',{'supervisorworker': supervisorworker})


def chartPage(request):
    return render(request, 'charts-chartjs.html')

def MaininventoryTablePage(request):
    return render(request,'main/inventory-table.html')

def MainProfileForm(request):
    if request.method=="POST":
        name=request.POST['name']
        role=request.POST['role']
        email=request.POST['email']
        phone=request.POST['phone']
        image=request.FILES['image']


        mainProfile=MainProfile(name=name,role=role,email=email,phone=phone,image=image)
        mainProfile.save()
        return redirect('/home/') 
    return render(request,'main/profile-form.html')

def MainProfilePage(request):
    mainProfiles=MainProfile.objects.all()
    context={
        'mainProfiles': mainProfiles
    }
    return render(request,'main/profile.html',context)


def SupervisorProfileForm(request):
    if request.method=="POST":
        name=request.POST['name']
        role=request.POST['role']
        email=request.POST['email']
        phone=request.POST['phone']
        image=request.FILES['image']


        supervisorProfile=SupervisorProfile(name=name,role=role,email=email,phone=phone,image=image)
        supervisorProfile.save()
        return redirect('/supervisorHome/') 
                        
    return render(request,'supervisor/profile-form.html')

def SupervisorProfilePage(request):
    supervisorProfiles=SupervisorProfile.objects.all()
    context={
        'supervisorProfiles':supervisorProfiles
    }
    return render(request,'supervisor/profile.html',context)

def WorkerProfileForm(request):
    if request.method=="POST":
        name=request.POST['name']
        role=request.POST['role']
        email=request.POST['email']
        phone=request.POST['phone']
        image=request.FILES['image']


        workerProfile=WorkerProfile(name=name,role=role,email=email,phone=phone,image=image)
        workerProfile.save()
        return redirect('/workerHome/') 
    
    return render(request,'workers/profile-form.html')



def WorkerProfilePage(request):
    workerProfiles=WorkerProfile.objects.all()
    context={
        'workerProfiles': workerProfiles
    }
    return render(request,'workers/profile.html',context)



