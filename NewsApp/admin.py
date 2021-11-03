from django.contrib import admin
from NewsApp.models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr',]


admin.site.register(Employee,EmployeeAdmin)
# admin.site.register(EmployeeAdmin)
