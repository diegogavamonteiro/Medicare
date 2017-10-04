"""medicare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static

from core.views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^home/?', index, name = 'index'),
    url(r'^about/?',about, name = 'about' ),
    url(r'^services/?',services, name = 'services' ),
    url(r'^contact/?',contact, name = 'contact' ),
    url(r'^customer_signup/?',customerSignup, name = 'customer_signup' ),
    url(r'^donate/?',donate, name = 'donate' ),
    url(r'^login/?',login, name = 'login' ),
    url(r'^reserve/?',reserve, name = 'reserve' ),
    url(r'^signup/?',signup, name = 'signup' ),
    url(r'^supplier_signup/?',supplier_signup, name = 'supplier_signup' ),
    url(r'^admin/', admin.site.urls),
]
