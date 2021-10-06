from django.shortcuts import render, redirect
from mysite.forms import EmployeeForm
from mysite.models import Employee
from django.http import HttpResponse
from .models import ToDoList, Item
# from mysite.tables import PersonTable

# def people(request):
#     people = PersonTable()
#     return render(request, "index.html", {'people': people})

# def index(response, id):
#     ls = ToDoList.objects.get(id=id)
#     return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {"name":"test"})

####table
def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
def index(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")