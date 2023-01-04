from django.contrib import admin
from emp_app import models
# Register your models here.
@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "dept", "salary", "bonus", "role", "phone", "hire_date"]
@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name","location"]
@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name",]
