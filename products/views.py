from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import NewItemForm, EditProductForm


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


@login_required
def new(request):

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            
            return redirect("products:index") # will be changed to point to dashboard

    else:
        form = NewItemForm()

    return render(request, "products/new.html", {
        "form":form
    })


@login_required
def dashboard(request):
    products = Product.objects.filter(created_by=request.user)

    return render(request, "products/dashboard.html", {
        "products": products
    })


@login_required
def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    return redirect("products:index")


@login_required
def edit(request, id):
    product = get_object_or_404(Product, id=id, created_by=request.user)

    if request.method == "POST":
        form = EditProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            
            return redirect("products:detail", id=product.id)

    else:
        form = EditProductForm(instance=product)

    return render(request, "products/edit.html", {
        "form": form,
        "title": "Edit Item"
    })
