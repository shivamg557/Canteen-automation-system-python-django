#from django.conf.urls import url, include
from django.urls import path
from App import views

app_name = 'App'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
]