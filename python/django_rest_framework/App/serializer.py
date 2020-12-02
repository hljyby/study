from rest_framework import serializers
from App.models import Column


class ColumnSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, label='栏目',help_text='姓名')
    link_url = serializers.URLField(label='链接')
    index = serializers.IntegerField(label='位置')
    email = serializers.EmailField(required=False)

    def create(self, validated_data):  # create()和update()方法定义了在调用serializer.save()时成熟的实例是如何被创建和修改的。
        return Column.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.link_url = validated_data.get('link_url', instance.link_url)
        instance.index = validated_data.get('index', instance.index)
        instance.save()
        return instance
