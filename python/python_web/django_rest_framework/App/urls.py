from django.urls import path

from App import views

app_name = 'App'  # 应用名空间 ,在反向定位时用到了

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path('<column_id>', views.Index.as_view(), name='index'),
    path('create', views.CreateTab.as_view(), name='index'),
    path('retrieve/<int:pk>', views.RetrieveTab.as_view(), name='index'),
    path('login', views.Login.as_view(), name='login'),
    path('testtoken', views.TestToken.as_view(), name='token'),
    path('getdata', views.GetData.as_view(), name='getdata'),

]