from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from . import views
urlpatterns = [
   path("",views.home,name="HOME"),
   path("about/",views.about,name="about"),
   path("signup/",views.handlesignup,name="handlesignup"),
   path("Admin/",include("manager.urls")),
   path("logout/",views.handlelogout,name="logout"),
   path("login/",views.handlelogin,name="login"),
   path("update/",views.update,name="update"),
   path("feedback/",views.feedback,name="FeedBack"),
   path("services/",views.services,name="loan"),
   path("homeloan/",views.homeloan,name="homeloan"),
   path("myprofile/",views.myprofile,name="profile"),
   path("forgot/",views.forgot,name="forgot"),
   path("model_save",views.model_save,name="lj"),
   path("load",views.load_model,name="sfsklp")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
