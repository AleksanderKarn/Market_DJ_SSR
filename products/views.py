from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from products.forms import ProductForm, CategoryForm
from products.models import Product, Category

from django.views.generic import TemplateView


#### CRUD для Product
class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner_id = self.request.user.id
        product.save()
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')


#########################################################################################

class HomePageView(TemplateView):
    template_name = 'product/home.html'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('products:category_list')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


# def get_context_data(self, **kwargs):  #### кэширование списка категорий
#    context_data = super().get_context_data(**kwargs)
#    context_data['categories'] = _cache_categories(self.object_list)
#    return context_data


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('products:category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('products:category_list')


def change_status(request, pk):
    product_item = get_object_or_404(Product, pk=pk)
    if product_item.is_active == True:
        product_item.is_active = False
    else:
        product_item.is_active = True
    product_item.save()

    return redirect(reverse('products:product_list'))
