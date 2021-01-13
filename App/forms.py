from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from App.models import Student, CanteenEmployee
# Sign Up Form
class RegistrationForm(forms.ModelForm):
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #email = forms.EmailField()
    #username=forms.CharField()
    #password=forms.CharField(max_length=15, widget=forms.PasswordInput)
    #conform_password=forms.CharField(max_length=15, widget=forms.PasswordInput)
    class Meta:
        model = Student
        fields = ('first_name','last_name','mobile','email','username','password')
             
    #def save(self,commit=True):
       # user = super(RegisterForm, self).save(commit=False)
        
       # user.first_name = self.cleaned_data['first_name']
        #user.last_name = self.cleaned_data['last_name']
        #user.email = self.cleaned_data['email']
        #user.username = self.cleaned_data['username']
        #user.password1 = self.cleaned_data['password1']
        #user.password2 = self.cleaned_data['password2']
    
        #if commit:
            #user.save()
       # return user

class LoginForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username','password']