from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from App import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
'''



urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^index/', views.index, name='index'),
    url(r'^admin/',admin.site.urls),
    url(r'^App/',include('App.urls')),
    
]

'''
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    #url(r'^$',views.index,name='index'),
    url(r'^',include('App.urls'))
]
