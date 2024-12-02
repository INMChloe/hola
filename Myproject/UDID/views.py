from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def Chloe (request):
    template=loader.get_template("coding.html")
    return HttpResponse(template.render()) 