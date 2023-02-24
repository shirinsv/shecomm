from django.urls import path
from . import views

app_name='shopp_app'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:C_slug>/',views.allProdCat,name='product_by_category'),
    path('<slug:C_slug>/<slug:product_slug>/',views.prodetail,name='pro_catdetail')
    ]