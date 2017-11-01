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
from django.contrib.auth.views import login, logout

from core import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^home/?', views.index, name='home'),
    url(r'^about/?', views.about, name='about'),
    url(r'^services/?', views.services, name='services'),
    url(r'^contact/?',views.contact, name = 'contact' ),
    url(r'^customer_signup/?',views.customer_register, name = 'customer_signup' ),
    url(r'^donate/?',views.donate, name = 'donate' ),
    url(r'^login/?',  login, {'template_name': 'login.html'}, name = 'login' ),
    url(r'^logout/?',  logout, {'next_page': 'home'}, name = 'logout' ),
    url(r'^reserve/?',views.reserve, name = 'reserve' ),
    url(r'^signup/?',views.signup, name = 'signup' ),
    url(r'^supplier_signup/?', views.supplier_register, name='supplier_signup'),
    url(r'^admin/', admin.site.urls),
]
