from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def First_look(request,*agrs, **kwargs):
    return render(request, "home.html", {})

def About_page(request,*agrs, **kwargs):   #template context example"""
    my_context={
        "my_text":"This is about me",
        "my_num":123,
        "my_lis": [123, 456,879]}
    return render(request, "about.html", my_context)


def Contact_page(request,*agrs, **kwargs):
    return render(request, "contact.html", {})