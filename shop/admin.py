from django.contrib import admin

#from oms.shop.models import Department, Employee, Role
from . models import Employee,Department,Role
# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Role)

