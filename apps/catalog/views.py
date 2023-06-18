from django.shortcuts import get_object_or_404, redirect

from apps.catalog.forms import ProductForm
from apps.catalog.models import Product, Post
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from apps.catalog.services import send_email


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Products'
    }

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'description', 'preview', 'category', 'unit_price')
    success_url = reverse_lazy('catalog:products')


class ProductByPageListView(ListView):
    model = Product
    template_name = 'catalog/products_by_page_list.html'
    paginate_by = 3
    extra_context = {
        'title': 'All products'
    }


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object'].product_name
        return context_data

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:product', kwargs={'pk': self.kwargs['pk']})

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')

class PostCreateView(CreateView):
    model = Post
    fields = ('post_title', 'text', 'preview')
    success_url = reverse_lazy('catalog:blog')


class PostListView(ListView):
    model = Post
    extra_context = {
        'title': 'Our blog'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object'].post_title
        return context_data

    def get_object(self, queryset=None):
        object = self.model.objects.get(pk=self.kwargs['pk'])
        if object:
            object.views += 1
            object.save()
            if object.views == 100:
                send_email(object.post_title)
        return object


class PostUpdateView(UpdateView):
    model = Post
    fields = ('post_title', 'text', 'slug', 'preview')

    def get_success_url(self):
        return reverse_lazy('catalog:post', kwargs={'pk': self.kwargs['pk']})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:blog')


def toggle_activity(request, pk):
    post_item = get_object_or_404(Post, pk=pk)
    if post_item.is_published:
        post_item.is_published = False
    else:
        post_item.is_published = True

    post_item.save()

    return redirect(reverse('catalog:post', args=[post_item.pk]))
