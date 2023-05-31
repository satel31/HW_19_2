from django.shortcuts import render
import json
from apps.catalog.models import Product, Contacts

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
    return render(request, 'products.html')