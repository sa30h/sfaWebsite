from django.shortcuts import render,redirect
from django.http import HttpResponse

def homeview(request):
    return render(request,'sfa/home.html')

def aboutview(request):
    return render(request,'sfa/carousel/index.html')

def galleryview(request):
    return render(request,'sfa/album/index.html')