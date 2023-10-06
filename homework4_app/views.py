from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ProductFormWidget, ProductChoiceForm
from homework2_app.models import Product

from django.shortcuts import redirect


def product_update_form(request, product_id):
    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            description = form.cleaned_data.get('description')
            number = form.cleaned_data.get('number')
            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            product = Product.objects.filter(pk=product_id).first()
            product.name = name
            product.price = price
            product.description = description
            product.quantity = number
            product.image = image.name
            product.save()

    else:
        form = ProductFormWidget()
    return render(request, 'homework4_app/product_update.html', {'form': form})


def product_update_id_form(request):
    if request.method == 'POST':
        form = ProductChoiceForm(request.POST)
        if form.is_valid():
            prod_id = form.cleaned_data.get('product_id')
            response = redirect(f'/homework4/product_update/{prod_id}')
            return response
    else:
        form = ProductChoiceForm()
    return render(request, 'homework4_app/product_update_id.html', {'form': form})


def index(request):
    return render(request, "homework4_app/index.html")
