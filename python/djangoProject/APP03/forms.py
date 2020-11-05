from captcha.fields import CaptchaField
from django import forms

# 有两种发发进行校验
from django.core.exceptions import ValidationError

'''
第一种：结合model,继承django.forms.ModelForm
    class xxx(models.Model):
        字段 = models.CharField(max_length=30)
        
    class xxxForm(ModelForm):
        class Meta
            model = xxx
            field = ('字段') # 只显示model中指定的字段 ，显示所有用__all__
            
第二种：直接继承form # 推荐用第二种，可以用他自带的校验规则
    from django import forms
    class xxxForm(forms.Form):
        pass
'''


def mobile_validate(value):
    import re
    mobile_re = re.compile("^(13[0-9]|14[579]|15[0-3,5-9]|1 6[6]|17[0135678]|18[0-9]|19[89])\\d{8}$")
    if not mobile_re.match(value):
        print('123123')
        raise forms.ValidationError('手机号码格式不对哦')


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=20, required=True, label='请输入用户名', error_messages={
        'min_length': '用户名最少3位',
        'max_length': '用户名最多20位',
        'required': '用户名不能为空',
    })  # 用户名最多20个字符最少三个字符
    password = forms.CharField(min_length=3, max_length=20, required=True, label='请输入密码', error_messages={
        'min_length': '密码最少3位',
        'max_length': '密码最多20位',
        'required': '密码不能为空',
    })

    confirm = forms.CharField(min_length=3, max_length=20, required=True, label='请输入密码', error_messages={
        'min_length': '密码最少3位',
        'max_length': '密码最多20位',
        'required': '密码不能为空',
    })

    regtime = forms.DateTimeField(required=True, label='请输入时间', error_messages={
        'invalid': '时间格式错误',
        'required': '时间不能为空',
    })

    sex = forms.BooleanField(required=False)

    mobile = forms.CharField(
        validators=[mobile_validate],
        error_messages={'required': '手机号不填不行'},
    )

    # 单个字段验证 clean_xxxx
    def clean_password(self):
        if self.cleaned_data.get('password').isdigit() or self.cleaned_data.get('password').isalpha():
            raise ValidationError('密码必须包含字母和数字')
        else:
            return self.cleaned_data['password']

    # def clean_valid_code(self):
    #     if self.cleaned_data.get('valid_code').upper() == self.request.session.get('valid_code'):
    #         return self.cleaned_data['valid_code']
    #     else:
    #         raise ValidationError('验证码不正确')

    # 全局验证
    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm'):
            raise ValidationError({'confirm': '密码不一致'})
        # 这块必须有键值对，没有键值对不知道是哪错了
        else:
            return self.cleaned_data


class Login(forms.Form):
    captcha = CaptchaField()
