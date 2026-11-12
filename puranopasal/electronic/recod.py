from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_products(product_descriptions, top_n=5):
    vectorizer = TfidfVectorizer(stop_words='english')
    product_descriptions=Product.all().values_list('description', flat=True)
    tfid_matrix = vectorizer.fit_transform(product_descriptions)
    target_product= Product.objects.get(id=product_id)
    all_product=List(Product.objects.all() )
    target_index=all_product.index(target_product)
    consine_sim=cosine_similarity(tfid_matrix[target_index], tfid_matrix).flatten()
    similar_indices=consine_sim.argsort()[-top_n-1:-1][::-1]
    
    
    
    