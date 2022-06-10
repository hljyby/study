from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views.decorators.cache import cache_page

from django.core.mail import send_mail

from APP03.models import User
from App04.token import token_confirm
from django.conf import settings


# 缓存20秒
# @cache_page(20)
def index(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    pre_time = datetime.now() - timedelta(days=3)
    pre_time = pre_time.strftime('%Y-%m-%d %H:%M:%S')
    print(current_time, pre_time)
    return render(request, 'index.html', locals())


def SetCache(request):
    from django.core.cache import cache
    from django.template import loader

    mycache = cache.get('mycache')
    if mycache:
        html = mycache
    else:
        tem = loader.get_template('mycache.html')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        html = tem.render({'app': current_time})
        cache.set('mycache', html, 10)
    return HttpResponse(html)


def checkUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        form = {'username': username, 'password': password, 'is_active': 0}
        if User.objects.filter(username=username).first():
            return HttpResponse('用户已存在')
        else:
            user = User.objects.create(**form)
            token = token_confirm.generate_validate_token(user.id)
            print(token)
            url = 'http://' + request.get_host() + reverse('App04:activeuser', kwargs={'token': token})
            print(url)
            html = loader.get_template('email_template.html').render({'url': url})
            # 发送单个
            send_mail('激活账号', '', settings.DEFAULT_FROM_EMAIL,
                      [email], html_message=html, fail_silently=False)
            return HttpResponse('邮件已发送')
    return render(request, 'checkUser.html')


def activeuser(request, token):
    try:
        id = token_confirm.confirm_validate_token(token)
    except:
        id = token_confirm.remove_validate_token(token)
        users = User.objects.filter(pk=id)
        for user in users:
            user.delete()
        return HttpResponse('链接过期请重新注册')
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return HttpResponse('您验证的用户不存在，请重新注册')
    user.is_active = True
    user.save()
    return HttpResponse('验证成功,请登录')
