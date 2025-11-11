from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.DO_NOTHING)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    
    @property
    def get_id(self):
        return self.user.id
    
    def __str__(self):
        return self.user.first_name

class ProductCategory(models.Model):
    name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField(null=False, default=0)
    discount = models.BooleanField(default=False)
    discount_price = models.PositiveIntegerField(null=False, default=0)
    discount_type=models.CharField(max_length=40, null=True)
    description=models.CharField(max_length=200)
    category = models.ForeignKey(ProductCategory, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.DO_NOTHING, null=True)
    product=models.ForeignKey('Product', on_delete=models.DO_NOTHING, null=True)
    email = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    mobile = models.CharField(max_length=20, null=True)
    order_date= models.DateField(auto_now_add=True, null=True)
    status=models.CharField(max_length=50, null=True, choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name
