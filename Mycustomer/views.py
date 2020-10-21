import random as rd
import smtplib
from email.mime.multipart import MIMEMultipart   # it is used to make msg subparts like to from subject
from email.mime.text import MIMEText  # is used to add html content
import email.mime.application
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User   # import user
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
from .models import MyCustomer,Updates,HomeLoan
# Create your views here.

def home(request) :
    allfeed=MyCustomer.objects.order_by("-DateTime")
    li=[]
    k=0
    li=[i for i in allfeed if i.Feedback != ""]
    k=len(li)//3+1 if len(li)%3!=0 else len(li)//3 
    params={"allfeed":li,"length":range(1,k)}
    return render(request,"home.html",params)
    
def about(request) :
    allu=Updates.objects.all()
    print(allu)
    return render(request,"about.html")


def handlelogin(request) :
    if request.method=="POST" :
        fname=request.POST.get("fname","")
        lname=request.POST.get("lname","")
        password=request.POST.get("loginpassword","")
        email=request.POST.get("loginemail","")
        username=fname+" "+lname
        # for authantication that wheather the user exits or not we import authanticate.login,logout
        user=authenticate(username=username,password=password) # it will check 
        if user is not None :
               k=0
               login(request,user)
               allupdates=Updates.objects.all();
               length=len(allupdates)
               name=fname+" "+lname
               alluser=MyCustomer.objects.filter(Name=name)[0]
               for i in allupdates :
                   if i.Upload_date >= alluser.last_seen  and i.upload_time > alluser.Time : k=k+1
               alluser.mes=alluser.mes+k
               alluser.save()
               params={"allupdates":allupdates,"total":alluser.mes}
               messages.success(request,f"Welcome ! {name}")
               return render(request,"home.html",params)
        else :
               name=fname+" "+lname
               messages.error(request,f"{name} your details are incorect , check your details and login again !")  
               return redirect("/")


def handlesignup(request) :
    if request.method=="POST" :
       fname=request.POST.get("fname","")
       lname=request.POST.get("lname","")
       password=request.POST.get("password","")
       cpassword=request.POST.get("cpassword","")
       email=request.POST.get("email","")
       number=request.POST.get("number","")
       username=fname+" "+lname
       if password==cpassword and "@gmail.com" in email and len(number) == 10:
           if User.objects.filter(username=username).exists():
               messages.warning(request,f"{username} already exits ! Please enter unique First and Last name")
           else :
             myuser=User.objects.create_user(username,email,password) 
             myuser.first_name=fname
             myuser.last_name=lname
             myuser.save()
             name=fname+" "+lname
             now = datetime.now()
             d,t=str(now).split()
             cont=MyCustomer(Name=name,Email=email,Number=number,last_seen=d,Time=t)
             cont.save()
             messages.success(request,f"{name} you are Succesfully registered to our website")
       else : 
           name=fname+" "+lname
           messages.error(request,f"{name} your details are incorect , check your details and register again !")
    return redirect("/")

def handlelogout(request) :
        now = datetime.now()
        d,t=str(now).split()
        name=request.user
        alluser=MyCustomer.objects.filter(Name=name)[0]  
        alluser.last_seen=d
        alluser.Time=t
        alluser.save()
        
        logout(request)
        messages.success(request,"Succesfully logged out")
        return redirect("/")
    
def update(request) :
    allupdates=Updates.objects.order_by('-datetime')
    name=request.user
    alluser=MyCustomer.objects.filter(Name=name)[0]  
    length=len(allupdates)
    total=alluser.mes
    params={"allupdates":allupdates,"total":total}
    alluser.mes=0
    alluser.save()
    return render(request,"update.html",params)

def feedback(request) :
    if request.method=="POST" :
        name=request.user
        now = datetime.now()
        alluser=MyCustomer.objects.filter(Name=name)[0]  
        feedback=request.POST.get("feed","")
        alluser.Feedback=feedback
        alluser.DateTime=now
        alluser.save()
        messages.success(request,"Thank you for giving your valuable feedback")
    return redirect("/")
        
def services(request) :
    return render(request,"services.html")

def homeloan(request) :
    if request.method == "POST" :
         Name = request.POST.get("fname","")
         Email= request.POST.get("email","")
         Gender=request.POST.get("gender","")
         Graduate=request.POST.get("edu","")
         Married=request.POST.get("married","")
         Number=request.POST.get("number","")
         Employ=request.POST.get("employ","")
         Income=request.POST.get("income","")
         Loan=request.POST.get("lamo","")
         Area=request.POST.get("area","")
         if Married == "Married" and Employ == "Yes" and Income >=str(500000) and Loan < Income :
             Status="YES"
         else : Status="NO"
         cont=HomeLoan(Name=Name,Email=Email,Gender=Gender,Graduate=Graduate,Loan=Loan,Married=Married,Number=Number,Employ=Employ,Income=Income,Area=Area,Status=Status)
         cont.save()
         messages.success(request,"Your request for loan is uploaded !")
         return redirect("/")
    else :     return render(request,"homeloan.html")


def myprofile(request) :
    name=request.user
    if request.method=="POST" :   #ie if the contact form is submitted then
         now = datetime.now()
         d,t=str(now).split()
         Name=request.POST.get("full","")
         Email=request.POST.get("email","")
         Number=request.POST.get("number","")
         Address=request.POST.get("address","")
         City=request.POST.get("city","")
         State=request.POST.get("state","")
         Password=request.POST.get("password","")
         Profile=request.FILES['profile']
         print(Profile)
         cu=MyCustomer.objects.filter(Name=name)[0]
         us=User.objects.filter(username=name)[0]
         cu.Name=Name
         cu.Email=Email
         cu.Number=Number
         cu.State=State
         cu.Address=Address
         cu.City=City
         cu.Profile=Profile
         us.username=Name
         if Password != "" :
               us.set_password(Password)
         us.save()
         cu.save()
         messages.success(request,"Successfully changed account setting !")
         return redirect("/")
    else:
       alluser=MyCustomer.objects.filter(Name=name)[0]
       params={"alluser":alluser} 
    return render(request,"myprofile.html",params)

def forgot(request) :
  if request.method=="POST" :
    f=request.POST.get("username","")
    l=request.POST.get("key","")
    name=f+" "+l
    a,b,c,d=rd.choices(population = ["@","#","$","&","%","*","s","a","v","u"],k =4)
    us=User.objects.filter(username=name)[0]
    cu=MyCustomer.objects.filter(Name=name)[0]
    pa=a+b+c+d
    us.set_password(pa)
    us.save()
    print(pa)

    sender_mail = 'uditmahajanmhs@gmail.com'  
    receivers_mail = cu.Email
    html1 = """   
         Dear, %s .
        <p> Your request for new password have been accepted .
         Now your new password is <strong>%s</strong>
         You can change this password after going to myrofile </p>
         <br>
         Best Regards,"""%(name,pa)
    msg = MIMEMultipart() 
    msg['From'] = "MBI Online Loan Portal"
    msg['To'] = receivers_mail
    msg['Subject'] = "Forgot password"
    HTML_Contents = MIMEText(html1, 'html')
    msg.attach(HTML_Contents)
    try:  
       obj = smtplib.SMTP('smtp.gmail.com',587) 
       obj.ehlo()
       obj.starttls()
       obj.login("uditmahajanmhs@gmail.com","abcd*2001")
       obj.sendmail(sender_mail,receivers_mail,msg.as_string()) 
       obj.quit() 
       messages.success(request,"password have been reset !")  
    except Exception as a:  
        print(a)
        messages.error(request,"Enable to send mail ! please check your entries")  
    return redirect("/")
