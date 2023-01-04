from django.shortcuts import redirect, render,HttpResponse
from django.views import View
from . import models
from datetime import datetime
from django.db.models import Q
# Create your views here.
class index(View):
    template='index.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request,self.template,context)
class view_employee(View):
    template='view_employee.html'
    context={}
    def get(self,request):
        context=self.context
        context["view_emp"]=models.Person.objects.all()
        return render(request,self.template,context)
class add_employee(View):
    template='add_employee.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request,self.template,context)
    def post(self,request):
        print (request.POST)
        add=models.Person.objects.create(first_name = request.POST["first_name"],last_name = request.POST["last_name"],dept_id = request.POST["dept"],salary = request.POST["salary"],role_id = request.POST["role"],bonus = request.POST["bonus"],phone = request.POST["phone"] )
        add.save()
        return HttpResponse("Employee Added Successfully ")
class remove_employee(View):
    context={}
    template='remove_employee.html'
    def get(self,request,emp_id):
        print("emp_id",emp_id)
        if emp_id:
            try:
                emp_remove=models.Person.objects.get(id=emp_id)
                emp_remove.delete()
                HttpResponse("Employee Removed Successfully")
                
            except:
                HttpResponse("Enter A Valid Employee")
        context=self.context
        context['remove']=models.Person.objects.all()
        return render(request,self.template,context)
        

class filter_employee(View):
    template='filter_employee.html'
    temp='view_employee.html'
    context={}
    def get(self,request):
        context=self.context
        return render(request,self.template,context)
    def post(self,request):
        context=self.context
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=models.Person.objects.all()
        
        if name:
            context['temp']=emps.filter(Q(first_name__icontains = name) & Q(role__name__icontains = role) & Q(dept__name__icontains = dept))
            return render(request,self.temp,context)
        # if role:
        #     context['temp']=emps.filter(role__name__icontains = role)
        #     return render(request,self.temp,context)
        # if dept:
        #     context['temp']=emps.filter(dept__name__icontains = dept)
        #     return render(request,self.temp,context)
