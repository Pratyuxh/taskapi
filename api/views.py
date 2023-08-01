from django.shortcuts import render
from rest_framework import viewsets
from api.models import Task, Employee
from api.serializers import TaskSerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    #task/{taskId}/emplyees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            task=Task.objects.get(pk=pk)
            emps=Employee.objects.filter(task=task)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer