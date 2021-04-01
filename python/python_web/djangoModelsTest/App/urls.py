from django.urls import path

from App import views

app_name = 'App'  # 应用名空间 ,在反向定位时用到了

urlpatterns = [
    path('index', views.Index.as_view(), name='Index'),
]
