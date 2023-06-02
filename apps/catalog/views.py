from django.shortcuts import render
import json
from apps.catalog.models import Product, Contacts, Category
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy


# Create your views here.
#def products(request):
    #products_list = Product.objects.all()
    #context = {
        #'objects_list': products_list,
        #'title': 'Products'
    #}
    #return render(request, 'product_list.html', context)

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Products'
    }


#def add_products(request):
    #folder = 'media/products/'
    #if request.method == 'POST' and request.FILES:
        #product_name = request.POST.get('product_name')
        #description = request.POST.get('description')
        #preview = request.FILES['preview']
        #fs = FileSystemStorage(location=folder)
        #filename = fs.save(preview.name, preview)
        #preview_url = fs.url(filename)[7:]
        #category = Category.objects.get(pk=request.POST.get('category'))
        #unit_price = request.POST.get('unit_price')

        #product_to_create = {'product_name': product_name, 'description': description,
                             #'preview': f'products/{preview_url}',
                             #'category': category, 'unit_price': unit_price}

        #Product.objects.create(**product_to_create)

    #return render(request, 'product_form.html')

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'preview', 'category', 'unit_price')
    success_url = reverse_lazy('catalog:products')

#def all_products(request):
    #"""create a Paginator object"""
    #all_products = []
    #for product in Product.objects.all():
        #all_products.append(
            #{'product_name': product.product_name, 'description': product.description, 'preview': product.preview,
            # 'category': product.category, 'unit_price': product.unit_price}
        #)
    #p = Paginator(all_products, per_page=3)
    #page_number = request.GET.get('page', 1)
    #page = p.page(page_number)

    #context = {
        #'object_list': page.object_list,
        #'page_obj': page,
        #'title': 'All products'
    #}
    #return render(request, 'products_by_page_list.html', context)

class ProductByPageListView(ListView):
    model = Product
    template_name = 'catalog/products_by_page_list.html'
    paginate_by = 3
    extra_context = {
        'title': 'All products'
    }
