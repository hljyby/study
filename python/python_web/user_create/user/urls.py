from django.urls import path

from user import views

app_name = 'user'  # 应用名空间 ,在反向定位时用到了

urlpatterns = [
    path('register', views.Register.as_view(), name='login'),
    path('login', views.Login.as_view(), name='login'),
    path('captcha', views.Captcha.as_view(), name='Captcha'),
    path('userlist', views.UserList.as_view(), name='userlist'),
    path('allpermission', views.PermissionList.as_view(), name='permission'),
    path('PermissionPost', views.PermissionPost.as_view(), name='PermissionPost'),
    path('UpdatePermission', views.UpdatePermission.as_view(), name='UpdatePermission'),
    path('DelPermission', views.DelPermission.as_view(), name='DelPermission'),
    path('GroupRule', views.GroupRule.as_view(), name='GroupRule'),
    path('TestQueryset', views.TestQueryset.as_view(), name='TestQueryset'),

]
