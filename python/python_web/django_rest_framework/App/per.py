from rest_framework.permissions import BasePermission
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from App.auth import token_confirm
import itsdangerous


class MyPermission(BasePermission):
    message = '无权访问，您的用户等级太低，充值888元立得永久VIP特权 '

    def has_permission(self, request, view):
        print(view)
        return False


class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        try:
            user = token_confirm.confirm_validate_token(token, expiration=6)
        except itsdangerous.exc.SignatureExpired as e:
            raise exceptions.AuthenticationFailed({'code': 200, 'mes': 'token过期请重新登陆'})
        except:
            return None
        return user, token
