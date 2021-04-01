from django.http import HttpResponse
from django.shortcuts import render

# from App.tasks import add


# Create your views here.
from django.views.generic import View, TemplateView


def index(request):
    # ...
    # tsend_email.delay()  # 执行任务
    # add.delay(1,2)  # delay(add函数的参数列表)
    # print(1 / 0)
    return HttpResponse('ok')


# fbv Function Base View 基于函数的视图
# cbv Class Base View 基于类的视图
# cbv 优点 继承 代码复用
class CBV(View):
    a = 10

    def get(self, request):
        return HttpResponse('GET')

    def post(self, request):
        return HttpResponse('post')

    def put(self, request):
        return HttpResponse('put')

    def delete(self, request):
        return HttpResponse('delete')


class MyTemplateView(TemplateView):
    template_name = 'template.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        print(kwargs)
        kwargs['name'] = 'yby'
        return kwargs
