from django.urls import path
from .views import product_all,product_detail,category_list

app_name = 'store'

urlpatterns =[
    path('',product_all, name='product_all'),
    path('<slug:slug>/',product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/',category_list, name='category_list'),
]
