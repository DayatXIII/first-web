from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template
from django.shortcuts import render,  redirect, HttpResponse, HttpResponseRedirect
from .forms import ContactForms

def homepage(request):
    if request.method == 'GET':
        form = ContactForms()
    else:
        form = ContactForms(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = "Contact Form Received From:"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [settings.DEFAULT_FROM_EMAIL]
            context = {                
                'user': name,
                'email': email,
                'message': message
            }

            contact_message = get_template('contact_message.txt').render(context)

            try:
                send_mail(subject, contact_message, from_email, to_email, fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            #return HttpResponse("Email Sent!!")

    return render(request, 'home.html', {'form':form})