from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password

from django.http import HttpResponse
from django.shortcuts import render, redirect

from APP03.forms import RegisterForm, Login
from APP03.models import User

# Create your views here.

# @login_required(login_url='APP03:login')
from APP03.uploads import FileUpload
from djangoProject.settings import MEDIA_ROOT


def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            print('data=', data)

            print('username=', data.get('username'))

            return HttpResponse('ok')
        else:
            return render(request, 'register.html', {'form': form})
    # hashkey = CaptchaStore.generate_key()
    # image_url = captcha_image_url(hashkey)
    return render(request, 'register.html')


def form(request):
    form = {'username': 'yby', 'password': 'a123'}
    user = User.objects.create_user(**form)
    # 用户写入数据库，他会自动签名加密
    # user.set_password('123') # 修改密码
    # user.save()
    if user:
        return HttpResponse('ok')
    return HttpResponse('bad')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        # password = make_password('123')
        # print(check_password('123',password))
        if user:
            login(request, user)
            form = Login(request.POST)
            if form.is_valid():
                return redirect('APP03:logout')
            else:
                hashkey = CaptchaStore.generate_key()
                image_url = captcha_image_url(hashkey)
                return render(request, 'login.html', locals())
        else:
            return HttpResponse('登陆失败，请从新登录 ')
    form = Login()
    # print(form)
    hashkey = CaptchaStore.generate_key()
    image_url = captcha_image_url(hashkey)
    return render(request, 'login.html', locals())


# 路由守护 login_url 代表你没登录跳转到那个页面上去
# @login_required(login_url='APP03:login')
def user_logout(request):
    username = request.user
    is_login = username.is_authenticated
    if request.GET.get('logout'):
        logout(request)
        return redirect('APP03:login')
    return render(request, 'home1.html', locals())


def email(request):
    from django.core.mail import send_mail
    from django.core.mail import send_mass_mail
    from django.conf import settings
    from django.template import loader
    from django.core.mail import EmailMultiAlternatives
    # 模板
    # subject, from_email, to = 'html', settings.DEFAULT_FROM_EMAIL, '230106199@qq.com'
    # html_content = loader.get_template('active.html').render({'username': '小花猫'})
    # msg = EmailMultiAlternatives(subject=subject, from_email=from_email, to=[to])
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()

    # 发送单个
    # send_mail('标题', '内容', settings.DEFAULT_FROM_EMAIL,
    #           ['230106199@qq.com'], fail_silently=False)
    # 发送多个
    msg1 = ('标题', '内容', settings.DEFAULT_FROM_EMAIL, ['230106199@qq.com'])
    msg2 = ('标题', '内容', settings.DEFAULT_FROM_EMAIL, ['230106199@qq.com'])

    send_mass_mail((msg1, msg2), fail_silently=False)
    return HttpResponse('邮件发送成功')


def artical(request):
    if request.method == 'POST':
        print(request.POST.get('content'))
    return render(request, 'artical.html')


def uploads(request):
    if request.method == 'POST':  # 获取对象
        obj = request.FILES.get('fafafa')
        import os
        # # 上传文件的文件名 　　　　
        # f = open(os.path.join(MEDIA_ROOT, 'pic', obj.name), 'wb')
        # if obj.multiple_chunks():
        #     for chunk in obj.chunks():
        #         f.write(chunk)
        #     print('大于2.5')
        # else:
        #      f.write(obj.read())
        #     print('小于2.5')
        # f.close()
        path = os.path.join(MEDIA_ROOT, 'pic')
        print(path)
        fp = FileUpload(obj, exts=['MOV'])
        print(fp.upload(path))
        if fp.upload(path):
            return HttpResponse('OK')
        else:
            return HttpResponse('bad')
    return render(request, 'uploads.html')
