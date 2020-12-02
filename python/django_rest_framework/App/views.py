from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from rest_framework import response
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from App.models import Column
from App.serializer import ColumnSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import BasePermission
from App.per import MyPermission, MyAuth
from App.mythrottle import VisitThrottle
from App.auth import token_confirm
from App.pagination import PageNumberPaginator
from App.filter_app import ColumnFilter


class Index(APIView):
    # throttle_classes = (VisitThrottle,)
    def get(self, request, column_id=-1):
        # 获取queryset
        columns = Column.objects.all()
        # 开始序列化； 正向序列化
        serializer_data = ColumnSerializer(instance=columns, many=True)

        # print(serializer_data)

        # print(serializer_data.data)

        # 获取序列化后的数据，返回给客户端
        return Response(serializer_data.data)

    def post(self, request, column_id=-1):
        # 获取数据
        client_data = request.data
        # 序列化数据 反向序列化
        verified_data = ColumnSerializer(data=client_data)
        # print(verified_data)

        # 校验数据
        if verified_data.is_valid():
            column = verified_data.save()
            # print(verified_data.data) # 需要保存之后才能获取.data
            # verified_data.create(verified_data)
            return Response(verified_data.data)
        else:
            return Response(verified_data.errors, status=400)

    def put(self, request, column_id):
        column_obj = Column.objects.get(pk=column_id)
        verified_data = ColumnSerializer(instance=column_obj, data=request.data)
        # 校验数据
        if verified_data.is_valid():
            column = verified_data.save()
            # print(verified_data.data) # 需要保存之后才能获取.data
            return Response(verified_data.data)
        else:
            return Response(verified_data.errors, status=400)

    def delete(self, request, column_id):
        column_obj = Column.objects.get(pk=column_id)
        column_obj.delete()
        return Response({'message': 'OK'})


# 创造新的类 继承于CreateAPIView
# class CreateTab(CreateAPIView):
#     serializer_class = ColumnSerializer


# 这个写法和上面的写法效果是一样的，上面的类继承了这两个类
class CreateTab(GenericAPIView, CreateModelMixin):
    serializer_class = ColumnSerializer

    def post(self, request):
        self.create(request)


class RetrieveTab(RetrieveAPIView):
    authentication_classes = (MyAuth,)
    permission_classes = (MyPermission,)
    queryset = Column
    serializer_class = ColumnSerializer


class Login(APIView):
    def get(self, request):
        token = token_confirm.generate_validate_token('yby')
        print(token)
        return JsonResponse({'token': token})


class TestToken(APIView):
    authentication_classes = (MyAuth,)

    def get(self, request):
        return JsonResponse({'detail': 'success'})


class GetData(ListAPIView):
    """
    get:
    获取列表

    """
    queryset = Column.objects.all()
    filter_class = ColumnFilter  # 过滤类
    pagination_class = PageNumberPaginator
    serializer_class = ColumnSerializer

    # def get(self, request):
    #     # book_queryset = Column.objects.all()
    #     # 1.实例化PageNumberPaginator
    #     page_obj = PageNumberPaginator()
    #     # 2.调用paginate_queryset方法获取当前页的数据
    #     page_data = page_obj.paginate_queryset(queryset=self.queryset, request=request, view=self)
    #     # 3.将获取的数据放入序列化器中进行匹配
    #     serializer_data = ColumnSerializer(page_data, many=True)
    #     # 4.返回带超链接的且有上一页和下一页的数据
    #     return page_obj.get_paginated_response(serializer_data.data)
