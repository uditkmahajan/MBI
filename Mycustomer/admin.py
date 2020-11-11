from django.contrib import admin

# Register your models here.
from .models import Updates,MyCustomer,HomeLoan
class HomeLoanAdmin(admin.ModelAdmin) :
    # fields =(("Area","Name"),("Email","Gender", "Status"),"Employ","Number","Income")
    fieldsets = (
        (None, {
            'fields': ("Area","Name")
        }),
        ('Advanced options', {
            'classes': ("collapse",'extrapretty'),
            'fields': ("Email","Gender", "Status"),
        }),
    )
   
admin.site.register(MyCustomer)
admin.site.register(Updates)
admin.site.register(HomeLoan,HomeLoanAdmin)

