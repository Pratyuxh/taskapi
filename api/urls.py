from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from api.views import TaskViewSet, EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
