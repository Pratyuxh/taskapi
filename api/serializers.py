from api.models import Task, Employee
from rest_framework import serializers

class TaskSerializer(serializers.hyperlinkedModelSerializer):
    task_id=serializers.ReadOnlyField()
    class Meta:
        model = Task
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=Employee
        fields="__all__"