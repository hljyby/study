"""


"""

from django_filters import rest_framework as filters

from App.models import Column


class ColumnFilter(filters.FilterSet):
    class Meta:
        model = Column  # 模型名
        fields = {
            'name': ['icontains']
        }
