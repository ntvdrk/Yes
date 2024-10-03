from django.shortcuts import render
from django.http import HttpResponse


def view3(request):
    return HttpResponse('View 3 from app3')