from django.shortcuts import render

# Create your views here.

def home(request) :
    return render(request,'nucleo/home.html')

def about(request) :
    return render(request,'nucleo/about-me.html')
    
def contact(request) :
    return render(request, 'nucleo/contactame.html')