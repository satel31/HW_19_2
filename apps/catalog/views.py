from django.shortcuts import render
import json
from apps.catalog.models import Product, Contacts, Category
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage


# Create your views here.

def homepage(request):
    data = Product.objects.order_by('-creation_date')[:5]
    for d in data:
        print(d)
    return render(request, 'homepage.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        message = request.POST.get('message')
        feedback_data = f'name: {name}, phone: {phone}, email: {email}, message: {message}'
        with open('feedback_contacts.txt', 'a', encoding='utf-8') as f:
            f.write(feedback_data)
            f.write('\n')

    context = {'contact': []}
    for contact in Contacts.objects.all():
        context['contact'].append(
            {'first_name': contact.first_name, 'last_name': contact.last_name, 'phone': contact.phone,
             'email': contact.email})
    return render(request, 'contacts.html', context)


def products(request):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list,
        'title': 'Products'
    }
    return render(request, 'products.html', context)


def add_products(request):
    folder = 'media/products/'
    if request.method == 'POST' and request.FILES:
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        preview = request.FILES['preview']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(preview.name, preview)
        preview_url = fs.url(filename)[7:]
        category = Category.objects.get(pk=request.POST.get('category'))
        unit_price = request.POST.get('unit_price')

        product_to_create = {'product_name': product_name, 'description': description,
                             'preview': f'products/{preview_url}',
                             'category': category, 'unit_price': unit_price}

        Product.objects.create(**product_to_create)

    return render(request, 'add_products.html')


def all_products(request):
    """create a Paginator object"""
    all_products = []
    for product in Product.objects.all():
        all_products.append(
            {'product_name': product.product_name, 'description': product.description, 'preview': product.preview,
             'category': product.category, 'unit_price': product.unit_price}
        )
    p = Paginator(all_products, per_page=3)
    page_number = request.GET.get('page', 1)
    page = p.page(page_number)

    context = {
        'object_list': page.object_list,
        'page_obj': page,
        'title': 'All products'
    }
    return render(request, 'products_by_page.html', context)
