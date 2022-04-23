from django.urls import re_path as url
from django.urls import path

from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product'),
    path('order', views.order, name='order'),
    path('orders', views.orders, name='orders'),
    path('investoram', views.investoram, name='investoram'),
    path('enterpriser', views.enterpriser, name='enterpriser'),
]

