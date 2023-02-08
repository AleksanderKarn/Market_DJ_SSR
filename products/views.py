
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from products.services import _cache_categories
from products.forms import ProductForm, CategoryForm
from products.models import Product, Version, Category

from django.views.generic import TemplateView


#### CRUD для Product
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner_id = self.request.user.id
        product.save()
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')

    ###########################################################################


def version_for_product(request):
    context = {
        'query_result': Version.objects.all()

    }

    return render(request, 'products/version_list.html', context)


#########################################################################################

class HomePageView(TemplateView):
    template_name = 'product/home.html'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('products:category_list')


class CategoryListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['categories'] = _cache_categories(self.object_list)
        return context_data


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('products:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('products:category_list')
