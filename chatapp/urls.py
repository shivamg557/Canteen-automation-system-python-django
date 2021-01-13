from django.contrib import admin
from django.conf.urls import url,include
from App import views


urlpatterns = [
    url(r'^$',views.login,name='login'),
    url(r'^admin/',admin.site.urls),
    url(r'^App/',include('App.urls')),
    
]
