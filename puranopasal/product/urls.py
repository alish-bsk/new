from django.urls import path
from . import views


urlpatterns=[
    path(' ',views.product_cost,name='product_cost'),
    path('sold/',views.product_sold,name='product_sold'),
    path('info/',views.product_info,name='product_info'),
    ##path('usersold/',views.product_usersold,name='product_usersold'),




]
