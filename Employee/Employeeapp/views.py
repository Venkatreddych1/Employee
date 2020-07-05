from django.shortcuts import render
from .models import Employee
from .Serializers import EmployeeSerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


def home(request):
    return render(request,'employee.html')

def insert(request):
    empid1=request.POST['x1']
    name1= request.POST['x2']
    emp_num1=request.POST['x3']
    department1=request.POST['x4']
    E=Employee(empid=empid1,name=name1,emp_num=emp_num1,department=department1)
    E.save()
    return HttpResponse("Inserted successfully")

def display(request):
    dis=Employee.objects.all()
    return render(request,'display.html',{'records':dis})


class EmployeeList(APIView):
      def get(self,request,format=None):
          Employees=Employee.objects.all()
          Serializers= EmployeeSerializer(Employees,Many=True)
          return Response(Serializers.data)
      def post(self,request,format=None):
          serializer=EmployeeSerializer(data=request.POST)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors)


# def inputid(request):
  #  return render(request,'inputid.html')