from django.shortcuts import render,redirect
from customer.models import Customer
from customer.forms import CustomerModelForm
from django.contrib import messages
from app.models import Product
from django.db.models import Q
from django.views.generic import TemplateView

from app.forms import ProductForm,ProductModelForm

# Create your views here.

# def customers(request):
#     search_query = request.GET.get('search')
#     if search_query:
#         customer_list = Customer.objects.filter(Q(full_name__icontains=search_query)| Q(address__icontains=search_query))
#     else:
#         customer_list = Customer.objects.all()
#     context = {
#             'customer_list': customer_list,
#
#
#         }
#
#     return render(request,'customer/customer-list.html',context)
class CustomersTemplateView(TemplateView):
    template_name = 'customer/customer-list.html'

    def get_context_data(self, **kwargs):
        customer = Customer.objects.all()
        search_query = self.request.GET.get('search')
        if search_query:
            customer = customer.filter(
                Q(name__icontains=search_query) | Q(billing_address__icontains=search_query)
            )

        context = super().get_context_data(**kwargs)
        context['customer'] = customer
        context['search_query'] = search_query
        return context



# def add_customer(request):
#     form = CustomerModelForm()
#     if request.method == 'POST':
#         form = CustomerModelForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('customers')
#
#     context = {
#
#         'form': form,
#
#     }
#     return render(request,'customer/add-customer.html',context)

class AddCustomerView(TemplateView):
    template_name = 'customer/add-customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CustomerModelForm()
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = CustomerModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')


# def delete_customer(request,pk):
#     customer = Customer.objects.get(id=pk)
#     if customer:
#         customer.delete()
#         messages.add_message(
#             request,
#             messages.SUCCESS,
#             'Customer successfully deleted'
#         )
#         return redirect('customers')
#
class DeleteCustomerView(TemplateView):

    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(id=self.kwargs['customer_id'])
        customer.delete()
        return redirect("customers")

# def edit_customer(request,pk):
#     customer = Customer.objects.get(id=pk)
#     form = CustomerModelForm(instance=customer)
#     if request.method == 'POST':
#         form = CustomerModelForm(instance=customer,data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('customers')
#     context = {
#
#         'form': form,
#
#     }
#     return render(request,'customer/update-customer.html',context)

class EditCustomerView(TemplateView):
    template_name = 'customer/update-customer.html'

    def get_context_data(self, **kwargs):
        form = CustomerModelForm(instance=Customer.objects.get(id=self.kwargs['customer_id']))
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        customer = Customer.objects.get(id=self.kwargs['customer_id'])
        form = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customers")

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return context


