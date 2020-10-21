from django.db import models

# Create your models here.
class Updates(models.Model) :
    s_no = models.AutoField(primary_key=True)
    Topic=models.CharField(max_length=50,default="")
    Content=models.TextField(max_length=500,default="")
    Upload_date=models.DateField(null=True,blank=True)
    upload_time=models.TimeField(null=True,blank=True)
    datetime=models.DateTimeField(null=True,blank=True)

class MyCustomer(models.Model) :
    s_no= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30,default="")
    Email=models.CharField(max_length=40,default="")
    Address=models.CharField(max_length=20,default="")
    City=models.CharField(max_length=20,default="")
    State=models.CharField(max_length=20,default="")
    Number=models.IntegerField(default=0)
    Profile=models.ImageField(upload_to="customer/",default="customer/simple.jpg",max_length=255)
    Lonas=models.CharField(max_length=30,default="")
    last_seen=models.DateField(null=True,blank=True)
    Time=models.TimeField(null=True,blank=True)
    mes=models.SmallIntegerField(max_length=3,default=0)
    Feedback=models.TextField(max_length=300,default="")
    DateTime=models.DateTimeField(null=True,blank=True)
    def __str__(self) :
        return self.Name


class HomeLoan(models.Model) :
    loan_id= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30,default="")
    Email=models.CharField(max_length=40,default="")
    Gender=models.CharField(max_length=10,default="")
    Graduate=models.CharField(max_length=10,default="")
    Married=models.CharField(max_length=10,default="")
    Number=models.IntegerField(default=0)
    Employ=models.CharField(max_length=10,default="")
    Income=models.IntegerField(default=0)
    Loan=models.IntegerField(default=0)
    Area=models.CharField(max_length=10,default="")
    Status=models.CharField(max_length=10,default="")
    def __str__(self) :
        return self.Name

class EucationLoan(models.Model) :
    pass  