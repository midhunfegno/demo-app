from datetime import datetime

from django.db import models

# Create your models here.

class contactdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=200,null=True,blank=True)

class delivereddb(models.Model):
    orderid = models.CharField(max_length=100, null=True, blank=True)
    Drivercode = models.CharField(max_length=100, blank=True, null=True)
    preferenceno=models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    date_of_delivery = models.DateTimeField(default=datetime.now, null=True, blank=True)
    invoiceno=models.CharField(max_length=200,null=True,blank=True)
    productcode=models.CharField(max_length=200,null=True,blank=True)
    custname=models.CharField(max_length=200,null=True,blank=True)
    shippingname=models.CharField(max_length=200,null=True,blank=True)
    district=models.CharField(max_length=200,null=True,blank=True)
    custaddress=models.CharField(max_length=200,null=True,blank=True)
    pincode=models.CharField(max_length=200,null=True,blank=True)
    custmob=models.CharField(max_length=200,null=True,blank=True)
    altmobno=models.CharField(max_length=200,null=True,blank=True)
    userid=models.CharField(max_length=20,null= True,blank=True)
class returndb(models.Model):
    orderid = models.CharField(max_length=100, null=True, blank=True)
    Drivercode = models.CharField(max_length=100, blank=True, null=True)
    preferenceno = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    date_of_return = models.DateTimeField(default=datetime.now, null=True, blank=True)
    invoiceno = models.CharField(max_length=200, null=True, blank=True)
    productcode = models.CharField(max_length=200, null=True, blank=True)
    custname = models.CharField(max_length=200, null=True, blank=True)
    shippingname = models.CharField(max_length=200, null=True, blank=True)
    district = models.CharField(max_length=200, null=True, blank=True)
    custaddress = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=200, null=True, blank=True)
    custmob = models.CharField(max_length=200, null=True, blank=True)
    altmobno = models.CharField(max_length=200, null=True, blank=True)
    userid = models.CharField(max_length=20, null=True, blank=True)
    reason = models.CharField(max_length=200, null=True, blank=True)