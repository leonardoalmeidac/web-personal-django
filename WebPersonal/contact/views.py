from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request) :
    contact_form = ContactForm()
    if request.method == "POST" :
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            number_ph = request.POST.get('number_ph')
            # enviamos el correo electronico
            email = EmailMessage(
                "Web Personal: Nuevo mensaje correo electronico ",
                f"De {name} <{email}> \n\n Escribió: \n\n {content} y su numero telefonico es {number_ph}",
                "no-contestar@inbox.mailtrap.io",
                ["leonardo.almeidac@gmail.com"],
                reply_to=[email])
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except :
                return redirect(reverse('contact')+'?fail')    
            
            

    return render(request, "contact/contact.html", {'form' : contact_form})
