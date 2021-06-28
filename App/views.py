
from .models import *
from django.contrib.auth.forms import UserCreationForm
import datetime
# Create your views here.
from django.http import JsonResponse
import json
from .utils import cookieCart, cartData

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Sign Up View
@ csrf_exempt
def signUp(request):
    if request.method == 'POST':
        login_username = request.POST.get('username')
        login_password = request.POST.get('password')
        user=authenticate(username = login_username, password = login_password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                mess=messages.success(request,"Login success")
                context={'messages':mess}
                return redirect('/adminPanel',context)
            else:
                login(request,user)
                '''
                #alert(text='Login Success', title='', button='OK')
                mess=messages.success(request,"Login success")
                products = Product.objects.all()
                user=request.user
                customer,created = Customer.objects.get_or_create(user=user) 
                context = {'username':user,'products':products}
                #return render(request,'html/login.html',context)
                context={'messages':mess}'''
                return redirect('/home')
        else:
            mess=messages.success(request,"invalid credentials. Please try again")
            context={'messages':mess}
            return redirect('/',context)
        
    return render(request,'html/signUp.html') 

    
def user_logout(request):
    logout(request)
    message=messages.info(request, "Logged out successfully!")
    return redirect('/')
    #return render(request,'html/index.html',{'messages':message}) 

def index(request):
    products = Product.objects.all()
    user = request.user
    customer, created = Customer.objects.get_or_create(user=user)
    
    customer=request.user.customer
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    context = {'products':products,'order':order}
    return render(request,'html/index.html',context) 

@ csrf_exempt
def user_login(request):
    if request.method == 'POST':
        login_username = request.POST.get('username')
        login_password = request.POST.get('password')
        user=authenticate(username = login_username, password = login_password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.success(request,"Login success")
                return redirect('/adminPanel')
            else:
                login(request,user)
                #alert(text='Login Success', title='', button='OK')
                messages.success(request,"Login success")
                products = Product.objects.all()
                username=request.user
                context = {'username':username,'products':products}
                #return render(request,'html/login.html',context)
                return redirect('/home')
        else:
            messages.success(request,"invalid credentials. Please try again")
            return redirect('/')
    else:
        messages.success(request,"404 Error")
        return redirect('/')
    return render(request,'html/signUp.html') 
#@login_required
def cart(request):
    data= cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'html/cart.html',context)
    

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
        
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)

def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    time = datetime.datetime.now()
    context = {'items':items, 'order':order, 'cartItems':cartItems,'time':time}
    return render(request,'html/checkout.html',context)


def productDetail(request):
    return render(request,'html/productDetail.html')

@csrf_exempt
def payment(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        date = request.POST.get('date')
        time = request.POST.get('time')
        payment, created = Payment.objects.get_or_create(order=order,recieve_date=date,recieve_time=time,pay_status=True)
        
    return render(request,'html/payment.html')



####-------------------------------------------------------------Admin panel------------------------------------------------------------------####
def adminPanel(request):
    items = OrderItem.objects.all()
    #order = Payment.objects.all()
    context = {'items':items}
    return render(request,'html/admin.html',context)

def order(request):
    items=OrderItem.objects.all()
    context = {'items':items}
    return render(request,'html/order.html',context)

def product(request):
    pro = Product.objects.all()
    context={'products':pro}
    return render(request,'html/product.html',context)

def addProduct(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('price') and request.POST.get('image'):
            product = Product()
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.image = request.POST.get('image')
        
            product.save()
            messages.success(request,"Product added Sucessfully")
            return redirect('/product/',{'messages':messages})
    return render(request,'html/addProduct.html')

def delProduct(request):
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(request,"Product delete Sucessfully")
    return redirect('/product/',{'messages':messages})

def editProduct(request):
    product_id = request.GET.get('product_id')
    #product = Product.objects.get(id=product_id)
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.POST.get('image')
        messages.success(request,"Product updated Sucessfully")
        return redirect('/product/',{'messages':messages})
    return render(request,'html/updateProduct.html',{'product':product})

def register(request):

    if request.method == 'POST': 
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email') 
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2') 
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists!!')
            return redirect('/index/')

        if not username.isalnum():
            messages.error(request,'Username should be alphanumeric')
            return redirect('/index/')

        if User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists!!')
            return redirect('/index/')

        if password1 != password2:
            messages.error(request,'Password did not match!!')
            return redirect('/index/')
            
        user = User.objects.create_user(username,email,password1)
        user.first_name=first_name
        user.last_name=last_name
        user.save()
        messages.success(request,"Your account has been sucessfully created")
        return redirect('/index/')
      
    else:
        return render(request, 'html/index.html')