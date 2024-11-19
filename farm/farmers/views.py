from django.shortcuts import render
from . models import Farmers
from . serializers import FarmersSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request,'index.html')





class FarmersView(viewsets.ModelViewSet):
    queryset=Farmers.objects.all()
    serializer_class= FarmersSerializer
    