from collections import OrderedDict

from rest_framework.pagination import BasePagination, PageNumberPagination
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response


class PageNumberPaginator(PageNumberPagination):
    page_size = 10  # 每页显示10条数据
    page_size_query_param = 'size'  # 每页显示条数的参数名称
    page_query_param = 'page'  # 页码参数名称,比如page=3&size=10 第三页显示10条
    max_page_size = 10  # 最大页码数量控制
    page_query_description = _('页码')
    page_size_query_description = _('每页现实的数量')

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('code', '200'),
            ('status', 'success'),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)

        ]))
