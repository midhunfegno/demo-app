from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from DeliveroApp.models import adminregister, driverregister ,taskdb

from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt

import pandas as pd
import numpy as np
from datetime import datetime

# Create your views here.
from DeliveroSite.models import contactdb, delivereddb, returndb

def homepage(request):
    fid = request.session['uid']
    if fid == "0":
        driver = driverregister.objects.all().count()
        tasks=taskdb.objects.all().count()
        delivered=delivereddb.objects.all().count()
        returned=returndb.objects.all().count()
        return render(request, 'index.html',{'driver': driver, 'tasks': tasks, 'delivered': delivered, 'returned': returned})
    else:
        driver = driverregister.objects.filter(userid=fid).count()
        tasks = taskdb.objects.filter(userid=fid).count()
        delivered = delivereddb.objects.filter(userid=fid).count()
        returned = returndb.objects.filter(userid=fid).count()
        return render(request,'index.html',{'driver':driver,'tasks':tasks,'delivered':delivered,'returned':returned})
def loginpage(request):
    return render(request,'login.html')
def adminregist(request):
    return render(request,'Add_Admin.html')
def saveregister(request):
    if request.method == "POST":
        Nname=request.POST.get("Name")
        Age=request.POST.get("Age")
        Address=request.POST.get("Address")
        Email=request.POST.get("Email")
        if adminregister.objects.filter(email=Email).exists():
            return HttpResponse("Email already exists....")
        Mobno=request.POST.get("Mobno")
        Username=request.POST.get("Username")
        if adminregister.objects.filter(username=Username).exists():
            return HttpResponse("Username already exists....")
        Password=request.POST.get("Password")
        Photo=request.FILES['Photo']
        obj=adminregister(names=Nname,age=Age,address=Address,email=Email,mobno=Mobno,username=Username,password=Password,photo=Photo)
        obj.save()
        return redirect(adminregist)
def admindisplay(request):
    data=adminregister.objects.all()
    return render(request, 'viewadminregister.html',{'data':data})
def editadmin(request,dataid):
    data=adminregister.objects.get(id=dataid)
    print(data)
    return render(request, 'editadminregister.html',{'data':data})

def updateadmin(request,dataid):
    if request.method=="POST":
        Nname = request.POST.get("Name")
        Age = request.POST.get("Age")
        Address = request.POST.get("Address")
        Email = request.POST.get("Email")
        if driverregister.objects.filter(email=Email).exists():
            return HttpResponse("Email already exists....")
        Mobno = request.POST.get("Mobno")
        Username = request.POST.get("Username")
        if driverregister.objects.filter(username=Username).exists():
            return HttpResponse("Username already exists....")
        Password = request.POST.get("Password")
        try:
            Photo=request.FILES['Photo']
            fs=FileSystemStorage()
            file=fs.save('Photo', Photo)
        except MultiValueDictKeyError:
            file=adminregister.objects.get(id=dataid).photo
        adminregister.objects.filter(id=dataid).update(names=Nname,age=Age,address=Address,email=Email,mobno=Mobno,username=Username,password=Password,photo=file)
    return redirect(admindisplay)

def deleteadmin(request, dataid):
    data=adminregister.objects.filter(id=dataid)
    data.delete()
    return redirect(admindisplay)

def driverregist(request):
    return render(request,'AddDriver.html')

def savedriverreg(request):
    if request.method == "POST":
        fid = request.session['uid']
        Fname=request.POST.get("Fname")
        Lname=request.POST.get("Lname")
        Age=request.POST.get("Age")
        Address=request.POST.get("Address")
        Email=request.POST.get("Email")
        if adminregister.objects.filter(email=Email).exists():
            return HttpResponse("Email already exists....")
        Mobno=request.POST.get("Mobno")
        Username=request.POST.get("Username")
        Password=request.POST.get("Password")
        Photo=request.FILES['Photo']
        obj=driverregister(fname=Fname,lname=Lname,age=Age,address=Address,email=Email,mobno=Mobno,username=Username,password=Password,photo=Photo,userid=fid)
        obj.save()
        return redirect(driverregist)

def driverdisplay(request):
    fid = request.session['uid']
    if fid == "0":
        data=driverregister.objects.all()
        return render(request, 'viewdriverregister.html',{'data':data})
    else:
        data = driverregister.objects.filter(userid=fid)
        return render(request, 'viewdriverregister.html', {'data': data})


def editdriver(request,dataid):
    data=driverregister.objects.get(id=dataid)
    print(data)
    return render(request, 'editdriverregister.html',{'data':data})

def updatedriver(request,dataid):
    if request.method=="POST":
        Fname = request.POST.get("Fname")
        Lname = request.POST.get("Lname")
        Age = request.POST.get("Age")
        Address = request.POST.get("Address")
        Email = request.POST.get("Email")
        Mobno = request.POST.get("Mobno")
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        try:
            Photo=request.FILES['Photo']
            fs=FileSystemStorage()
            file=fs.save('Photo', Photo)
        except MultiValueDictKeyError:
            file=driverregister.objects.get(id=dataid).photo
            driverregister.objects.filter(id=dataid).update(fname=Fname,lname=Lname,age=Age,address=Address,email=Email,mobno=Mobno,username=Username,password=Password,photo=file)
    return redirect(driverdisplay)

def deletedriver(request, dataid):
    data=driverregister.objects.filter(id=dataid)
    data.delete()
    return redirect(driverdisplay)

def adminlogin(request):
    Username_m=request.POST.get('Username')
    Password_m=request.POST.get('Password')
    if User.objects.filter(username__contains=Username_m).exists():
        user = authenticate(username=Username_m, password=Password_m)
        if user is not None:
            login(request,user)
            request.session['Username'] = Username_m
            request.session['Password'] = Password_m
            request.session['uid'] = '0'
            print(user)
            return redirect('homepage')
        else:
            return HttpResponse()

            # return render(request, 'login.html',{'msg':"Invalid username or password"})
    else:
        if adminregister.objects.filter(username__contains=Username_m, password=Password_m).exists():
            request.session['Username'] = Username_m
            request.session['Password'] = Password_m
            userid = adminregister.objects.filter(username=Username_m, password=Password_m).values('id').first()
            request.session['uid'] = userid['id']
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'msg': "Invalid username or password"})

def logout(request):
    del request.session['Username']
    del request.session['Password']
    del request.session['uid']
    return redirect('loginpage')

def addtasks(request):
    return render(request,'AddTask.html')

def taskadd(request):
    if request.method=='POST':
        tsk=request.FILES['Task']
        Uid=request.session.get('uid')
        print(tsk)
        df=pd.read_excel(tsk)
        print(df)
        tarray=np.array(df)
        for ch in tarray:
            db=taskdb(
            Status='Pending',
            created_date=datetime.today().strftime('%m/%d/%Y'),
            Orderid=ch[0],
            Invoiceno=ch[1],
            Productcode=ch[2],
            Drivercode=ch[3],
            Custmob=ch[4],
            Custname =ch[5],
            Shippingname=ch[6],
            District=ch[7],
            Custaddress=ch[8],
            Pincode=ch[9],
            Altmobno=ch[10],
            Clientname=ch[11],
            Preferenceno=ch[12],
            # Lattitude=ch[13],
            # Longitude=ch[14],
            userid=Uid)
            db.save()
        return redirect('addtasks')

def viewtask(request):
    fid = request.session['uid']
    if fid == "0":
        data = taskdb.objects.filter(Status='Pending')
        driver1 = driverregister.objects.all()
        return render(request, 'ViewTasks.html', {'data': data, 'driver1': driver1})
    else:
        data = taskdb.objects.filter(userid=fid, Status='Pending')
        driver1 = driverregister.objects.filter(userid=fid)
        return render(request, 'ViewTasks.html', {'data': data, 'driver1': driver1})
    return render(request,'ViewTasks.html')
def viewmoretask(request,dataid):
    data=taskdb.objects.filter(id=dataid)
    return render(request,'viewmoretask.html',{'data':data})

def deletetask(request,dataid):
    taskdb.objects.filter(id=dataid).delete()
    return redirect('viewtask')

def change_preferencenumber(request):

    if request.method == 'POST':
        id_r = request.POST.get('edittaskid1')
        print(id_r)
        preferenceNumber_r = request.POST.get('Preference_Number')
        print("the value id_r",id_r)
        if taskdb.objects.filter(id=id_r).exists():
           taskdb.objects.filter(id=id_r).update(Preferenceno=preferenceNumber_r)
           return redirect('viewtask')
        else :
           return redirect('viewtask')

def messagedisplay(request):
    data=contactdb.objects.all()
    return render(request, 'messages.html',{'data':data})

@csrf_exempt
def Edit_drivercode(request):
    data={}
    if request.method == 'POST':
        id_r = request.POST.get('id')
        print(id_r)
        driverCode_r = request.POST.get('driverCode')
        print(driverCode_r)
        if taskdb.objects.filter(id=id_r).update(Drivercode=driverCode_r):
           taskdb.objects.filter(id=id_r).update(Drivercode=driverCode_r)
           data['status']  = 1
           data['message'] = "Successfully updated"
           return JsonResponse(data)
        else :
           data['status']  = 0
           data['message'] = "Failed to update"
           return JsonResponse(data)

def displaydelivered(request):
    fid = request.session['uid']
    if fid == "0":
        data=delivereddb.objects.all()
        return render(request, 'Viewdelivered.html', {'data': data})
    else:
        data = delivereddb.objects.filter(userid=fid)
        return render(request, 'Viewdelivered.html', {'data': data})

def displayreturned(request):
    fid = request.session['uid']
    if fid == "0":
        data = returndb.objects.all()
        return render(request, 'Viewreturned.html', {'data': data})
    else:
        data = returndb.objects.filter(userid=fid)
        return render(request, 'Viewreturned.html', {'data': data})