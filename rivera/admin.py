from django.contrib import admin
from . models import members,guest,EmployeeData

# Register your models here.
admin.site.register(members)
admin.site.register(guest)
admin.site.register(EmployeeData)