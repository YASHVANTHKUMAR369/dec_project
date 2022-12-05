from django.contrib import admin
from snadhanapp.models import customer_details

class customer_detailsAdmin(admin.ModelAdmin):
    list = ['mobile_no', 'cname', 'mail', 'subject', 'message']
    
admin.site.register(customer_details, customer_detailsAdmin)

# Register your models here.
