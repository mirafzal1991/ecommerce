from django import forms
from customer.models import Customer

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    email_from = forms.EmailField(max_length=200)
    email_to = forms.EmailField(max_length=200)

