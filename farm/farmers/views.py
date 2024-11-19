from django.shortcuts import render
from . models import Farmers
from .  serializers import FarmersSerializer
from rest_framework import viewsets

# Create your views here.
class FarmersView(viewsets.ModelViewSet):
    queryset=Farmers.object.all()
    serializer_class=FarmersSerializer
