from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_products(top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    product_descriptions=Product.all().values_list('description', flat=True)
    tfid_matrix = vectorizer.fit_transform(product_descriptions)
    all_product=Product.objects.all()
    searchname= searchhistory.objects.all().strip()
    for i in all_product:
        if i.brand_name == searchname:
            product_id=Product.objects.get(brand_name=i.brand_name)
            target_product= Product.objects.get(id=product_id)
            all_product=List(Product.objects.all() )
            target_index=all_product.index(target_product)
            consine_sim=cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
            similar_indices=consine_sim.argsort()[-top_n-1:-1][::-1]
            print(similar_indices)
    
    
    
    