from django import forms
from apps.catalog.models import Product
import re


class ProductForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('product_name').lower()
        description = cleaned_data.get('description').lower()
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',
                     'casino', 'cryptocurrency', 'crypto', 'exchange', 'cheap', 'free', 'fraud', 'police', 'radar']

        for word in bad_words:
            if word in name or word in description:
                raise forms.ValidationError('There is at least one prohibited word in the name or the description')

        return cleaned_data
