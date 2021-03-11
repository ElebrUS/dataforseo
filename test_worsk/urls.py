"""test_worsk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from users import views as vs
from django.contrib.auth import views as a_vs

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', vs.home, name='home'),
    url(r'^login/$', a_vs.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$', a_vs.LogoutView.as_view(next_page='login'), name='logout'),
    url(r'^signup/$', vs.signup, name='signup'),
    path('locations/', include('locations.urls')),
    path('orders/', include('orders.urls')),
]
