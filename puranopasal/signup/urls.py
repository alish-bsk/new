from django.urls import path
from .views import SignUpExct,SignUpView


urlpatterns=[
    path('', SignUpExct.as_view(), name='signup'),
    path('', SignUpExct.as_view(), name='success_page'),
    path('', SignUpView.as_view(), name='signupview'),


]