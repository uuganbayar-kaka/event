from django import forms
from django.forms import modelformset_factory
from .models import *
from django.contrib.auth.models import User


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'password']
        widgets = { 'password': forms.PasswordInput() }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['address', 'mobile']

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name', 'price', 'discount_price', 'discount_type', 'discount', 'description', 'product_image']

ProductImageFormSet = modelformset_factory(
    ProductImage,
    fields=('image',),
    extra=3,
    can_delete=True
)

#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# Category
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model=ProductCategory
        fields=['name', 'brand']

class ProductBrandForm(forms.ModelForm):
    class Meta:
        model=ProductBrand
        fields=['name', 'brand_image']