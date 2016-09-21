from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product
# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'products/index.html', context)

def new(request):
    return render(request, 'products/new.html')

def create(request):
    if request.method=='POST':
        Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    return redirect(reverse('products:index'))

def show(request, id):
    context = {
        'product': Product.objects.get(id=id)
    }
    return render(request, 'products/show.html')

def edit(request, id):
    context = {
        'product': Product.object.get(id=id)
    }
    return render(request, 'products/edit.html')

def update(request, id):
    if request.method=='POST':
        p = Product.objects.get(id=id)
        p.name = request.POST['name']
        p.description = request.POST['description']
        p.price = request.POST['price']
        p.save()
    return redirect(reverse('products:show', kwargs={'id': id}))
def destroy(request, id):
    if request.method=='POST':
        Product.objects.get(id=id).delete()
    return redirect(reverse('products:index'))
