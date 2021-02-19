import jwt
from time import time
from server import settings
from rest_framework.authentication import BaseAuthentication, get_authorization_header, exceptions
from jwt.exceptions import ExpiredSignatureError
from django.contrib.auth import get_user_model
ECUser = get_user_model()


# to generate jwt token, once user logged, response with this token for browser local storage
def generate_jwt(user, exp_days=7):
    exp_timestamp = int(time() + (exp_days * 24 * 60 * 60))
    return jwt.encode({'userid': user.pk, 'exp': exp_timestamp}, settings.SECRET_KEY).decode('utf-8')


# when get a request from frontend, server try to get authorization header and decode the token
# if the token is valid, not expired, user valid, return user and token to frontend.
class JWTAuthentication(BaseAuthentication):
    keyword = 'JWT'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header. Token string itself should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            token_info = jwt.decode(jwt_token, settings.SECRET_KEY)
            userid = token_info.get('userid')
            try:
                user = ECUser.objects.get(pk=userid)
                return user, jwt_token
            except ValueError:
                msg = 'User does not exist!'
                raise exceptions.AuthenticationFailed(msg)
        except ExpiredSignatureError:
            msg = 'Login token expired!'
            raise exceptions.AuthenticationFailed(msg)