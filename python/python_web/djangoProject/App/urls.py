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

from App import views

app_name = 'App'  # 应用名空间 ,在反向定位时用到了

urlpatterns = [
    path('home/', views.home, name='home'),
    path('main_app/', views.main_app, name='main_app'),
    path('main_app/<int:id>/', views.main_app, name='main_app'),
    path('main_app2/', views.main_app2, name='main_app2'),
    path('send_message/', views.send_message, name='send_message'),
]
