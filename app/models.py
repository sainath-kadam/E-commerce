from distutils.command.upload import upload

from pyexpat import model
from sre_parse import CATEGORIES, State
from statistics import mode
from telnetlib import STATUS
from tkinter import CASCADE
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from email.policy import default


from django.db import models


# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.DateField(max_length=2000)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    State = models.CharField(max_length=50)

    def __str__(self):
      return str(self.id)




    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50)


# class product(models.Model):
#     title = models.CharField(max_length=100)
#     selling_pricerice = models.FloatField()
#     discounted_price=models.FloatField()
#     description = models.TextField(max_length=1000)
#     brand =models.CharField(max_length=100)
# #     category = models.CharField()
# #     product_image = mode.ImageField(upload_to = 'productimg')

#     def __str__(self):
#        return str(self.id)
CATEGORY_CHOICES =(
    ('M','Mobile'),
    ('L','Laptop'),
    ('MN', 'Men'),
    ('WM','Women'),
    ('KD','Kids'),

)
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50,null=True)
    category =models.CharField(choices=CATEGORY_CHOICES,max_length=2,null=True)
    subcategory=models.CharField(max_length=50,default="",null=True)
    price=models.IntegerField(default=0,null=True)
    desc=models.CharField(max_length=300,null=True)
   
    # image=models.ImageField(upload_to="images" ,default="",null=True)

    def __str__(self):
        return self.product_name



class Cart(models.Model):
#     User= models.ForeignKey(User,on_delete=models.CASCADE)
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
      return str(self.id)