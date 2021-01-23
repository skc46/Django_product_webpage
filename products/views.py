from django.shortcuts import render
from .models import Products
from .forms import ProductForm
# Create your views here.

def product_detail_view(request):
    obj = Products.objects.get(id=1)
    # context = {
    #     'title': obj.Item,
    #     'description': obj.Description
    context = {
        'object': obj
        }
    return render(request, "product_templates/detail.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()  # this clears the field after the data is saved

    context = {
        'form': form
        }
    return render(request, "product_templates/product_create.html", context)