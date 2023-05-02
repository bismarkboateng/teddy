from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q



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


@login_required
def browse(request):

    query = request.GET.get("query", "")
    category = Category.objects.all()
    category_id = request.GET.get("category_id", 0)
    products = Product.objects.filter(is_sold=False)

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)).filter(is_sold=False)

    if category_id:
        products = Product.objects.filter(category_id=category_id)

    return render(request, "products/browse.html", {
        "products": products,
        "categories": category
    })