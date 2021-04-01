from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from App.models import User


def index(request):
    return HttpResponse("Hellow world")


def home(request):
    # return HttpResponse('首页')
    users = User.objects.all()
    print(users)
    return render(request, 'home.html', context=locals())


def apps(request, app=0):
    print(app)
    print(request.GET.get('username'))
    print(request)
    print(request.GET)
    print(request.POST)
    print(request.POST.get('username'))
    print(request.META)
    HttpResponseRedirect(reverse("App:home"))
    return HttpResponse(app)


def main_app(request):
    users = [{'username': 'yby'}, {'username': 'yn'}, {'username': 'cly'}]
    title = '测试'
    name = "yby"
    return render(request, 'index.html', context=locals())


@csrf_exempt
def csrf(request):
    return HttpResponse({'name': 'js', 'lan': 'china'})


def show(request):
    return render(request, 'show.html', context={'title': 'show'})


def jinja2(request):
    return render(request, 'jinja2.html')
