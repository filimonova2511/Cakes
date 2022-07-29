from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .forms import *


def cakes(request):
    cakes = models.Cake.objects.all()
    context = {'cakes': cakes}
    return render(request, 'cakes.html', context)


def cake(request, cake_id):
    cake = get_object_or_404(models.Cake, id=cake_id)
    products = models.Product.objects.filter(cake=cake)
    context = {'cake': cake, 'products': products}
    return render(request, 'cake.html', context)


def product(request, product_id):
    product = get_object_or_404(models.Product, id=product_id)
    samples = models.Sample.objects.filter(product=product)
    context = {'product': product, 'samples': samples}
    return render(request, 'product.html', context)


def sample(request, sample_id):
    sample = get_object_or_404(models.Sample, id=sample_id)
    samples = models.Sample.objects.filter(sample=sample)
    context = {'sample': sample, 'samples': samples}
    return render(request, 'sample.html', context)


def fillings(request):
    fillings = models.Filling.objects.all()
    context = {'fillings': fillings}
    return render(request, 'fillings.html', context)


def about_us(request):
    text = 'Мы поможем сделать Ваш праздник незабываемым, изготовив великолепный торт.'
    context = {"text": text}
    return render(request, 'about_us.html', context)


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            order = models.Order.objects.create(**form.cleaned_data)
            return redirect('cakes')
    else:
        form = OrderForm()
        context = {'form': form}
        return render(request, 'order.html', context)


def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            models.Review.objects.create(name=name, text=text)
            return redirect('reviews')
    else:
        form = ReviewForm()
        reviews = models.Review.objects.all()
        context = {'reviews': reviews, 'form': form}
        return render(request, 'reviews.html', context)





















