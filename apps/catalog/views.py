from django.shortcuts import render
import json
from apps.catalog.models import Product, Contacts, Category


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
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        preview = request.POST.get('preview')
        category = Category.objects.get(pk=request.POST.get('category'))
        unit_price = request.POST.get('unit_price')

        product_to_create = {'product_name': product_name, 'description': description, 'preview': preview,
                             'category': category, 'unit_price': unit_price}

        Product.objects.create(**product_to_create)

    return render(request, 'add_products.html')
