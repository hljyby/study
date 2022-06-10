import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import ArticleContent, ArticleTab
from App.SMS import send_messages


def home(request):
    # return HttpResponse('home')
    return render(request, 'home.html')


def main_app(request, id=-1):
    artic_tab = ArticleTab.objects.all()
    if id < 0:
        first_tab = artic_tab.first()
        id = first_tab.id

    artic_content = ArticleContent.objects.filter(tid=id)
    print(request.GET.get('search'))
    if request.GET.get('search'):
        artic_content = artic_content.filter(title__icontains=request.GET.get('search'))

    return render(request, 'main_app.html', locals())


def main_app2(request):
    return render(request, 'main_app2.html')


def send_message(request):
    try:
        code = random.randint(100000, 999999)
        send_messages('18249241924', (code, 10))
    except Exception as e:
        print(e)
        return HttpResponse('bad')
    else:
        return HttpResponse('ok')

