from django.contrib import admin

from app.models import Product
from app.models import Images,AttributeValues,Attribute,ProductAttribute

# Register your models here.

admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Attribute)
admin.site.register(AttributeValues)
admin.site.register(ProductAttribute)
