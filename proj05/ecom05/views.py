from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'ecom05/index.html')

def about(request):
    return HttpResponse("About!")    

def contact(request):
    return HttpResponse("Contact!")    


def productview(request):
    return HttpResponse("Product View!")    


def search(request):
    return HttpResponse("Search!")    