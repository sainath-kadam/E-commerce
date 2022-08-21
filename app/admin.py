from atexit import register
from django.contrib import admin
from .models import Customer,OrderPlaced,Product,Cart

# Register your models here.
admin.site.register(Customer)
admin.site.register(OrderPlaced)
admin.site.register(Product)
admin.site.register(Cart)


