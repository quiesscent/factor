from django.contrib import admin
from .models import Farmer, Task, Worker

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Task)
admin.site.register(Worker)