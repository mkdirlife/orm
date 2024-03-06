from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product(request):
    return HttpResponse("Product Page")

def productdetails(request, pk):
    return HttpResponse(f"Product Details Page: {pk}")