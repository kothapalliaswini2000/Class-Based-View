from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.

# returning string as response by using FBV

def StringByFbv(request):
    return HttpResponse('<h1>StringByFbv</h1>')

# returning string as response by using CBV

class StringByCbv(View):
    def get(self,request):
        return HttpResponse('<h1>StringByCbv</h1>')

# returning html page as response by using FBV

def HtmlByFbv(request):
    return render(request,'HtmlByFbv.html')

# returning html page as response by using CBV

class HtmlByCbv(View):
    def get(self,request):
        return render(request,'HtmlByCbv.html')

 # Inserting data into school by using FBV

def insertbyfbv(request):
    d={'ESFO':SchoolForm()}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_by_fbv is done')
        else:
            return HttpResponse('insert_by_fbv is failed')
    
    return render(request,'insertbyfbv.html',d)

# Inserting data into school by using CBV

class InsertByCbv(View):
    def get(self,request):
        d={'ESFO':SchoolForm()}
        return render(request,'InsertByCbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_by_cbv is done')
        else:
            return HttpResponse('insert_by_cbv is failed')
    

#TEMPLATE VIEW
class HtmlbyTV(TemplateView):
    template_name='HtmlbyTV.html'