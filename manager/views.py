from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from Mycustomer.models import Updates,MyCustomer,HomeLoan
from django.core.paginator import Paginator         # 1st step for pagination 
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart   # it is used to make msg subparts like to from subject
from email.mime.text import MIMEText  # is used to add html content
import email.mime.application
 

# Create your views here.
def Admin(request) :
   allapp=HomeLoan.objects.all()
   p = Paginator(allapp,10)   # 2nd step : show 2 name for each page
   page_number = request.GET.get('page')
   page_obj = p.get_page(page_number)
   if request.method=="POST" :
      username=request.POST.get("username","")
      password=request.POST.get("key","")
      if username=="UDIT" and password=="abcd*2001" :  
            messages.success(request,"Welcome Udit Mahajan !")  
            return render(request, 'admin/home.html', {'page_obj': page_obj,"length":len(allapp)})
      else :
         return redirect("/")

   return render(request,"admin/home.html", {'page_obj': page_obj,"length":len(allapp)})

def feedback(request) :
       allfeed=MyCustomer.objects.order_by("-DateTime")
       li=[]
       k=0
       for i in allfeed :
             if i.Feedback != "" :
                li.append(i)
       print(li)
       k=len(li)//3+1 if len(li)%3!=0 else len(li)//3 
       params={"allfeed":li,"length":range(1,k)}
       return render(request,"admin/feedback.html",params)
 
def upload(request) :
    if request.method=="POST" :
         Title=request.POST.get("title","")
         Content=request.POST.get("text","")
         now = datetime.now()
         d,t=str(now).split()
         cont=Updates(Topic=Title,Content=Content,Upload_date=d,upload_time=t,datetime=now)
         cont.save()
         messages.success(request,"Post is uploaded to the website")
         return redirect("/Admin")
    else :
          return render(request,"admin/upload.html")

def customer(request) :
   allcust=MyCustomer.objects.all()
   p = Paginator(allcust,10)   # 2nd step : show 2 name for each page
   page_number = request.GET.get('page')
   page_obj = p.get_page(page_number)
   return render(request, 'admin/customer.html', {'page_obj': page_obj})

def eligibility(request) :
    if request.method =="POST" :
      app=HomeLoan.objects.filter(Status="YES")
      sender_mail = 'uditmahajanmhs@gmail.com'
      for i in app :  
         receivers_mail = i.Email
         html1 = """   
         Dear, %s .
         Thanks for using MBI's online loan services .
         <p><strong>Your loan has been passed by our bank </strong>and now, you have to
         submit the following documents to our nearer bank after filling the given form.</p>
         <ul>
         <li>Adhar card</li>
         <li>2 passport photos</li>
         <li>House paper</li>
         </ul>  
         
         Best Regards,"""%(i.Name)
 
         msg = MIMEMultipart()
         msg['Subject'] = "loan approvement"
         msg['From'] = "MBI Online Loan portal"
         msg['To'] = (i.Name)
         HTML_Contents = MIMEText(html1, 'html')
         filename='loan.pdf'
         fo=open(filename,'rb')
         attach = email.mime.application.MIMEApplication(fo.read(),_subtype="pdf")
         fo.close()
         attach.add_header('Content-Disposition','attachment',filename=filename)
         msg.attach(attach)
         msg.attach(HTML_Contents)
         try:  
           obj = smtplib.SMTP('smtp.gmail.com',587) 
           obj.ehlo()
           obj.starttls()
           obj.login("uditmahajanmhs@gmail.com","abcd*2001")
           obj.sendmail(sender_mail,receivers_mail,msg.as_string())  
           flag=True  
         except Exception as a: 
           messages.error(request,"Enable to send mail ! please check your entries")  
      if flag==True : messages.success(request,"Emails have been sent to all eligible customers!")
      app=HomeLoan.objects.filter(Status="NO")
      sender_mail = 'uditmahajanmhs@gmail.com'
      for i in app :  
         receivers_mail = i.Email
         html1 = """   
         Dear, %s .
         Thanks for using MBI's online loan services .
         <p><strong>Sorry ,Your request for loan has been declined by our bank </strong>and now, you are elible to
         get loan from our bank.. </p> <br>
         Best Regards,"""%(i.Name)
 
         msg = MIMEMultipart()
         msg['Subject'] = "loan approvement"
         msg['From'] = "MBI Online Loan portal"
         msg['To'] = (i.Name)
         HTML_Contents = MIMEText(html1, 'html')
         msg.attach(HTML_Contents)
         try:  
           obj = smtplib.SMTP('smtp.gmail.com',587) 
           obj.ehlo()
           obj.starttls()
           obj.login("uditmahajanmhs@gmail.com","abcd*2001")
           obj.sendmail(sender_mail,receivers_mail,msg.as_string())  
           flag=True  
         except Exception as a: 
           flag=False
           messages.error(request,"Enable to send mail ! please check your entries")  
      obj.quit()
      if flag==True : messages.success(request,"Emails have been sent to non eligible !")
      HomeLoan.objects.all().delete()
      return redirect("/Admin")
    else :
      allcust=HomeLoan.objects.filter(Status="YES")
      p = Paginator(allcust,10)   # 2nd step : show 2 name for each page
      page_number = request.GET.get('page')
      page_obj = p.get_page(page_number)
      return render(request, 'admin/eligible.html', {'page_obj': page_obj,"length":len(allcust)})

def slug(request,slug) :
   cus=MyCustomer.objects.filter(s_no=slug)[0]
   return render(request,"Admin/slug.html",{"cust":cus})