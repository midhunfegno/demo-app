from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from DeliveroApp.models import driverregister, taskdb
from DeliveroSite.models import contactdb, delivereddb, returndb


def sitehomepage(request):
    return render(request,'webindex.html')
def driverlogin(request):
    return render(request,'userlogin.html')
def aboutpage(request):
    return render(request,'about.html')
def contactpage(request):
    return render(request,'contact.html')
def sendmessage(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Message=request.POST.get("message")
        obj=contactdb(name=Name,email=Email,message=Message)
        obj.save()
        return redirect(contactpage)
def logindriver(request):
    Username_d = request.POST.get('Username')
    Password_d = request.POST.get('Password')
    if driverregister.objects.filter(username=Username_d,password=Password_d).exists():
        driverid=driverregister.objects.filter(username=Username_d,password=Password_d).values('id').first()
        # request.session['Username']=Username_d
        request.session['Did'] = driverid['id']
        return redirect('sitehomepage')
    else:
        return redirect('driverlogin')
def driverlogout(request):
    del request.session['Did']
    return redirect('sitehomepage')

def viewdrivertasks(request):
    did=request.session['Did']
    data=taskdb.objects.filter(Drivercode=did,Status='Pending')
    return render(request, 'Driverviewtasks.html' ,{'data':data})

def viewtaskdet(request,taskid):
    data=taskdb.objects.filter(id=taskid)
    return render(request,'Viewtaskdetails.html',{'data':data})

def updatedelivered(request):
    if request.method == "POST":
        DriverCode = request.POST.get("Drivercode")
        Preferenceno = request.POST.get("Preferenceno")
        Orderid = request.POST.get("Orderid")
        Invoiceno = request.POST.get("Invoiceno")
        Custname = request.POST.get("Custname")
        Shippingname = request.POST.get("Shippingname")
        District = request.POST.get("District")
        Custaddress = request.POST.get("Custaddress")
        Pincode = request.POST.get("Pincode")
        Custmob = request.POST.get("Custmob")
        Altmobno = request.POST.get("Altmobno")
        user_id= request.POST.get("Userid")
        Productcode= request.POST.get("ProductCode")
        obj=delivereddb(status='Delivered',Drivercode=DriverCode,preferenceno=Preferenceno,orderid=Orderid,invoiceno=Invoiceno,custname=Custname,shippingname=Shippingname,district=District,custaddress=Custaddress,pincode=Pincode,custmob=Custmob,altmobno=Altmobno,userid=user_id,productcode=Productcode)
        obj.save()
        taskdb.objects.filter(Orderid=Orderid).update(Status='Delivered')
        did = request.session['Did']
        data = taskdb.objects.filter(Drivercode=did, Status='Pending')
    return render(request, 'Driverviewtasks.html', {'data': data})

def returndelivered(request,taskid):
    data = taskdb.objects.filter(id=taskid)
    return render(request,'Returndetails.html',{'data':data})

def approvereturn(request):
    if request.method == "POST":
        DriverCode = request.POST.get("Drivercode")
        print(DriverCode)
        Preferenceno = request.POST.get("Preferenceno")
        Orderid = request.POST.get("Orderid")
        Invoiceno = request.POST.get("Invoiceno")
        Custname = request.POST.get("Custname")
        Shippingname = request.POST.get("Shippingname")
        District = request.POST.get("District")
        Custaddress = request.POST.get("Custaddress")
        Pincode = request.POST.get("Pincode")
        Custmob = request.POST.get("Custmob")
        Altmobno = request.POST.get("Altmobno")
        user_id = request.POST.get("userid")
        Productcode = request.POST.get("Productcode")
        Reason = request.POST.get("Reason")
        obj = returndb(status='Returned',Drivercode=DriverCode,preferenceno=Preferenceno, orderid=Orderid, invoiceno=Invoiceno, custname=Custname,shippingname=Shippingname, district=District, custaddress=Custaddress, pincode=Pincode,custmob=Custmob, altmobno=Altmobno,userid=user_id,productcode=Productcode,reason=Reason)
        obj.save()
        taskdb.objects.filter(Orderid=Orderid).update(Status='Returned')
        did = request.session['Did']
        data = taskdb.objects.filter(Drivercode=did, Status='Pending')
        return render(request, 'Driverviewtasks.html',{'data':data})
