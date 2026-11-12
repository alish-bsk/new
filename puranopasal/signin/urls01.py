from django.urls import path
from .views import SignInExct


urlpatterns=[
    path('',views.signin,name='signin'),
    path('signin/signinpage/',views.signinpage,name='signinpage'),
    path('logout/',views.logout,name='logout'),
    path('signinpage_btn/',views.signinpage_btn,name='signinpage_btn'),
    


]
