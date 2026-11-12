from django.urls import path
from .views import SignInExct, SignInPageExct

urlpatterns = [
    path('', SignInExct.as_view(), name='signin'),
    path('signin/signinpage/', SignInPageExct.as_view(), name='signinpage'),
    path('signinpage_btn/', SignInPageExct.as_view(), name='signinpage_btn'),
]
