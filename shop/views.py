from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import render


def index(req):
    return render(req,'shop/index.html')
def products(request):
    return render(request,'shop/products.html')

def blog(request):
    return

def home(reqs):
    return render(reqs,'shop/home.html')

def contact(request):
    return
def form(req):
    return render(req,'shop/basic.html')
def details(request):
    print(request.GET.get('entered details','details unavailable'))
    return render(request,'shop/details.html')
