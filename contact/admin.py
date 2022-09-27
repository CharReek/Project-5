from django.contrib import admin
from .models import ContactModel

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    """ admin conact form """
    list_display = ('name', 'contact_email', 'message')

admin.site.register(ContactModel, ContactAdmin)  