from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from user.token import token_confirm
import itsdangerous

ErrorMessage = {
    'code': 500,
    'status': 'error',
    'result': '请求失败'
}


class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        try:
            user = token_confirm.confirm_validate_token(token, expiration=120)
        except itsdangerous.exc.SignatureExpired as e:
            ErrorMessage['result'] = {'msg': 'token过期请重新登陆'}
            raise exceptions.AuthenticationFailed(ErrorMessage)
        except:
            return None
        return user, token
