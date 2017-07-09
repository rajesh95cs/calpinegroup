from django.shortcuts import render

from rest_framework import viewsets
from Employee.models import Employee
from Employee.employeeserializer import Employeeserializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Employee.objects.all()
    serializer_class = Employeeserializer
