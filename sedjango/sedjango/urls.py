"""sedjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from news.views import news,index,time
from member.views import login,logout,register,manage
from info.views import shop
from product.views import shop2
from cart.views import cart,addtocart,cartorder,cartok,cartordercheck,myorder,ECPayCredit


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',index),
    path('news/',news),
    path('login/',login),
    path('logout/',logout),
    path('register/',register),
    path('member/',manage),
    path('info/',shop),
    path('cart',cart),
    path('addtocart/<str:ctype>/',addtocart),
    path('addtocart/<str:ctype>/<int:productid>/',addtocart),
    path('cartorder/',cartorder),
    path('cartok/',cartok),
    path('cartordercheck/',cartordercheck),
    path('myorder/',myorder),
    path('creditcard/',ECPayCredit),
    path('product/',shop2),
    path('setime/',time),
]
