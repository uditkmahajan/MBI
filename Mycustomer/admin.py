from django.contrib import admin

# Register your models here.
from .models import Updates,MyCustomer,HomeLoan
admin.site.register(MyCustomer)
admin.site.register(Updates)
admin.site.register(HomeLoan)

