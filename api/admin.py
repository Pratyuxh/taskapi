from django.contrib import admin
from api.models import Task, Employee

class TaskAdmin(admin.ModelAdmin):
    list_display=('title','description','priority')
    search_fields=('title',)   

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','task')
    list_filter=('task',)

admin.site.register(Task,TaskAdmin)
admin.site.register(Employee,EmployeeAdmin)