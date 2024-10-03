from django.shortcuts import render
from django.http import HttpResponse

def view2(request):
    return HttpResponse('View 2 from app2')
