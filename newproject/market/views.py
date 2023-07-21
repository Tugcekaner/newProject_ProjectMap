from django.shortcuts import render,redirect,get_object_or_404
from .models import *

# Create your views here.
def indexPage(request):
    kategoriler = Category.objects.all()
    urunler = Product.objects.all()

    context = {
        'kategoriler': kategoriler,
        'urunler': urunler
    }

    return render(request,'index.html',context)

def detailPage(request,id):
    product = get_object_or_404(Product,id=id)

    context={
        'product': product,
    }

    return render(request,'detail.html',context)