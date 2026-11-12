from django.urls import path
from . import views


urlpatterns=[
    path('home/',views.home,name='home'),
    path('payment/',views.payment,name='payment'),
    path('/',views.payment_failed,name='payment_failed'),
  #  path('/',views.product_item,name='product_item')



]