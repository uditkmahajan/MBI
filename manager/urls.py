from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from . import views
urlpatterns = [
   path("",views.Admin,name="ADMIN"),
   path("upload/",views.upload,name="UPLOAD"),
   path("feedback",views.feedback,name="FEEDBACK"),
   path("customer/",views.customer,name="customer"),
   path("eligibilty/",views.eligibility,name="Eligible"),
   path("customer/<str:slug>",views.slug,name="slug"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
