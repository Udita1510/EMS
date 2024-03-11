from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.website, name="website"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('contactus/',views.contact,name="contact"),
    path('questions/',views.question,name="question"),
    path('sports_event/',views.sport,name="sport"),
       
]



# Develop rest of pages and their Views && URLs. okay. 