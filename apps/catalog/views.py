from django.shortcuts import render
import json

# Create your views here.

def homepage(request):
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
    return render(request, 'contacts.html')
