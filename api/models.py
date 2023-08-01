from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    owner_email = models.CharField(max_length=50)
    creator_email = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title +'--'+ self.description

#Employee Model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','manager'),
        ('Software Developer','sd'),
        ('Project Leader','pl')
    ))        
    
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    
    