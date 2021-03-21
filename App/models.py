from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class CanteenEmployee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,default='')
    job = models.CharField(max_length=50)
    loginId = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
  
    def __str__(self):
        return self.first_name

class Student(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    mobile = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100,default='',unique=True)
    username = models.CharField(max_length=10,unique=True,primary_key=True)
    password = models.CharField(max_length=15,unique=True)

    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.first_name +" "+self.last_name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=100,null=True)
    price = models.FloatField()
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True,blank=True,null=True)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product= models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order= models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order= models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address= models.CharField(max_length=100,null=True)
    city= models.CharField(max_length=100,null=True)
    state= models.CharField(max_length=100,null=True)
    zipcode= models.CharField(max_length=100,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    




    