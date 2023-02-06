from django.urls import path
from django.views.decorators.cache import cache_page

from products.apps import ProductsConfig
from products.formset_views import ProductUpdateWithVersionView

from products.views import HomePageView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, \
    ProductCreateView, version_for_product, CategoryCreateView, CategoryListView, CategoryUpdateView, \
    CategoryDeleteView

app_name = ProductsConfig.name




urlpatterns = [
    path('', HomePageView.as_view(), name='list'),

    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', cache_page(300)(ProductDetailView.as_view()), name='product_detail'),

    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('product_crate/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/version/', ProductUpdateWithVersionView.as_view(), name='update_with_version'),

    #path('version_list/', VersionListView.as_view(), name='version_list'),
    path('version_for_product/', version_for_product, name='version_list'),

    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('category_crate/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),

]
