from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.
def home(request):
    products=Product.objects.all()
    params={'products':products}
    return render(request,"products/products.html",params)
