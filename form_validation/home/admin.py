from django.contrib import admin

# Register your models here
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('ename',)  # Add 'ename' to display in admin

admin.site.register(Employee, EmployeeAdmin)