#from django.shortcuts import render, HttpResponse
from App.forms import RegistrationForm,LoginForm
from App.models import Student,CanteenEmployee
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# Sign Up View
@login_required
def index(request):
    return render(request,'html/index.html') 
    
def login(request):
    
    if request.method == 'POST':
        #user = Student.objects.get(username,password)
        #username = request.POST.get('username')
        #password = request.POST.get('password')


        user_object = Student.objects.get(username=username)
        if check_password(password, user_object.password):
            authenticate(username = username, password = password, model = "Student")
            login(request, user_object)
            return redirect('/App/index/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('/App/login/')
    else:
        return render(request,'html/login.html') 
    #return HttpResponse("login page")
def logoutUser(request):
    logout(request)
    return redirect('/App/login/')

def register(request):

    #form = RegistrationForm()
    if request.method == 'POST': 
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email') 
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2') 
    
        if password1 == password2:
            if Student.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('/App/register/')
                print("taken username")
            elif Student.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('/App/register/')
            else:
                user = Student.objects.create(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,mobile=mobile)
                user.save()
                return redirect('/App/login/')
        else:
            #user = Student.objects.create(username=username,password=password1,email=email,first_name=first_name,last_name=last_name,mobile=mobile)
            #user.save()
            messages.info(request,'password is not matches')
            return redirect('/App/register/')
        #form = RegistrationForm(request.POST)
        #if form.is_valid():
           # user=form.save()
           # return redirect('/App/login/')
    #context = {'form':form}
    else:
        return render(request, 'html/registration.html')

