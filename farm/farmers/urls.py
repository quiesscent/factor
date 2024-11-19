from django.urls import path
from . import views

app_name="farmers"
urlpatterns = [
    path("",views.login, name="login"),
    path("home/", views.index, name="home")
]
