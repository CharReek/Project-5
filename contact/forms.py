from django import forms
from .models import ContactModel


class ContactForms(forms.ModelForm):
    """ a contact form that allows users to contact site admin """

    class Meta:
        model = ContactModel
        fields = [
            "name",
            "contact_email",
            "message"
        ]
