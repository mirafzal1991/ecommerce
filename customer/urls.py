from django.urls import path
from customer.views import CustomersTemplateView,AddCustomerView,DeleteCustomerView,EditCustomerView

urlpatterns = [
    path('customer-list/',CustomersTemplateView, name='customers'),
    path('customer-add/',AddCustomerView,name='add_customer'),
    path('customer/<int:pk>/delete',DeleteCustomerView,name='delete'),
    path('customer/<int:pk>/update',EditCustomerView,name='edit')

]