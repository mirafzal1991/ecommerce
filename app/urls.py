from django.urls import path
from app.views import product_detail,add_product,index

urlpatterns = [
    path('index/',index,name='index'),
    path('product_detail/<int:product_id>',product_detail,name='product_detail'),
    path('add_product/',add_product,name = 'add_product')
]