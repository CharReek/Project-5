from django import forms 
from .models import ContactForm

class ContactForms(form.ModelForm):
    """ a contact form that allows users to contact site admin """
    
    class Meta:
        model = ContactForm
        fields = [
            "name",
            "email",
            "message"
        ]