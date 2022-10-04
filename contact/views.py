from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForms


# Create your views here.

def contact(request):

    """ a view for users to sumbit forms to admin"""
    if request.method == "POST":
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            subject = "Contact Form"
            body = {
                'name': form.cleaned_data['name'],
                'contact_email': form.cleaned_data['contact_email'],
                'message': form.cleaned_data['message'],
            }
            message = "/n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com',
                          ['admin@example.com'])

            except BadHeaderError:
                messages.error(request, 'Invalid Header Found')
                return HttpResponse('Invalid header found')
            messages.success(request, 'Your form has been \
                successfuly submitted!')
            return(redirect(contact))

    form = ContactForms
    return render(request, "contact/contact.html", {'form': form})
