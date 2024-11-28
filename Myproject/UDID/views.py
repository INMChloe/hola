from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Chloe (request):
    return HttpResponse("<h1>WELCOME TO MY WEBSITE<h1>")