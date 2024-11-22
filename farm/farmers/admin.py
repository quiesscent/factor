from django.contrib import admin
from .models import Farmers, Tasks, Workers

# Register your models here.
admin.site.register(Farmers)
admin.site.register(Tasks)
admin.site.register(Workers)