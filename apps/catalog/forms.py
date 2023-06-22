from django import forms
from apps.catalog.models import Product, Version
from apps.users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control-10'


class ProductForm(StyleFormMixin, forms.ModelForm):
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

    def save(self, *args, **kwargs):
        self.owner_id = kwargs['owner_id']
        if self.owner_id:
            self.instance.owner = User.objects.get(pk=self.owner_id)
        return super().save(*args, **kwargs)


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):
        cleaned_data = super().clean()
        is_active = cleaned_data.get('is_active')
        product = cleaned_data.get('product')
        Version.objects.filter(product=product).exclude(id=self.instance.id).update(is_active=False)
        return is_active

