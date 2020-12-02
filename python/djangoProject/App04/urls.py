"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from App04 import views

app_name = 'App04'  # 应用名空间 ,在反向定位时用到了

urlpatterns = [
    path('', views.index, name='index'),
    path('setcache/', views.SetCache, name='setcache'),
    path('checkuser/', views.checkUser, name='checkUser'),
    path('activeuser/<path:token>/', views.activeuser, name='activeuser'),

]
