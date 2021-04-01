from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings as django_settings
from rest_framework.response import Response

from user import models
from user import serializer
from user.filter import UserFilter
from user.pagination import PageNumberPaginator
from user.serializer import User, Permission, AddPermission
from user.token import token_confirm

salt = '123abcABC@'

SuccessMessage = {
    'code': 200,
    'status': 'success',
    'result': ''
}

ErrorMessage = {
    'code': 500,
    'status': 'bad',
    'result': '请求失败'
}


class Register(GenericAPIView):
    serializer_class = serializer.Register
    authentication_classes = ()
    queryset = models.User.objects.all()

    def post(self, request):
        data = self.get_serializer(data=request.data)
        if data.is_valid():
            data = data.data
            password = make_password(data.get('password'), salt=salt)
            data['password'] = password
            data['register_ip'] = request.META.get('REMOTE_ADDR')
            data['salt'] = salt
            data.pop('verify')
            self.queryset.create(**data)
            SuccessMessage['result'] = data
            return Response(SuccessMessage)
        return Response({'msg': data.errors})


class Login(GenericAPIView):
    serializer_class = serializer.Login
    authentication_classes = ()
    queryset = models.User.objects.all()

    def get_queryset(self):
        self.queryset = self.queryset.filter(username=self.request.data.get('username')).first()

        if self.queryset and check_password(self.request.data.get('password'), self.queryset.password):
            return True
        else:
            return False

    def post(self, request):

        serializer_data = self.get_serializer(data=request.data)
        if not self.get_queryset():
            ErrorMessage['result'] = '账号或密码错误'
            return Response(ErrorMessage)

        if serializer_data.is_valid():
            token = token_confirm.generate_validate_token(self.queryset.id)
            self.queryset.token = token
            self.queryset.login_ip = request.META.get('REMOTE_ADDR')
            self.queryset.login_num = int(self.queryset.login_num) + 1 if self.queryset.login_num else 1
            self.queryset.save()
            SuccessMessage['result'] = {'token': token, 'msg': '登陆成功'}
            return Response(SuccessMessage)
        ErrorMessage['result'] = serializer_data.errors
        return Response(ErrorMessage)


class UserList(ListAPIView):
    authentication_classes = ()
    queryset = models.User.objects.all()
    filter_class = UserFilter  # 过滤类
    pagination_class = PageNumberPaginator
    serializer_class = User


class Captcha(APIView):
    def get(self, request):
        try:
            hashkey = CaptchaStore.generate_key()
            image_url = captcha_image_url(hashkey)
            id_ = CaptchaStore.objects.filter(hashkey=hashkey).first().id
            SuccessMessage['result'] = [{'image_url': image_url, 'img_id': id_}]
            return JsonResponse(SuccessMessage)
        except:
            Response(ErrorMessage)


class PermissionList(ListAPIView):
    authentication_classes = ()
    queryset = models.Rule.objects.all()
    serializer_class = Permission

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        SuccessMessage['result'] = serializer.data
        return Response(SuccessMessage)


class PermissionPost(CreateAPIView):
    queryset = models.Rule
    serializer_class = AddPermission
    authentication_classes = ()


class UpdatePermission(APIView):
    queryset = models.Rule.objects.all()
    serializer_class = Permission

    def post(self, request):
        id = request.data.get('id')
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            if serializer_data.data['rule_level'] == 1 and serializer_data.data['parents_id']:

                self.queryset.filter(pk=id).update(**serializer_data.data)

                SuccessMessage['result'] = serializer_data.data
                return Response(SuccessMessage)
            else:
                ErrorMessage['result'] = 'parents_id 字段必须存在'
                return Response(ErrorMessage)
        ErrorMessage['result'] = serializer_data.errors
        return Response(ErrorMessage)


class DelPermission(APIView):
    queryset = models.Rule.objects.all()
    serializer_class = Permission

    def post(self, request):
        id = request.data.get('id')
        try:
            self.queryset = self.queryset.filter(pk=id).first()
            self.queryset.delete()
            models.RuleGroup.objects.all().filter(rule_id=id).delete()
        except:
            return Response(ErrorMessage)
        return Response(SuccessMessage)


class GroupRule(APIView):

    def get(self, request):
        group_id = request.data.get('id')
        serializer_instance = models.Group.objects.filter(id=group_id)
        serializer_data = serializer.GroupRule(instance=serializer_instance, many=True)
        SuccessMessage['result'] = serializer_data.data
        return Response(SuccessMessage)


class TestQueryset(APIView):
    def get(self, request):
        user = models.User.objects.filter().values()
        for i in user:
            print(i)
        return Response({'code': ''})
