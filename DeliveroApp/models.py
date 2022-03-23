from datetime import datetime

from django.db import models

# Create your models here.


class adminregister(models.Model):
    names=models.CharField(max_length=100,null=True,blank=True)
    age=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=150,null=True,blank=True)
    email=models.CharField(max_length=40,null=True,blank=True)
    mobno=models.CharField(max_length=20,null=True,blank=True)
    username=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    photo=models.ImageField(upload_to="profile",null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)


class driverregister(models.Model):
    fname=models.CharField(max_length=100,null=True,blank=True)
    lname=models.CharField(max_length=100,null=True,blank=True)
    age=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=150,null=True,blank=True)
    email=models.CharField(max_length=40,null=True,blank=True)
    mobno=models.CharField(max_length=20,null=True,blank=True)
    username=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    photo=models.ImageField(upload_to="profile",null=True,blank=True)
    status=models.IntegerField(null=True,blank=True)
    userid=models.CharField(max_length=100, blank=True, null=True)


class taskdb(models.Model):
    Status=models.CharField(max_length=100, blank=True,null=True)
    # date_byorder= models.DateTimeField(default=datetime.now,null=True,blank=True)
    # status_updated_on=models.CharField(max_length=100, blank=True,null=True)
    # time=models.CharField(max_length=100, blank=True,null=True)
    # Created_by=models.CharField(max_length=100, blank=True,null=True)
    created_date=models.CharField(max_length = 20 ,default="0")
    Orderid = models.CharField(max_length=100, blank=True, null=True)
    Invoiceno=models.CharField(max_length=100, blank=True,null=True)
    Productcode=models.CharField(max_length=100, blank=True,null=True)
    Drivercode=models.CharField(max_length=100, blank=True,null=True)
    Custmob=models.CharField(max_length=100, blank=True,null=True)
    Custname=models.CharField(max_length=100, blank=True,null=True)
    Shippingname=models.CharField(max_length=100, blank=True,null=True)
    District=models.CharField(max_length=100, blank=True,null=True)
    Custaddress=models.CharField(max_length=100, blank=True,null=True)
    Pincode=models.CharField(max_length=100, blank=True,null=True)
    Altmobno=models.CharField(max_length=100, blank=True,null=True)
    Preferenceno = models.CharField(max_length=100, blank=True, null=True)
    Clientname = models.CharField(max_length=100, blank=True, null=True)
    userid=models.CharField(max_length=100, blank=True, null=True)
    # Lattitude = models.CharField(max_length=100, blank=True, null=True)
    # Longitude = models.CharField(max_length=100, blank=True, null=True)
    # POD_Type=models.CharField(max_length = 100 , null  = True ,  blank=True)
    # POD_Number=models.CharField(max_length = 100 , null  = True ,  blank=True)
    # comment=models.CharField(max_length = 500 , null  = True ,  blank=True)
    # additional_information=models.CharField(max_length = 500,null =True , blank=True)
    # userid=models.ForeignKey(admindb,on_delete=models.CASCADE,null=True,blank=True)
    # username=models.CharField(max_length=100, blank=True,null=True)


