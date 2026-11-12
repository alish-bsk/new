from django.shortcuts import render
from electronic.models import Account,SearchHistory  # Adjust according to your app name
from django.contrib.postgres.search import SearchVector, SearchQuery
from rest_framework import renderers
# Create your views here.

# Create your views here.
from django.shortcuts import render
##from .models import destination
# Create your views here.
from electronic.models import Product,Category,ProductView
from datetime import date
import re;
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from django.views import View
from django.db.models import QuerySet 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
from .models import Product, ProductView
import numpy as np
from django.shortcuts import get_object_or_404



class ElectronicView:
    def recommend_products(self,request):
            seh = request.session.get('search_query')
            print(f"elct:{seh}")
            pattenrnnum=r'^[0-9]+$'

            #print(f"test:{sehchk}")
            if not seh:
                product_des=Product.objects.all()[::-1]
                return product_des [1:10]
            ##check category
            if seh is not None:
                ## check price number it return all product
                if re.match(pattenrnnum, seh):
                        product_des=Product.objects.all()[::-1]
                        return product_des[1:10]


                else:  
                        category=Category.objects.all().values('id')
                        prd_category = Category.objects.filter(category_name=seh).first()
                        ## prd_category is empty then return pass
                        if not prd_category:
                                pass
                        else:
                        ## check category same product all list

                                for i in category:
                                        if i.get('id')==prd_category.id:
                                                product_des=Product.objects.filter(category_name_id=prd_category.id)
                                                return product_des [1:10]

        ## calculation of TF value             
            vectorizer = TfidfVectorizer(stop_words='english')
        ## check value of model name in product data
            product_des=Product.objects.all().values_list('model_name', flat=True)
            product_all = [desc or "no description" for desc in product_des]
        ## calculation of IDf value
            tfid_matrix = vectorizer.fit_transform(product_all)
        ## match input data to number value
            if re.match(pattenrnnum, seh):
                    product_des=Product.objects.all()[::-1]
                    return product_des[1:10]


        ## check input data is empty or not
            if " " in seh:
                ## check input data split into two part

                    half = seh.split(" ")[1]
            
                ## check split data is number or not

                    if re.match(pattenrnnum, half):
                            srch = seh.split(" ")[0]
                            all_product=Product.objects.all()
                            ## calculation of cosine similarity product
                            for i in all_product:
                                    if i.model_name==srch:
                                            target_product= Product.objects.get(id=i.id)
                                            all_product=list(Product.objects.all() )
                                            target_index=all_product.index(target_product)
                                            consine_sim=cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
                                            similar_indices=consine_sim.argsort()[::-1]
                                            similar_products=[all_product[i] for i in similar_indices]

                                            return similar_products[0:10]

                                    if i.brand_name==srch:
                                            print(f'brand: {i.model_name} description: {i.description}')
                                            target_product= Product.objects.get(id=i.id)
                                            all_product=list(Product.objects.all() )
                                            target_index=all_product.index(target_product)
                                            consine_sim=cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
                                            print(f'Cosine Similarity: {list(consine_sim)}')
                                            similar_indices=consine_sim.argsort()[::-1]
                                            similar_products=[all_product[i] for i in similar_indices]

                                            return similar_products[0:10]

                                    
                    else:
                            all_product=Product.objects.all()
                            for i in all_product:
                                if i.model_name.lower() == seh.lower():
                                        target_product= Product.objects.get(id=i.id)
                                        all_product=list(Product.objects.all() )
                                        target_index=all_product.index(target_product)
                                        consine_sim=cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
                                        print(f'Cosine Similarity: {list(consine_sim)}')
                                        similar_indices=consine_sim.argsort()[::-1]
                                        similar_products=[all_product[i] for i in similar_indices]

                                        return similar_products[0:10]
                                

                                if i.brand_name.lower()==seh.lower():
                                        print("hello brand")
                                        target_product= Product.objects.get(id=i.id)
                                        all_product=list(Product.objects.all() )
                                        target_index=all_product.index(target_product)
                                        consine_sim=cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
                                        print(f'Cosine Similarity: {list(consine_sim)}')
                                        similar_indices=consine_sim.argsort()[::-1]

                                        similar_products=[all_product[i] for i in similar_indices]

                                        return similar_products[0:10]

                                    
                                    
                                    
                                    
                                    
            else:
                    
                    all_product=Product.objects.all()
                    for i in all_product:
                            if i.model_name.lower()==seh.lower():
                                    target_product= Product.objects.get(id=i.id)
                                    all_product=list(Product.objects.all() )
                                    target_index=all_product.index(target_product)
                                    consine_sim=cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
                                    print(f'Cosine Similarity: {list(consine_sim)}')
                                    similar_indices=consine_sim.argsort()[::-1]
                                    similar_products=[all_product[i] for i in similar_indices]

                                    return similar_products[0:10]

                            if i.brand_name.lower()==seh.lower():
                                    target_product= Product.objects.get(id=i.id)
                                    all_product=list(Product.objects.all() )
                                    target_index=all_product.index(target_product)
                                    consine_sim=cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
                                    print(f'Cosine Similarity: {list(consine_sim)}')
                                    similar_indices=consine_sim.argsort()[::-1]
                                    similar_products=[all_product[i] for i in similar_indices]

                                    print(f'Similar indices: {"brand name"}')
                                    return similar_products[0:10]
                                                                       

                    



    def electronicall(self,request):
            if 'phonenumber' not in request.session:
                    recretrn=self.recommend_products(request)
                    sl=Product.objects.all()
                    today_date = date.today()
                    return render(request, 'allproductelect.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})

            else:
                    
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    prdtvw=ProductView.objects.filter(user_id=account.id)

                    if not prdtvw:
                            sl=Product.objects.all()
                            today_date = date.today()
                            return render(request, 'allproductelect.html',{'name': account,'prdsl':sl,'today_date':today_date})


                    
                    else:
                        sl=Product.objects.all()
                        today_date = date.today()


                        # Products viewed by this user
                        viewed_products = Product.objects.filter(
                                productview__user_id=account.id
                        ).distinct()

                        if not viewed_products.exists():
                                return Product.objects.all()[:]

                        # IDs of products already viewed
                        viewed_ids = set(
                                viewed_products.values_list("id", flat=True)
                        )

                        # Create content from user's viewed products
                        user_content = []

                        for product in viewed_products:


                                content = " ".join([
                                str(product.model_name or ""),
                                str(product.brand_name or ""),
                                ])

                                user_content.append(content)



                        # Combine all viewed products into ONE user profile
                        user_profile = " ".join(user_content)

                        # Get products user has NOT viewed
                        other_products = list(
                                Product.objects.exclude(
                                id__in=viewed_ids
                                )
                        )

                        if not other_products:
                                return []

                        # Content of other products
                        other_content = []

                        for product in other_products:

                                content = " ".join([
                                str(product.model_name or ""),
                                str(product.brand_name or ""),
                                ])

                                other_content.append(content)

                        # TF-IDF
                        documents = [user_profile] + other_content



                        vectorizer = TfidfVectorizer(
                                stop_words="english"
                        )

                        vectors = vectorizer.fit_transform(documents)

                        # Compare User 1 profile with every other product
                        similarity = cosine_similarity(
                                vectors[0:1],
                                vectors[1:]
                        )[0]
                        recommendations=[]   

                        for product, score in zip(
                               other_products,
                               similarity
                       ):
                                recommendations.append({
                                "product": product,
                                "score": float(score)
                                })

                        # Highest similarity first
                        recommendations.sort(
                                key=lambda x: x["score"],
                               reverse=True
                       )

                        userview=[recommendations[i]['product'] for i in range(0,len(recommendations)) ]

                        
                        #print(f"product my:{recommendations}")    
                        return render(request, 'allproductelect.html',{'name': account,'prdsl':userview,'today_date':today_date})
 
                



                    



    def laptop_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    recretrn=self.recommend_products(request)

                    sl=Product.objects.all()
                    today_date = date.today()
                    return render(request, 'laptop_list.html',{'name': account,'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            except:
                    sl=Product.objects.all()
                    recretrn=self.recommend_products(request)

                    today_date = date.today()
                    return render(request, 'laptop_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})

    def mobile_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    sl=Product.objects.all()
                    today_date = date.today()

                    return render(request, 'mobile_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
            except:
                    sl=Product.objects.all()
                    recretrn=self.recommend_products(request)

                    today_date = date.today()

                    return render(request, 'mobile_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
    def speaker_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    recretrn=self.recommend_products(request)

                    sl=Product.objects.all()
                    today_date = date.today()

                    return render(request, 'speaker_list.html',{'name': account,'prdsl':sl,'today_date':today_date})
            except:
                    sl=Product.objects.all()
                    recretrn=self.recommend_products(request)

                    today_date = date.today()

                    return render(request, 'speaker_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
    def headphone_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    sl=Product.objects.all()
                    today_date = date.today()

                    return render(request, 'headphone_list.html',{'name': account,'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            except:
                    sl=Product.objects.all()
                    recretrn=self.recommend_products(request)
                    today_date = date.today()
                    return render(request, 'headphone_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
    def tv_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    recretrn=self.recommend_products(request)
                    sl=Product.objects.all()
                    today_date = date.today()

                    return render(request, 'tv_list.html',{'name': account,'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            except:
                    sl=Product.objects.all()
                    recretrn=self.recommend_products(request)
                    today_date = date.today()

                    return render(request, 'tv_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            
    def refrigerator_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    sl=Product.objects.all()
                    today_date = date.today()
                    recretrn=self.recommend_products(request)


                    return render(request, 'refrigerator_list.html',{'name': account,'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            except:
                    sl=Product.objects.all()
                    today_date = date.today()
                    recretrn=self.recommend_products(request)


                    return render(request, 'refrigerator_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
    def microoven_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    recretrn=self.recommend_products(request)
                    sl=Product.objects.all()
                    today_date = date.today()

                    return render(request, 'microoven_list.html',{'name': account,'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            except:
                    sl=Product.objects.all()
                    recretrn=self.recommend_products(request)
                    today_date = date.today()

                    return render(request, 'microoven_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            
    def vaccum_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    recretrn=self.recommend_products(request)
                    sl=Product.objects.all()
                    today_date = date.today()

                    return render(request, 'vacuum_list.html',{'name': account,'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            except:
                    sl=Product.objects.all()
                    recretrn=self.recommend_products(request)
                    today_date = date.today()

                    return render(request, 'vacuum_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
                
    def iron_list(self,request):
            try:
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    recretrn=self.recommend_products(request)
                    sl=Product.objects.all()
                    today_date = date.today()

                    return render(request, 'iron_list.html',{'name': account,'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})
            except:
                    sl=Product.objects.all()
                    recretrn=self.recommend_products(request)
                    today_date = date.today()

                    return render(request, 'iron_list.html',{'prdsl':sl,'today_date':today_date,'recodprdt': recretrn})


    def search_list(self,request):
            seh=request.POST['search-data'].strip()
            today_date = date.today()

            pattern = r"^[a-zA-Z]+ [0-9]+$"                
            pattnnum = r'^[0-9]+$'
            patternstr=r"^[a-zA-Z0-9']"
            patternstrnex = r"^[a-zA-Z0-9'  ]+$"
            #print(f'check:{seh.lower()}')
            request.session['search_query'] = seh
            recretrn=self.recommend_products(request)

            category_map = {
                    'laptop': 1,
                    'headphone': 2,
                    'iron': 3,
                    'microoven': 4,
                    'mobile': 5,
                    'refrigerator': 6,
                    'speaker': 7,
                    'tv': 8,
                    'vacuum': 9
                    }


            if re.match(pattnnum,seh):
                    List = []
                    sefil = Product.objects.all()

                    for sl in sefil:
                            ## Compares the products price to the users input
                            ## If they match exactly the product is added to the result list
                            if str(sl.price) == str(seh):
                                    List.append(sl)
                   ## Display search products on the "searchelec.html" page
                    return render(request, "searchelec.html", {'serlist': List,'today_date': today_date,'recodprdt': recretrn})
            
            if re.match(pattern,seh):

                    List = []
                    ## Retrieves all products from the database
                    sefil = Product.objects.all()
                    half = seh.split(" ")
                    name=half[0]
                    prc=half[1]
                    recretrn=self.recommend_products(request)

                    category_name = category_map.get(name.lower())


                    for sl in sefil:
                            if category_name is not None:
                                    ## Compares the products price to the users input and category name to user input
                                    ## If they match exactly the product is added to the result list
                                    if str(sl.price) == prc and sl.category_name_id == category_map[name] :
                                            List.append(sl)

                            
                            else:
                                    ## Compares the products price to the users input and brand name to user input
                                    ## If they match exactly the product is added to the result list
                                    if str(sl.price) == prc and str(sl.brand_name).lower() == name.lower() :
                                            List.append(sl)
                                    ## Compares the products price to the users input and model name to user input
                                    ## If they match exactly the product is added to the result list
                                    if str(sl.price) == prc and str(sl.model_name).lower() == name.lower() :
                                            List.append(sl)



                      ## Display search products on the "searchelec.html" page
                    return render(request, "searchelec.html", {'serlist': List,'today_date': today_date,'recodprdt': recretrn})
                    
            if re.match(patternstrnex,seh):
                    List = []
                    sefil = Product.objects.all()
                    category_name = category_map.get(seh.lower())
                    recretrn=self.recommend_products(request)

                    if category_name is not None:
                            for sl in sefil:
                                    ## Compares  category name to user input.
                                    ## If they match exactly the product is added to the result list
                                    if sl.category_name_id == category_map[seh.lower()]:
                                            List.append(sl)
                            

                    else:
                            for sl in sefil:
                                    ## Compares brand name to user input.
                                    if str(sl.brand_name).lower() == str(seh).lower() :
                                            List.append(sl)
                            
                                    ## Compares brand name to user input.

                                    if (str(sl.model_name).lower()).strip() == str(seh).lower() :
                                            List.append(sl)
                            
                    ## Display search products on the "searchelec.html" page
                    return render(request, "searchelec.html", {'serlist': List,'today_date': today_date,'recodprdt': recretrn})

                                                
    
                        
            else:
                    if 'phonenumber' not in request.session:
                            recretrn=self.recommend_products(request)

                            return render(request, "electron01.html")
                    account = Account.objects.get(phonenumber=request.session['phonenumber'])
                    recretrn=self.recommend_products(request)

                    return render(request, "electron01.html", {'name': account,'recodprdt': recretrn})
            
class ElectronicExct(View):
    def get(self,request):
        if 'phonenumber' not in request.session:
                electronic_view = ElectronicView()
                return electronic_view.electronicall(request)
                ##return render(request, "electron01.html")
        
        account = Account.objects.get(phonenumber=request.session['phonenumber'])
        electronic_view = ElectronicView()
        return electronic_view.electronicall(request)


        #return render(request, "electron01.html", {'name': account})
    def post(self,request):
            electronic_view = ElectronicView()
            valuebtnserc = request.POST.get('search')

            valuebtnelect = request.POST.get('elect')
            valuebtnlapt = request.POST.get('laptop')
            valuebtnmb = request.POST.get('mobile')
            valuebtnspk = request.POST.get('speaker')
            valuebtnhdp = request.POST.get('headphone')
            valuebtntv = request.POST.get('tv')
            valuebtnrefg = request.POST.get('refrigerator')
            valuebtnmico = request.POST.get('microoven')
            valuebtnvacm = request.POST.get('vaccum')
            valuebtnirn = request.POST.get('iron')
            ## print(f"Value of search button: {valuebtn}")
            if valuebtnserc == "search":
                    return electronic_view.search_list(request)
            if valuebtnelect == "elect":
                    return electronic_view.electronicall(request)



            if valuebtnlapt == "laptop":
                    return electronic_view.laptop_list(request)

            if valuebtnmb == "mobile":
                    return electronic_view.mobile_list(request)

            if valuebtnspk == "speaker":
                    return electronic_view.speaker_list(request)

            if valuebtnhdp == "headphone":
                    return  electronic_view.headphone_list(request)

            if valuebtntv == "tv":
                    return electronic_view.tv_list(request)

            if valuebtnrefg == "refrigerator":
                    return electronic_view.refrigerator_list(request)

            if valuebtnmico == "microoven":
                    return electronic_view.microoven_list(request)

            if valuebtnvacm == "vaccum":
                    return electronic_view.vaccum_list(request)

            if valuebtnirn == "iron":
                    return electronic_view.iron_list(request)

      
