from django.urls import path
from . import views

app_name="farmers"
urlpatterns = [
    path("",views.login, name="login"),
      path("register/",views.register, name="register"),
    path("home/", views.index, name="home"),
     path("tasksPage/", views.tasksPage, name="tasksPage"),
       path("workersPage/", views.workersPage, name="workersPage"),
       path("createWorkersPage/", views.createWorkersPage, name="createWorkersPage")
]
