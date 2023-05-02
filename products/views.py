from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def index(request):
    products = Product.objects.filter(is_sold=False)[0:5]
    category = Category.objects.all()

    
    return render(request, "products/index.html", {
        "products": products,
        "category": category
    })



def detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, "products/detail.html", {
        "product": product
    })