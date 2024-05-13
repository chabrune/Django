from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Ta soeur en slibar</h1>')

def about(request):
    return HttpResponse('<h1>Ta soeur en calslip</h1>')