from django.urls import path
from .views import ElectronicExct


urlpatterns=[
    path('',ElectronicExct.as_view(),name='elect'),



]