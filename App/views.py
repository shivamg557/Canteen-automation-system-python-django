#from django.shortcuts import render, HttpResponse
from App.forms import RegistrationForm,LoginForm
from App.models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Sign Up View

def index(request):
    products = Product.objects.all()
    context = {'products':products}
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
                return render(request,'html/admin.html')
            else:
                login(request,user)
                messages.success(request,"Login success")
                products = Product.objects.all()
                username=request.user
                context = {'username':username,'products':products}
                return render(request,'html/login.html',context)
        else:
            messages.success(request,"invalid credentials. Please try again")
            return redirect('/index/')
    else:
        messages.success(request,"404 Error")
        return redirect('/index/')

#@login_required
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        #cust = request.user.customer.objects.create(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        messages.success(request,"Plese login to place order")
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        return redirect('/index/')

    context = {'items':items,'order':order}
    return render(request,'html/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer= request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}

    context = {'items':items,'order':order}
    return render(request,'html/checkout.html',context)
    

    
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request,'html/index.html') 

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

def updateItem(request):
    data= json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action',action)
    print('productId',productId)

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