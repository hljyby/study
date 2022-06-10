from itsdangerous import URLSafeTimedSerializer as utsr

import base64
from django.conf import settings as django_settings


class Token():
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodebytes(self.security_key.encode('utf8'))

    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        return serializer.dumps(username, self.salt)

    def confirm_validate_token(self, token, expiration=3600):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)

    def remove_validate_token(self, token):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt)


token_confirm = Token(django_settings.SECRET_KEY)