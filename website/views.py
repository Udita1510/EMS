from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def website(request):
  
  context = {
    'name': "CHauhan",
  }
  
  return render(request, 'website/dashboard.html', context=context)



def aboutus(request):
  return render(request, "website/aboutus.html")

def contact(request):
  phoneNumber = "0281 256 3445"
  email = "admin@atmiyauni.ac.in"
  
  print(phoneNumber)
  
  if request.method == "POST":
    gName = request.POST.get("name")
    gEmail = request.POST.get("email")
    gMessage = request.POST.get("message")
    gSubject = request.POST.get("subject")
    
    data = ContactData()
    data.name = gName
    data.email_id = gEmail
    data.message = gMessage
    data.subject = gSubject
    
    
    data.save()
    
    return redirect("contact")
    
  
  data = {
    'phone' : phoneNumber,
    'EmailID' : email,
  }
  
  return render(request,"website/contactus.html", context= data)

def question(request):
  return render(request,"website/questions.html")

def sport(request):
  return render(request,"website/sportsEvent.html")