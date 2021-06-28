#from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

app_name = 'App'

urlpatterns = [
    url(r'^$',views.signUp,name="signUp"),
    url(r'^home/', views.index, name='home'),
    url(r'^logout/',views.user_logout,name="user_logout"),
    url(r'^cart/',views.cart,name="cart"),
    url(r'^checkout/',views.checkout,name="checkout"),
    url(r'^update_item/',views.updateItem,name="update_item"),
    url(r'^productDetail/',views.productDetail,name="productDetail"),
    url(r'^payment/',views.payment,name="payment"),

    url(r'^adminPanel/',views.adminPanel,name="adminPanel"),
    url(r'^order/',views.order,name="order"),
    url(r'^product/',views.product,name="product"),
    url(r'^addProduct/',views.addProduct,name="addProduct"),
    url(r'^delProduct/',views.delProduct,name="delProduct"),
    url(r'^editProduct/',views.editProduct,name="editProduct"),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)