from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import ProductForm

# Create your views here.

def index_view(request):
    products = Product.objects.all().order_by('category', 'product_name')
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def sale_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'sale_view.html', context)

def create_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product_name = form.cleaned_data.get('product_name')
            description = form.cleaned_data.get('description')
            category = request.POST.get('category')
            remainder = request.POST.get('remainder')
            price = request.POST.get('price')
            new_sale = Product.objects.create(product_name=product_name, description=description, category=category, remainder=remainder, price=price)
            return redirect("sale_view", pk=new_sale.pk)
        return render(request, 'create.html', {"form": form})

def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'product_name': product.product_name,
            'description': product.description
        })
        return render(request, 'update.html', {"product": product, "form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.product_name = request.POST.get('product_name')
            product.description = request.POST.get('description')
            product.category = request.POST.get('category')
            product.remainder = request.POST.get('remainder')
            product.price = request.POST.get('price')
            product.save()
            return redirect("sale_view", pk)
        return render(request, 'update.html', {"product": product, "form": form})

def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, "delete.html", {"product": product})
    else:
        product.delete()
        return redirect("index")