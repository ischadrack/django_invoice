from django.contrib import admin
from .models import *

# Register your models here.


class admincustomer(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'adress', 'sex', 'age', 'city', 'zip_code')

class adminInvoice(admin.ModelAdmin):
    list_display=('customer', 'save_by', 'invoice_date_time', 'total', 'last_updated_date', 'paid', 'invoice_type')

admin.site.register(customer, admincustomer)
admin.site.register(Invoice, adminInvoice)
admin.site.register(Article)

