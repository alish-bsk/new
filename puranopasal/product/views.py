from django.shortcuts import render, redirect
from django.contrib import messages
from electronic.models import Account  
from electronic.models import Product,ProductView  
import time
import random
import string
import re
from datetime import date
from django.http import JsonResponse



def product_cost(request):

    if request.method == 'POST':

            model_name = request.POST['modelname']
            brand_name = request.POST['brandname']
            category=request.POST['category']
            delivery=request.POST['delivery']
            negotiable=request.POST['negotiable']
            date=request.POST['date']
            expiredate=request.POST['expiredate']
            price=request.POST['price']
            processor=request.POST['processor']
            ram=request.POST['ram']
            HDD=request.POST['HDD']
            screensize=request.POST['screensize']
            battery=request.POST['battery']
            img=request.FILES.get('div_picture')
            idnumber=request.POST['numberid']
            des=request.POST['description']
            numdes=len(des) 
           
            random_suffix = ''.join(random.choices( string.digits, k=4))
            unique_id = f"{random_suffix}"
      
            
            pattern = r"[@#$>!%*&_-]"

            pattnnum = r'^[0-9]+$'
            errors={}


            if not idnumber:
                if  re.search(pattern,model_name):
                    errors["modelname"]="Remove special character"

                if re.search(pattern,brand_name):
                    errors["brandname"]="Remove special character"


                if re.search(pattern,processor):
                    errors["processorname"]="Remove special character"

                            
                                
                if re.search(pattern,ram):
                     errors["ramname"]="Remove special character"

                                    
                if re.search(pattern,HDD):
                     errors["hddname"]="Remove special character"

                                        
                if re.search(pattern,screensize):
                     errors["screensizename"]="Remove special character"

                     
                                            
                if re.search(pattern,battery):
                    errors["batteryname"]="Remove special character"
                                      

                if numdes>=150:
                    errors["descriptionname"]="Text is more than 20"

                if errors:
                    return JsonResponse({"error": errors}, status=400)
                else:
                    prdt = Product(
                                    model_name = model_name,
                                    brand_name = brand_name,
                                    category_name_id = category,
                                    delivery = delivery,
                                    negotiable = negotiable,
                                    date = date,
                                    expiredate = expiredate,
                                    price = price,
                                    processor = processor,
                                    ram = ram,
                                    HDD = HDD,
                                    screensize = screensize,
                                    battery = battery,
                                    product_id=unique_id,
                                    image=img,
                                    description=des,
                                    phonenumber=request.session['phonenumber']
                                    )
                    prdt.save()
                    return JsonResponse({"success": True})

                
            if idnumber:

                if  re.search(pattern,model_name):
                    errors["modelname"]="Remove special character"

                if re.search(pattern,brand_name):
                    errors["brandname"]="Remove special character"


                if re.search(pattern,processor):
                    errors["processorname"]="Remove special character"

                            
                                
                if re.search(pattern,ram):
                     errors["ramname"]="Remove special character"

                                    
                if re.search(pattern,HDD):
                     errors["hddname"]="Remove special character"

                                        
                if re.search(pattern,screensize):
                     errors["screensizename"]="Remove special character"

                     
                                            
                if re.search(pattern,battery):
                    errors["batteryname"]="Remove special character"
                                      

                if numdes>=150:
                    errors["descriptionname"]="Text is more than 20"

                if errors:
                    return JsonResponse({"error": errors}, status=400)
                else:
                    prdt = Product.objects.get(product_id=idnumber)

                    
                    if prdt:
                        if prdt.phonenumber == request.session['phonenumber']:
                            prdt.model_name = model_name
                            prdt.brand_name = brand_name
                            prdt.category_name_id = category
                            prdt.delivery = delivery
                            prdt.negotiable = negotiable
                            prdt.date = date
                            prdt.expiredate = expiredate
                            prdt.price = price
                            prdt.processor = processor
                            prdt.ram = ram
                            prdt.HDD = HDD
                            prdt.screensize = screensize
                            prdt.battery = battery
                            prdt.product_id=idnumber
                            prdt.image=img
                            prdt.description=des
                            prdt.phonenumber=request.session['phonenumber']

                            prdt.save()


                            return JsonResponse({"success": True})


                                                      
                
                
                
            
            
                                    


                            
                            
def product_sold(request):
    if request.method == 'POST':
        id_number = request.POST['idnumber']
        sold = request.POST['sold']
        action = request.POST.get('submit')
        error={}

        pattnnum = r'^[0-9]+$'
        if action == "OK":
            if re.match(pattnnum,id_number):
                try:
                    prdt = Product.objects.get(product_id=id_number)


                    if prdt.phonenumber==request.session['phonenumber']:
                        if prdt:

                            prdt.sold = sold
                            prdt.save()

                            return JsonResponse({"success": True})
                        else:
                            error['idnumbername']='Id is not match'
                            return JsonResponse({"errors": error}, status=400)

                        
                    else:
                        error['idnumbername']='Id is not match'
                        return JsonResponse({"errors": error}, status=400)


                except:
                        error['idnumbername']='Id is not match'
                        return JsonResponse({"errors": error}, status=400)

                    
            else:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                return render(request, 'userads.html',{'prddelerr':'please enter number','acct':account}) 
            
        if action == "delete":                   
            if re.match(pattnnum,id_number):
                try:
                    prdt = Product.objects.get(product_id=id_number)
                    prdt.delete()
                    error['deletename']='Product is delete'

                    return JsonResponse({"errors": error})
                except:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    return render(request, 'userads.html',{'prddelerr':'Does not exist number','acct':account})       

            else:
                account = Account.objects.get(phonenumber=request.session['phonenumber'])

                return render(request, 'userads.html',{'prddelerr':'please enter number','acct':account}) 
    else:
        account = Account.objects.get(phonenumber=request.session['phonenumber'])

        return render(request, 'signinpage01.html',{'acct':account}) 
                            

def product_info(request):
    try:
        account = Account.objects.get(phonenumber=request.session['phonenumber'])
        id = request.GET.get('id')
        prdt = Product.objects.get(product_id=id)
        prdtvw=ProductView.objects.all()
        uservw=0
        for i in prdtvw:
            if i.product_id == prdt.id:
                if i.user_id==account.id:
                    uservw=0
                    break
            else:
                uservw=1
        if uservw==1:
            ProductView.objects.create(product_id=prdt.id,user_id=account.id)
        
        
    
        return render(request, 'information.html',{'acct':account,'prdsl':prdt}) 
    except:

        id = request.GET.get('id')

        prdt = Product.objects.get(product_id=id)


        return render(request, 'information.html',{'prdsl':prdt}) 
    