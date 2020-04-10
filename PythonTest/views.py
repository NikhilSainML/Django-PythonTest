from django.shortcuts import render
from django.http import HttpResponse
from PythonTest.SeleniumScript import *

def index(request):
    return render(request, 'index.html')

def execute(request):
    WebAuto = Test()
    WebAuto.FormAuthomation()
    return HttpResponse('result')
    #return render(request, 'result.html', {'submit': res})
