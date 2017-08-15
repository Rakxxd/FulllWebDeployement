"""first_project URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from first_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),   #specifies index page www.websitename.com/
    url(r'^first_app/',include('first_app.urls')),   #conatiner for all urls in first_app.urls.py redirecting to www.websitenamee.com/first_app/*
    url(r'^admin/', admin.site.urls),
]
