from django.shortcuts import render,redirect
from customer.models import Customer
from customer.forms import CustomerModelForm
from django.contrib import messages
from app.models import Product
from django.db.models import Q

from app.forms import ProductForm,ProductModelForm

# Create your views here.

def customers(request):
    search_query = request.GET.get('search')
    if search_query:
        customer_list = Customer.objects.filter(Q(full_name__icontains=search_query)| Q(address__icontains=search_query))
    else:
        customer_list = Customer.objects.all()
    context = {
            'customer_list': customer_list,


        }

    return render(request,'customer/customer-list.html',context)

def add_customer(request):
    form = CustomerModelForm()
    if request.method == 'POST':
        form = CustomerModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {

        'form': form,

    }
    return render(request,'customer/add-customer.html',context)

def delete_customer(request,pk):
    customer = Customer.objects.get(id=pk)
    if customer:
        customer.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Customer successfully deleted'
        )
        return redirect('customers')

def edit_customer(request,pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerModelForm(instance=customer)
    if request.method == 'POST':
        form = CustomerModelForm(instance=customer,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')
    context = {

        'form': form,

    }
    return render(request,'customer/update-customer.html',context)


