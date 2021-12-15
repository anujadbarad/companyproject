from django.db import models as m

class Employee(m.Model):
    Id =  m.BigAutoField(Primary_key=True)
    Employeename = m.CharField(max_length=500)
    Department = m.IntergerField(null=False)
    Email = m.CharField(max_length=250)
    DateOfBirth = m.DateField(null=False)
    Picture = m.CharField(max_length=1000)
    
    class Meta:
      db_table = 'Employee'
   
class Department(m.Model):
  Id =  m.BigAutoField(Primary_key=True)
  DepartmentName = m.CharField(max_length=500)
  Manager = m.IntergerField(null=True)
  
  class Meta:
      db_table = 'Department'
    
