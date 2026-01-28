from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product


@login_required(login_url='/')
def product_list(request):
    products = Product.objects.filter(available=True)
    context = {'products': products}
    return render(request, 'store/product_list.html', context)


@login_required(login_url='/')
def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    context = {'product': product}
    return render(request, 'store/product_detail.html', context)


def about_page(request):
    return render(request, 'store/about.html')


def contact_page(request):
    return render(request, 'store/contact.html')


def privacy_page(request):
    return render(request, 'store/privacy.html')


def terms_page(request):
    return render(request, 'store/terms.html')