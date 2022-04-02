from datetime import datetime
from django.http import HttpRequest, HttpResponse

from django.shortcuts import render,HttpResponseRedirect

from . models import Employee, Role,Department
from .forms import  StudentEmployee,StudentRole,StudentDepartment
from django.db.models import Q

# Create your views here. 
def index(request):
    return render(request,"index.html")

def all_emp(request):
    emps = Employee.objects.all()
    print(emps)
    return render(request,"all_emp.html",{'emps':emps})

def add_emp(request):
    #fm=StudentEmployee()
    if request.method == 'POST':
        fm=StudentEmployee(request.POST)
        if fm.is_valid():
            first_name=fm.cleaned_data['first_name']
            last_name=fm.cleaned_data['last_name']
            dept=fm.cleaned_data['dept']
            salary=fm.cleaned_data['salary']
            bonus=fm.cleaned_data['bonus']
            role=fm.cleaned_data['role']
            phone=fm.cleaned_data['phone']



            hire_date=fm.cleaned_data['hire_date']
            reg = Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept=dept, role=role,hire_date=datetime.now())
            reg.save()

            
            print(first_name)

            return HttpResponseRedirect('/')
            #fm = StudentEmployee() 

       
        
    else:
        fm = StudentEmployee()
        print('ye get request se aaya hai')
    
    
    return render(request,"add_emp.html",{'form':fm})
    #return render(request,'shop/index.html',{'form':fm})

    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     salary = request.POST['salary']
    #     bonus = request.POST['bonus']
    #     phone = request.POST['phone']

    #     dept = request.POST['dept']
        
    #     role = request.POST['role']
    #     hire_date = request.POST['hire_date']
    #     em=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept=dept, role=role,hire_date=datetime.now())
    #     new_emp = Employee
    #     new_emp.save() 
    #     return render(request,'add_emp.html','form':em)
    #     return render(request,"add_emp.html",{'form':em})
    #     return HttpResponse('Employee added successfully')
    # elif request.method=='GET':
    #     return render(request,'add_emp.html')

        
    # else:
    #     return HttpResponse("An Exception occure! employee has not been added")


    #return render(request,"add_emp.html",'form':fm)
    
def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            removed=Employee.objects.get(id=emp_id)
            removed.delete()
            return HttpResponse('Employee remove successfully')
        except:
            return HttpResponse("please enter valid emp id")


    emps = Employee.objects.all()
    return render(request,"remove_emp.html",{'emps':emps})

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role =request.POST['role']
        emps = Employee.objects.all()
        print(name)
        print(dept)
        print(role) 
        if name:
            emps = emps.filter(Q(first_name__icontains = name)) #| Q(last_name__icontains = name)
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)
        return render(request,"all_emp.html",{'emps':emps})
    elif request.method == 'GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse('An Exception occured')

 