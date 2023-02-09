from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from StudentApp.models import City, Course, Student


# Create your views here.
def register_fun(request):
    return render(request,'register.html',{'data':''})


def regdata_fun(request):
    user_name=request.POST['txtUserName']
    user_email=request.POST['txtUserEmail']
    user_password=request.POST['txtUserPswd']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'register.html',{'data':'Username and Email is already exists'})
    else:
        u1=User.objects.create_superuser(username=user_name,email=user_email,password=user_password)
        u1.save()
        return redirect('log')


def log_fun(request):
    return render(request,'login.html',{'data':''})

def logdata_fun(request):
    user_name = request.POST['txtUserName']
    user_password = request.POST['txtUserPswd']
    user1 = authenticate(username=user_name,password=user_password)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not a superuser'})
    else:
        return render(request, 'login.html',{'data':'Enter proper username and password'})
    # if User.objects.filter(is_superuser=True).filter(username=user_name).exists():
    #     return render(request,'home.html',{'data':''})
    # else:
    #     return render(request,'login.html',{'data':'!!Account not exist!!'})


def home_fun(request):
    return render(request,'home.html')


def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request,'addstudent.html',{'City_Data':city,'Course_Data':course})


def readdata_fun(request):
    s1=Student()
    s1.Name=request.POST['txtName']
    s1.Age=request.POST['txtAge']
    s1.Phone_Num=request.POST['txtPhno']
    s1.City=City.objects.get(City_Name=request.POST['ddlCity'])
    s1.Course=Course.objects.get(Course_Name=request.POST['ddlCourse'])
    s1.save()
    return redirect('add')


def displaystudent_fun(request):
    d=Student.objects.all()
    return render(request,'displaystudent.html',{'data':d})


def update_fun(request,id):
    s=Student.objects.get(id=id)
    ct=City.objects.all()
    cs=Course.objects.all()
    if request.method == 'POST':
        s.Name = request.POST['txtName']
        s.Age = request.POST['txtAge']
        s.Phone_Num = request.POST['txtPhno']
        s.City = City.objects.get(City_Name=request.POST['ddlCity'])
        s.Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        s.save()
        return redirect('display')
    return render(request,'update.html',{'data':s,'City_Data':ct,'Course_Data':cs})


def delete_fun(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    return redirect('display')


def log_out_fun(request):
    return redirect('log')