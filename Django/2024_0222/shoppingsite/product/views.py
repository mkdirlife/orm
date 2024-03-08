from django.shortcuts import render
from .data import product_database

def product_list(request):
    context = {"product_list": product_database}
    return render(request, "product/product_list.html", context)


def product_detail(request, pk):
    context = {"product": product_database[pk - 1]}
    return render(request, "product/product_detail.html", context)