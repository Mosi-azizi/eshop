from django.urls import path

from .views import ProductsList,product_detail,SearchProductView,products_categories_partial,ProductsListByCategory

urlpatterns = [
       path('products', ProductsList.as_view()),
       path('products/<category_name>',ProductsListByCategory.as_view()),
       path('products/<productId>/<name>',product_detail),
       path('products/search',SearchProductView.as_view()),
       path('products_categories_partial', products_categories_partial, name='products_categories_partial')
]