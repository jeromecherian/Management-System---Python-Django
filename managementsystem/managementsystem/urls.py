"""
URL configuration for managementsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from things.views import home
from things import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('category/',views.category,name='category'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('product/',views.product,name='product'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('delete_category/<int:id>',views.delete_category,name='delete_category'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('productedit/<int:id>',views.productedit,name='productedit'),
    path('updateproduct/<int:id>',views.updateproduct,name='updateproduct'),
    
]