from django.shortcuts import render, redirect
from django.contrib import messages
from electronic.models import Account  
from electronic.models import Product
from django.contrib.auth.hashers import make_password, check_password  # Import for password hashing
from datetime import date
from django.views import View
from signup.views import SignUpView
from django.http import JsonResponse

import re
class SignInView:
    def __init__(self,phone_number=None,password=None):
        self._phone_number = phone_number
        self._password = password

    
    def signin(self,request):
        today_date = date.today() 
        if request.method == 'POST':

            pattnum = r'^[0-9]+$'
            if not self._phone_number:
                if not self._password:
                    return render(request, 'signin01.html',{'errs':'fill phonenumber and password'})

            if not self._phone_number:
                return render(request, 'signin01.html',{'errs':'fill phonenumber and password'})

            if not self._password:
                return render(request, 'signin01.html',{'errs':'fill phonenumber and password'})
            
            try:
                account = Account.objects.get(phonenumber=self._phone_number)
                check=SignUpView()

                if check.sha1(self._password)==account.password:  # Validate the password
                    request.session['phonenumber']=account.phonenumber
                    request.session['password']=account.password
                    request.session['first_name']=account.first_name
                    account = Account.objects.get(phonenumber=self._phone_number)

                    try:
                        prdt = Product.objects.all()
                        return render(request, "signinpage02.html", {'acct':account,'prdsl':prdt,"today_date": today_date})
        


                    except:
                        return render(request, "signinpage02.html", {'acct':account})
                    

                else:
                    return render(request, 'signin01.html',{'errs':'Incorrect password'})

            except Account.DoesNotExist:
                messages.error(request, 'Phone number not found.')
                return render(request, 'signin01.html',{'errs':'Phone number not found'})

        if 'phonenumber' not in request.session:
            return render(request, "signin01.html")

        return render(request, "signinpage02.html", {'name': request.session['first_name']})



    
    def logout(self,request):
        request.session.flush()  # Clear all session data
        messages.success(request, 'You have been logged out successfully.')
        return render(request, "signin01.html")
    
    
class SignPageView(View):
    def __init__(self,first_name=None, middle_name=None, last_name=None, location=None, img=None, valuebtn=None):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._location = location
        self._img = img
        self._valuebtn = valuebtn

    def signinpage_btn(self,request):
        if request.method == 'POST':
            valuebtn = request.POST.get('submit')
            print(f"Value of submit button: {valuebtn}")


            today_date = date.today()

            try:
                account = Account.objects.get(phonenumber=request.session.get('phonenumber', None))
                prdt = Product.objects.all()

                if valuebtn == "Adspost":
                    return render(request, "userads.html", {'acct': account, 'prdsl': prdt, "today_date": today_date})

                if valuebtn == "All":
                    return render(request, "userall.html", {'acct': account, 'prdsl': prdt, "today_date": today_date})

                if valuebtn == "Sold":
                    return render(request, "usersold.html", {'acct': account, 'prdsl': prdt, "today_date": today_date}) 
                if valuebtn == "Expire":
                    return render(request, "userexpire.html", {'acct': account, 'prdsl': prdt, "today_date": today_date}) 

            except Exception as e:
                return render(request, "signinpage02.html", {'acct': account, 'prdsl': prdt, "today_date": today_date})
        else:
            return render(request, "signinpage02.html", {'acct': None, 'prdsl': None, "today_date": date.today()})

    def signinpage(self, request):

        today_date = date.today() 
        errors = {}


        if 'phonenumber' not in request.session:
            return render(request, "signin01.html")
        else:
            if request.method == 'POST':
                pattern = r"^[a-zA-Z][a-zA-Z' ]*$"
                if not self._first_name and not self._last_name and not self._location:
                    if not self._img :
                        account = Account.objects.get(phonenumber=request.session['phonenumber'])
                        prdt = Product.objects.all()

                        return render(request, 'signinpage02.html',{'acct':account,'prdsl':prdt,"today_date": today_date})



                if not self._first_name and not self._last_name and not self._location:
                    if self.img !="":
                        account = Account.objects.get(phonenumber=request.session['phonenumber'])
                        account.image=self.img
                        account.save()
                        prdt = Product.objects.all()

                        return render(request, 'signinpage02.html',{'acct':account,'prdsl':prdt,"today_date": today_date})

    
                

                # First name: required
                if not re.fullmatch(pattern, self._first_name.strip()):
                    errors["firstname"] = "Invalid format"

                # Middle name: optional
                if self._middle_name.strip() and not re.fullmatch(
                    pattern, self._middle_name.strip()
                ):
                    errors["middlename"] = "Invalid format"

                # Last name: required
                if not re.fullmatch(pattern, self._last_name.strip()):
                    errors["lastname"] = "Invalid format"

                # Location: required; adjust allowed characters if needed
                if not re.fullmatch(pattern, self._location.strip()):
                    errors["locationname"] = "Invalid format"

                if errors:
                    return JsonResponse({"errors": errors}, status=400)

                else:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])

                    if self._middle_name == "":
                        account.first_name = self._first_name
                        account.last_name = self._last_name
                        account.location = self._location
                        account.image=self._img
                        account.save()
                        prdt = Product.objects.all()


                        return JsonResponse({"success": True})


                    else:
                        account.first_name = self._first_name

                        account.middle_name = self._middle_name
                        account.last_name = self._last_name
                        account.location = self._location
                        account.image=self._img
                        account.save()
                        prdt = Product.objects.all()
                        errors={"successname":"Successfully rename all"}

                        return JsonResponse({"errors": errors}, status=400)




                            

                                    






    
                


        account = Account.objects.get(phonenumber=request.session['phonenumber'])
        prdt = Product.objects.all()

        return render(request, "signinpage02.html", {'acct':account,'prdsl':prdt,"today_date": today_date})


class SignInExct(View):
    def get(self, request):
        today_date = date.today() 
        if  'phonenumber' not in request.session:
            return render(request, 'signin01.html')        

        else:
            account = Account.objects.get(phonenumber=request.session['phonenumber'])

            prdt = Product.objects.all()
            return render(request, "signinpage02.html", {'acct':account,'prdsl':prdt,"today_date": today_date})


    def post(self, request):


        valuebtnsign = request.POST.get('signin')
        valuelgt = request.POST.get('logout')


        print(f"Value of submit button: {valuebtnsign}")
        if valuebtnsign is not None:
            if valuebtnsign == "signin":
                phone_number= request.POST['number']
                pssd = request.POST['password']
                sigin_view = SignInView(phone_number, pssd)
                return sigin_view.signin(request)
        if valuelgt is not None:
            if valuelgt == "logout":
                sigin_view = SignInView( )

                return sigin_view.logout(request)
        else:
            return render(request, 'signin01.html')

class SignInPageExct(View):
    def get(self, request):
        today_date = date.today() 

        account = Account.objects.get(phonenumber=request.session['phonenumber'])

        prdt = Product.objects.all()
        return render(request, "signinpage02.html", {'acct':account,'prdsl':prdt,"today_date": today_date})


    def post(self, request):
        valuebtnads = request.POST.get('prdtads')

        valuebtnprf = request.POST.get('submit')

        
        if valuebtnads is not None:
            today_date = date.today()
            account = Account.objects.get(phonenumber=request.session.get('phonenumber', None))
            prdt = Product.objects.all()

            if valuebtnads == "Adspost":
                return render(request, "userads.html", {'acct': account, 'prdsl': prdt, "today_date": today_date})

            if valuebtnads == "All":

                return JsonResponse({
                    "success": True,
    "products": [    

        {
            "product_id": prdt.product_id,
            "model_name": prdt.model_name,
            "price": prdt.price,
            "image": prdt.image.url if prdt.image else ""
        }
        for prdt in prdt
        if prdt.phonenumber == account.phonenumber
    ]
                })


            if valuebtnads == "Sold":
                return JsonResponse({
                    "success": True,
    "products": [    

        {
            "product_id": prdt.product_id,
            "model_name": prdt.model_name,
            "price": prdt.price,
            "image": prdt.image.url if prdt.image else ""
        }
        for prdt in prdt
        if prdt.phonenumber == account.phonenumber
        if prdt.sold == "sold"

    ]
                })
            
            if valuebtnads == "Expire":
                return JsonResponse({
                    "success": True,
    "products": [    

        {
            "product_id": prdt.product_id,
            "model_name": prdt.model_name,
            "price": prdt.price,
            "image": prdt.image.url if prdt.image else ""
        }
        for prdt in prdt
        if prdt.phonenumber == account.phonenumber
        if prdt.expiredate <= today_date

    ]
                })


            








        if valuebtnprf is not None:
            if valuebtnprf=='OK':
                print(f"click button hello")
                first_name = request.POST['firstname']
                middle_name = request.POST['middlename']
                last_name = request.POST['lastname']
                location=request.POST['location']
                img=request.FILES.get('profile_picture')  

                sigin_view = SignPageView(first_name, middle_name, last_name, location, img)
                return sigin_view.signinpage(request)
                
        else:
            sigin_view = SignPageView()
            return sigin_view.signinpage_btn(request)       


       
        
    