from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from requests import get

from shopp_app.models import Category, Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.


def allProdCat(request,C_slug=None):
    C_Page=None
    products_list=None
    if C_slug!=None:
        C_Page=get_object_or_404(Category,slug=C_slug)
        products_list=Products.objects.all().filter(category=C_Page,available=True)
    else:
        products_list=Products.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page',1))
    except:
        page=1
    try:
        products=paginator.page(page)
    except(InvalidPage,EmptyPage):
        products=paginator.page(paginator.num_pages)


    return render(request,"category.html",{'category':C_Page,'products':products})

def prodetail(request,C_slug,product_slug):
    try:
        product=Products.objects.get(category__slug=C_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})

