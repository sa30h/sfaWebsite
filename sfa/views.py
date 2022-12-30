from django.shortcuts import render,redirect
from django.http import HttpResponse

def homeview(request):
    return render(request,'sfa/home.html')