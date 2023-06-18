from django.db import models
from django.utils.text import slugify
from apps.catalog.services import transliterate

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=40, verbose_name='Product Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    preview = models.ImageField(upload_to='products/', verbose_name='Preview', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    unit_price = models.IntegerField(verbose_name='Unit Price')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    last_modified = models.DateTimeField(auto_now=True, verbose_name='Last Modified')

    def __str__(self):
        return f'Product Name: {self.product_name}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Category(models.Model):
    category_name = models.CharField(max_length=15, verbose_name='Category Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)

    def __str__(self):
        return f'Category Name: {self.category_name}'

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Contacts(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    phone = models.CharField(max_length=100, verbose_name='Phone Number')
    email = models.EmailField(max_length=254, verbose_name='E-mail')

    def __str__(self):
        return f'Contact: {self.first_name} {self.last_name} {self.phone} {self.email}'

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class Post(models.Model):
    post_title = models.CharField(max_length=250, verbose_name='Post Title')
    slug = models.CharField(max_length=50, verbose_name='Slug', **NULLABLE)
    text = models.TextField(verbose_name='Text', **NULLABLE)
    preview = models.ImageField(upload_to='blog/', verbose_name='Preview', **NULLABLE)
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    views = models.IntegerField(default=0, verbose_name='Views')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self, self.post_title)
            self.slug = transliterate(self.slug)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.is_published:
            self.is_published = False
        self.save()

    def __str__(self):
        return f'{self.post_title}'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    number = models.CharField(max_length=255, verbose_name='Version number')
    name = models.CharField(max_length=255, verbose_name='Version name')
    is_active = models.BooleanField(default=False, verbose_name='Active')

    def __str__(self):
        return f'{self.name} ({self.number}): {self.product}'

    class Meta:
        verbose_name = 'version'
        verbose_name_plural = 'versions'
