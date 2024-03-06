from django.contrib import admin
from .models import PositionModel,EmployeeModel
# Register your models here.

admin.site.register(PositionModel)
admin.site.register(EmployeeModel)
