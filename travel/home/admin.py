from django.contrib import admin
from .models import  Contact
# Register your models here.



class ContactAdmin(admin.ModelAdmin):
    list_display =  ('id', 'c_name', 'c_subject', 'c_email', 'c_message' )

admin.site.register(Contact,ContactAdmin)