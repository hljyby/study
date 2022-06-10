from datetime import datetime, timedelta

from django.shortcuts import render, redirect


# Create your views here.

def check_login(func):
    def inner(*args, **kwargs):
        if args[0].COOKIES.get('username'):
            return func(*args, **kwargs)
        else:
            return redirect('App02:login')

    return inner


def login(request):
    if request.method == 'POST':
        print(request.POST.dict())

        response = redirect('App02:home')
        future = datetime.now() + timedelta(days=3)  # timedelate 时间间隔
        # 过期时间expires
        # response.set_cookie('username', request.POST.get('username'), expires=future)
        response.set_signed_cookie('username', request.POST.get('username'), salt='', expires=future)  # 加盐
        # 加盐的作用是不让随意自己修改不是为了保密
        request.session['username'] = request.POST.get('username')
        request.session['password'] = request.POST.get('password')
        request.session.set_expiry(5) # 默认两周
        return response
    return render(request, 'login.html')


@check_login
def home(request):
    username = request.COOKIES.get('username')
    # username = request.get_signed_cookie('username', salt='') # 获取加盐
    session = request.session.get('username')
    print('session=',session)
    return render(request, 'home1.html', locals())


def logout(request):
    response = redirect('App02:login')
    response.delete_cookie('username')
    # session 删除
    request.session.clear() # 清空所有session 但不会将session表中的数据删除
    request.session.flush() # 清空所有 并删除表中的数据
    request.session.logout() # 退出登录，清空所有 并删除表中的数据
    del request.session[key] # 删除摸一个session的值
    return response

