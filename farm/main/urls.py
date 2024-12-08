from django.urls import path
from . import views

app_name="farmers"

urlpatterns = [
  path("",views.login, name="login"),
  path("register/",views.register, name="register"),
  path("home/", views.index, name="home"),
  path("tasksPage/", views.tasksPage, name="tasksPage"),
  path("workersPage/", views.workersPage, name="workersPage"),
  path("createWorkersPage/", views.createWorkersPage, name="createWorkersPage"),
  path("createTasksPage/", views.createTasksPage, name="createTasksPage"),
  path("editTask/<id>",views.editTask),
  path("deleteTask/<id>",views.deleteTask),
  path("editWorker/<id>",views.editWorker),
  path("deleteWorker/<id>",views.deleteWorker),
  path("contact/",views.contact, name="contact"),
  path("workerHome/",views.workerHome, name="workerHome"),
  path("workerTask/",views.workerTask, name="workerTask"),
  path("workerWorkers/", views.workerWorkers, name="workerWorkers"),
  path("supervisorHome/", views.supervisorHome, name="supervisorHome"),
  path("supervisorCreateTaskPage/",views.supervisorCreateTaskPage,name="supervisorCreateTaskPage"),
  path("supervisorTaskPage/",views.supervisorTaskPage,name="supervisorTaskPage"),
  path("supervisorWorkerPage/",views.supervisorWorkerPage, name="supervisorWorkerPage"),
  path("supervisorCreateWorkerPage/",views.supervisorCreateWorkerPage, name="supervisorCreateWorkerPage"),
  path("SupervisorProfilePage/", views.SupervisorProfilePage, name="SupervisorProfilePage"),
  path("MainProfilePage/", views.MainProfilePage, name="MainProfilePage"),
  path("WorkerProfilePage/", views.WorkerProfilePage, name="WorkerProfilePage"),
  path("MainProfileForm/",views.MainProfileForm, name="MainProfileForm"),
  path("SupervisorProfileForm/",views.SupervisorProfileForm, name="SupervisorProfileForm"),
  path("WorkerProfileForm/",views.WorkerProfileForm, name="WorkerProfileForm"),
  path("chartPage/", views.chartPage, name="chartPage"),
  path("MaininventoryTablePage/", views.MaininventoryTablePage, name="MaininventoryTablePage"),
]