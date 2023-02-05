from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from products.forms import ProductForm
from products.models import Product, Version

from django.views.generic import TemplateView


#def home_page(request):
#    return render(request, 'products/home_page.html')



                                   #### CRUD для Product
class VersionListView(ListView):
    model = Version


class ProductListView(ListView):
    model = Product

    #def get_queryset(self):
#
    #    products = Product.objects.filter(products__status_version=True)
    #    for product in products:
    #        print(product.products)
    #    return products




class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')



def version_for_product(request):
    context = {
        'query_result': Version.objects.all()

    }

    return render(request, 'products/version_list.html', context)


#########################################################################################

class HomePageView(TemplateView):
    template_name = 'product/home.html'