from rest_framework import serializers
from Employee.models import Employee

class Employeeserializer(serializers.Serializer):
	# serializer to represent Employee model
	class Meta:
		model = Employee
		fields = ("Empfname","Emplname","EmpDes","Hired_date")
