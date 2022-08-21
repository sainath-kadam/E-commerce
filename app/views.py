from unicodedata import category
from django import views
from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Cart,OrderPlaced
from math import ceil





# def home(request):
    
#    return render(request, 'app/home.html')
# class ProductView(View):
#    def get(self, request):
#     Mens =Product.objects.filter(category="MW")
#     Womens =Product.objects.filter(category="WM")
#     Kids =Product.objects.filter(category="KD")
#     Laptops =Product.objects.filter(category="L")
#     Mobiles =Product.objects.filter(category="M")
#     return render(request,'app/home.html',{'Mens':Mens,'Womens':Womens,'Kids':Kids,'Laptops':Laptops,'Mobiles':Mobiles})

def home(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'app/home.html', params)
def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
