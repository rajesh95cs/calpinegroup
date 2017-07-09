from django.db import models
from django.utils import timezone                                #for date of joining 


class Employee(models.Model):
	Empfname   =   models.CharField(max_length=100)              	
	Emplname   =   models.CharField(max_length=100)              
    #Empid      =   models.CharField(max_length=10)               
    EmpDes     =   models.CharField(max_length=500)              
    Hired_date =   models.DateTimeField(default=timezone.now)    
    

