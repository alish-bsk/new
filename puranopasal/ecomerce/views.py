
# Create your views here.
from django.shortcuts import render
from electronic.models import Account  
from electronic.models import Product  
from electronic.views import ElectronicView
##from .models import destination
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404

# Secret key for the eSewa API (Use your actual secret key here)
SECRET_KEY = b"8gBm/:&EnhH.1/q"  # This is your UAT secret key




def home(request):
    laptop=Product.objects.filter(category_name=1)
    mobile=Product.objects.filter(category_name=5)
    headphone=Product.objects.filter(category_name=2)



    if 'phonenumber' not in request.session:

        seh=request.session.get('search_query')
        if seh is None:
            request.session['search_query'] = "laptop"


        electview = ElectronicView()

        recretrn=electview.recommend_products(request)

        return render(request, "home02.html", {'recodprdt': recretrn,"laptop":laptop[0:3],"mobile":mobile[0:3],"headphone":headphone[0:3]})

    
    account = Account.objects.get(phonenumber=request.session['phonenumber'])



    seh=request.session.get('search_query')
    if seh is None:
        request.session['search_query'] = "laptop"


    electview = ElectronicView()

    recretrn=electview.recommend_products(request)


    return render(request, "home02.html", {'recodprdt': recretrn, 'name':account,"laptop":laptop[0:3],"mobile":mobile[0:3],"headphone":headphone[0:3]})



def payment(request):
    url ="https://uat.esewa.com.np/epay/transrec"
    


    # Do this in production (EXPLAINED BELOW IN DETAIL )
    # Esewa test allows price upto Rs. 100 only 
    id = request.GET.get('id')
    prdt = Product.objects.get(product_id=id)

    return render(request,"payment02.html",{'pp':prdt})

def payment_failed(request):
    return render(request,'payment02.html')

