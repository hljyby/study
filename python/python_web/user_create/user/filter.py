from django_filters import rest_framework as filters

from user.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User  # 模型名
        fields = {
            'username': ['icontains']
        }
