import sys

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

# 如果
from django.views.debug import technical_500_response


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(request.path)
        if request.user.is_authenticated or request.path.find('login') != -1 or request.path.find('captcha') != -1:
            return
        else:
            return redirect('APP03:login')

    def process_response(self, request, response):
        # 响应走这
        print('process_response')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('在自己的视图函数执行之前执行，每个函数返回的都是None ,如果返回render 或者 response 对象 则跳过自己写的view 直接到 process_response 里')
        return

    def process_exception(self, request, exception):
        # 异常处理 如果你是本地地址可以看到错误信息，如果不是调到登录页，可以照例写判断404 或者 500
        ip = request.META.get('REMOTE_ADDR')
        if ip == '127.0.0.1':
            return technical_500_response(request, *sys.exc_info())
        return redirect(reverse('APP03:login'))
