from django.urls import path

from App import views

app_names = 'App' # 应用名空间 ,在反向定位时用到了

urlpatterns = [
    # 不能以斜线开头
    path('home/', views.home, name='home'),
    path('apps/<path:app>/', views.apps, name='apps'),
    path('main_app/', views.main_app, name='main_app'),
    path('csrf/', views.csrf, name='csrf'),
    path('show/', views.show, name='show'),
    path('jinja2/', views.jinja2, name='jinja2'),

]
