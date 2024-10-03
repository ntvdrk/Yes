from django.shortcuts import render
from django.http import HttpResponse



def view1(request):
    return HttpResponse("This is view 1 in app2")

def view2(request):
    return HttpResponse("This is view 2 in app2")
#   return HttpResponse("В жизни главное - это велосипед")


def view3(request):
    return HttpResponse("This is view 3 in app2")