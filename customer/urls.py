from django.urls import path
from customer.views import CustomersTemplateView,AddCustomerView,DeleteCustomerView,EditCustomerView,send_email

urlpatterns = [
    path('customer-list/',CustomersTemplateView.as_view(), name='customers'),
    path('customer-add/',AddCustomerView.as_view(),name='add_customer'),
    path('customer/<int:pk>/delete',DeleteCustomerView.as_view(),name='delete'),
    path('customer/<int:pk>/update',EditCustomerView.as_view(),name='edit'),
    path('send-mail',send_email,name='send_email')

]