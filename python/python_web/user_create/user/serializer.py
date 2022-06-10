from datetime import datetime, timedelta

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from captcha.models import CaptchaStore

from user import models


class Register(ModelSerializer):
    verify = serializers.CharField()
    username = serializers.CharField(validators=[UniqueValidator(models.User.objects.all(), message="该名称已经注册了")])

    class Meta:
        model = models.User
        fields = ['username', 'password', 'verify']

        # fields = '__all__'
        # read_only_fields = ['verify']

    # def validate_username(self, value):
    #     if models.User.objects.all().filter(username=value):
    #         raise serializers.ValidationError({'msg': 'bad'})
    #     return value


class Login(ModelSerializer):
    captcha = serializers.CharField(required=True, error_messages={'required': '验证码必须输入'})
    username = serializers.CharField(required=True, error_messages={'required': '用户名必须输入'})
    password = serializers.CharField(required=True, error_messages={'required': '密码必须输入'})
    captcha_id = serializers.CharField(required=True, error_messages={'required': '验证码id 必须输入'})

    class Meta:
        model = CaptchaStore
        fields = ['username', 'password', 'captcha', 'captcha_id']

        # fields = '__all__'
        # read_only_fields = ['verify']

    def validate(self, attrs):
        try:
            image_code = CaptchaStore.objects.all().filter(id=attrs['captcha_id']).first()
        except:
            raise serializers.ValidationError('验证码不存在')
        one_minute_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if one_minute_ago > image_code.expiration:
            raise serializers.ValidationError('验证码过期')
        if not image_code.response == attrs['captcha']:
            raise serializers.ValidationError('验证码错误')
        del attrs['captcha_id']
        del attrs['captcha']
        return attrs


class User(ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class Permission(ModelSerializer):
    class Meta:
        model = models.Rule
        fields = '__all__'


class AddPermission(ModelSerializer):
    class Meta:
        model = models.Rule
        fields = '__all__'


class RuleSer(ModelSerializer):
    class Meta:
        model = models.Rule
        fields = '__all__'


class GroupRule(ModelSerializer):
    rule = serializers.SerializerMethodField()

    class Meta:
        model = models.Group
        fields = ['group_name', 'rule']
        # read_only_fields = ['rule']

    def get_rule(self, val):
        a = models.RuleGroup.objects.filter(group_id=val.id).values_list('rule_id')
        b = []
        for i in a:
            b.append(i[0])
        b = tuple(b)
        print(b)
        rules = models.Rule.objects.all().extra(select={'isCheck': "id in %s "}, select_params=(b,)).values()
        print(rules)
        return rules
