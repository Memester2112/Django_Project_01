from email import contentmanager
from django.shortcuts import render
from .models import Product
from .forms import ProductForm 
# Create your views here.


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = { 'form' : form}

    return render(request, "products/product_create.html", context)



def product_detail_view(request):
    obj = Product.objects.get(id = 1)
    my_context = {
        'title' : obj.name,
        'desc' : obj.description
    }
    return render(request, "products/product_detail.html", my_context)
