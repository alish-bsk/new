from django.db import models
from django.contrib.auth.models import User  # Import the User model

class Account(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phonenumber= models.BigIntegerField(max_length=10)
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')

   


class Category(models.Model):
    # Define fields that match the existing Category table structure
    category_name = models.CharField(max_length=100)  # Adjust as needed


    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_id = models.BigIntegerField(max_length=100)
    model_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    category_name= models.ForeignKey('electronic.Category', on_delete=models.CASCADE)  
    image = models.ImageField(upload_to='pics')
    price = models.BigIntegerField(max_length=100)
    date = models.DateField()  
    expiredate = models.DateField() 
    phonenumber = models.BigIntegerField(max_length=10) 
    delivery = models.CharField(max_length=100)
    negotiable = models.CharField(max_length=100)
    
    processor = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    HDD = models.CharField(max_length=100)
    screensize = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    sold = models.CharField(max_length=100)
    description = models.TextField(max_length=100, null=True, blank=True)


    

    def __str__(self):
        return f"{self.model_name} - {self.brand_name} "


class SearchHistory(models.Model):
    search_query = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.user.username} searched for '{self.search_query}' at {self.timestamp}"

class ProductView(models.Model):
    user=models.ForeignKey('electronic.Account',on_delete=models.CASCADE)
    product=models.ForeignKey('electronic.Product',on_delete=models.CASCADE)
    view_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    