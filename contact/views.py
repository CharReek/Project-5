from django.shortcuts import render, redirect
from .forms import ContactForms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


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
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            }
            messages = "/n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])

            except BadHeaderError:
                messages.error(request, 'Invalid Header Found')
                return HttpResponse('Invalid header found')
            messages.success(request, 'Your form has been successfuly submitted!')
            return(redirect(contact))

    form = ContactForms
    return render(request, "contact/contact.html", {'form':form})