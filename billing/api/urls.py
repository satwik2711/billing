from django.urls import path, include
from . import views

urlpatterns = [
    path('get', views.getall),
    path('get/category/<str:cat>/', views.getcategory),
    path('get/subcategory/<str:subcat>/', views.getsubcategory),
    path('get/name/<str:nam>/', views.getname),
    path('additem', views.add_item),
    path('update', views.update_item),

]