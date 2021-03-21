#from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'App'

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^user_login/', views.user_login, name='user_login'),
    url(r'^logout/',views.user_logout,name="user_logout"),
    url(r'^cart/',views.cart,name="cart"),
    url(r'^checkout/',views.checkout,name="checkout"),
    url(r'^update_item/',views.updateItem,name="update_item"),
]
