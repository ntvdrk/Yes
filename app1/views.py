from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view1(request):
    return HttpResponse("This is view 1 in app1")

def view2(request):
    return HttpResponse("This is view 2 in app1")

def view3(request):
    return HttpResponse("This is view 3 in app1")

